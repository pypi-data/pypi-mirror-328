import os
import yaml
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, Dict
from gai.lib.common.utils import get_app_path
from gai.lib.common.logging import getLogger
logger = getLogger(__name__)

class ModuleConfig(BaseSettings):
    name: str
    class_: str = Field(alias="class")  # Use 'class' as an alias for 'class_'

    class Config:
        allow_population_by_name = True  # Allow access via both 'class' and 'class_'

class GaiGeneratorConfig(BaseSettings):
    type: str
    engine: str
    model: str
    name: str
    hyperparameters: Optional[Dict] = {}
    extra: Optional[Dict] = None
    module: ModuleConfig
    class Config:
        extra = "allow"

    @classmethod
    def from_name(cls,name:str, file_path:str=None) -> "GaiGeneratorConfig":
        return cls._get_generator_config(name=name, file_path=file_path)
    
    @classmethod
    def from_dict(cls, config:dict) -> "GaiGeneratorConfig":
        return cls._get_generator_config(config=config)
    
    @staticmethod
    def _find_caller_module_path():
        import inspect
        """
        Finds the path of the module that originally called into the GaiGeneratorConfig,
        ignoring any calls that originate from 'site-packages'.
        """
        # Traverse the stack from the current call upwards
        for frame_info in inspect.stack():
            module = inspect.getmodule(frame_info.frame)
            if module and hasattr(module, '__file__'):
                file_path = module.__file__
                # Skip frames where the file path contains 'site-packages'
                if 'site-packages' not in file_path:
                    # Return the directory of the first matching file
                    return os.path.dirname(file_path)
        
        raise ValueError("Could not find a calling module path outside of 'site-packages'.")           
    
    @classmethod
    def _update_gai_config(cls,name:str, gai_dict:dict, global_lib_config_path:str) -> "GaiGeneratorConfig":


        import glob
        
        here = cls._find_caller_module_path()
        # here = os.path.abspath(os.path.dirname(__file__))
        
        # traverse to the parent directory until we find the pyproject.toml
        
        while not os.path.exists(os.path.join(here, "pyproject.toml")):
            here = os.path.abspath(os.path.join(here, ".."))
            if here == "/":
                raise ValueError("GaiGeneratorConfig: pyproject.toml not found")
        
        # look for the file ./src/**/config/gai.yml
        namespace_dir = os.path.join(here, "src", "**", "config")
        config_path = os.path.join(namespace_dir, "gai.yml")
        config_files = glob.glob(config_path, recursive=True)
                        
        if not config_files:
            raise FileNotFoundError("GaiGeneratorConfig: gai.yml not found in the specified paths")

        # Read the first matching config file

        config_path = config_files[0]
        with open(config_path, 'r') as f:
            generator_dict = yaml.load(f, Loader=yaml.FullLoader)

        if not generator_dict.get("generators", None):
            raise ValueError(f"GaiGeneratorConfig: 'generators' key is required but not found in {config_path}.")
        
        if not generator_dict["generators"].get(name, None):
            raise ValueError(f"GaiGeneratorConfig: Generator Key {name} is not found in {config_path}.")
        
        # Update global config with the new generator config
        
        gai_dict["generators"][name] = generator_dict["generators"][name]
        
        with open(global_lib_config_path, 'w') as f:
            yaml.dump(gai_dict, f, sort_keys=False,indent=4)
                            
        logger.warning(f"GaiGeneratorConfig: Generator Config not found. name={name}. Config added to {global_lib_config_path}")            

        return generator_dict["generators"][name]
    
    @classmethod
    def _get_generator_config(
            cls,
            name: Optional[str] = None,
            config: Optional[dict] = None,
            file_path: Optional[str] = None    
        ) -> "GaiGeneratorConfig":
        if config:
            return cls(**config)
        if name:
            gai_dict = None
            try:
                app_dir=get_app_path()
                global_lib_config_path = os.path.join(app_dir, 'gai.yml')
                if file_path:
                    global_lib_config_path = file_path
                with open(global_lib_config_path, 'r') as f:
                    gai_dict = yaml.load(f, Loader=yaml.FullLoader)
            except Exception as e:
                raise ValueError(f"GaiClientConfig: Error loading client config from file: {e}")

            generator_config = None
            
            generator_config = gai_dict["generators"].get(name, None)

            if not generator_config:
                
                generator_config = cls._update_gai_config(
                    name=name, 
                    gai_dict=gai_dict, 
                    global_lib_config_path=global_lib_config_path)

            return cls(**generator_config)

        raise ValueError("GaiGeneratorConfig: Invalid arguments. Either 'name' or 'config' must be provided.")
