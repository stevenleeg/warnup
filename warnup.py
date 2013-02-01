import ConfigParser, os

def get_config():
    working_dir = os.getcwd()
    if(os.path.exists(os.path.join(working_dir, ".warnup")) is False):
        return None
    
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(working_dir, ".warnup"))

    return config
