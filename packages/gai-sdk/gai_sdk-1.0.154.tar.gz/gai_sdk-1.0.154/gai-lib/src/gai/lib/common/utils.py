import os, sys, re, time
import json
from gai.lib.common import constants
import yaml
import importlib.resources as pkg_resources

def get_packaged_data_path():
    return pkg_resources.path('gai.data', '')

# This is where the file is stored in the package directory and is used for copying the config file to the user's home directory during initialization
def get_packaged_gai_config_path():
    return pkg_resources.path('gai.data', 'gai.yml')

# This is where the file is stored in the package directory and is used for starting the docker containers
def get_packaged_docker_compose_path():
    path = pkg_resources.path('gai.data', 'docker-compose.yml')
    return path

# Get JSON FROM ~/.gairc
def get_rc():
    if (not os.path.exists(os.path.expanduser(constants.GAIRC))):
        raise Exception(f"Config file {constants.GAIRC} not found. Please run 'gai init' to initialize the configuration.")
    with open(os.path.expanduser(constants.GAIRC), 'r') as f:
        return json.load(f)

# Get "app_dir" from ~/.gairc
def get_app_path():
    rc = get_rc()
    app_dir=os.path.abspath(os.path.expanduser(rc["app_dir"]))
    return app_dir

def this_dir(file):
    return os.path.dirname(os.path.abspath(file))

def root_dir():
    here = this_dir(__file__)
    root = os.path.abspath(os.path.join(here, '..', '..', '..', '..', '..'))
    print(f"Root directory: {root}")
    return root

# Create ~/.gai/cache
def mkdir_cache():
    cache_dir = os.path.expanduser('~/.gai/cache')
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir

def is_url(s):
    return re.match(r'^https?:\/\/.*[\r\n]*', s) is not None

def sha256(text):
    import hashlib
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def timestamp():
    return int(time.time() * 1000)

def find_url_in_text(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = re.findall(url_pattern, text)
    return urls

def clean_string(s):
    if s is None:
        return ''
    return re.sub(r'\s+', ' ', s)

def free_mem():
    from rich.console import Console
    console = Console()    
    import pynvml
    pynvml.nvmlInit()
    handle=pynvml.nvmlDeviceGetHandleByIndex(0)
    info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    free_amt = info.free / 1024**3
    if free_amt < 4:
        console.print(f"Free memory: [bright_red]{free_amt:.2f} GB[/]")
    else:
        console.print(f"Free memory: [bright_green]{free_amt:.2f} GB[/]")
    pynvml.nvmlShutdown()
    return info.free / 1024**3
