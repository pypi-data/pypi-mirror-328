from pathlib import Path
from rich.console import Console
import shutil
import json

def init(force=False):
    console=Console()

    # Download nltk data
    try:
        import nltk
        nltk.download("punkt")
        nltk.download("punkt_tab")
        nltk.download("averaged_perceptron_tagger_eng")
    except:
        console.print("[red]Failed to download nltk data[/]")

    # Initialise config

    if not force and (Path("~/.gairc").expanduser().exists() or Path("~/.gai").expanduser().exists()):
        console.print("[red]Already exists[/]")
        return
    
    # app_dir doesn't exist
    if not Path("~/.gai").expanduser().exists():
        Path("~/.gai").expanduser().mkdir()

    # models directory doesn't exist
    if not Path("~/.gai/models").expanduser().exists():
        Path("~/.gai/models").expanduser().mkdir()

    # nodes directory doesn't exist
    from gai.lib.common.utils import get_packaged_data_path
    source_path = get_packaged_data_path()
    source_persona_path = source_path / "persona"
    
    if not Path("~/.gai/persona/nodes").expanduser().exists():
        Path("~/.gai/persona/nodes").expanduser().mkdir(parents=True)
        
        # cp -rp gai-data/src/gai/data/persona/* ~/.gai/persona/nodes
        for item in Path(source_persona_path).glob("*"):
            if item.is_dir():
                shutil.copytree(item, Path("~/.gai/persona/nodes").expanduser() / item.name)
            else:
                shutil.copy(item, Path("~/.gai/persona/nodes").expanduser() / item.name)

    # Force create .gairc
    with open(Path("~/.gairc").expanduser(), "w") as f:
        f.write(json.dumps({
            "app_dir":"~/.gai"
        }))

    # Finally
    if Path("~/.gairc").expanduser().exists() and Path("~/.gai").expanduser().exists():
        console.print("[green]Initialized[/]")

    from gai.lib.common.utils import get_packaged_gai_config_path
    source_path = get_packaged_gai_config_path()
    console.print(f"[yellow] copy from {source_path}[/yellow]")
    dest_path = Path("~/.gai").expanduser()
    console.print(f"Copying [yellow]{source_path}[/] to [yellow]{dest_path}[/]")
    shutil.copy2(source_path, dest_path)
    
if __name__=="__main__":
    init(True)