import os, ConfigParser, pickle

def get_config():
    working_dir = os.getcwd()
    if(os.path.exists(os.path.join(working_dir, ".warnup")) is False):
        return None
    
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(working_dir, ".warnup"))

    return config

def get_staged():
    config = get_config()

    # Get the path of the .warnupstage
    development = config.get("paths", "development")
    staged_file = os.path.join(development, ".warnupstage")
    
    if(os.path.exists(staged_file) == False):
        return []

    f = open(staged_file, "rb")
    staged = pickle.load(f)
    f.close()
    
    return staged

def save_staged(staged):
    config = get_config()

    # Get the path of the .warnupstage
    development = config.get("paths", "development")
    staged_file = os.path.join(development, ".warnupstage")
    
    f = open(staged_file, "wb")
    pickle.dump(staged, f)
    f.close()

def stage(path):
    # Get the pickled data
    staged = get_staged()
    staged.append(path)
    
    save_staged(staged)

def unstage(path):
    staged = get_staged()
    try:
        staged.remove(path)
    except ValueError:
        return False
    
    save_staged(staged)
    return True

