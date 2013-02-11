import os, ConfigParser, pickle, subprocess, datetime

def get_config():
    working_dir = os.getcwd()
    if(os.path.exists(os.path.join(working_dir, ".warnup")) is False):
        return None
    
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join(working_dir, ".warnup"))

    return config

def get_paths(path):
    """
    Returns a tuple with the development path, production path,
    and temporary path from the given argument path
    """
    config = get_config()

    # Get the paths
    development = config.get("paths", "development")
    production = config.get("paths", "production")
    dev_path = os.path.join(development, path)
    prod_path = os.path.join(production, path)

    # Get a temporary path
    split = list(os.path.split(prod_path))
    split[-1] += ".temp"
    temp_path = os.path.join(split[0], split[1])

    return (dev_path, prod_path, temp_path)

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

def push(path):
    dev_path, prod_path, temp_path = get_paths(path)

    if os.path.exists(prod_path):
        subprocess.call(["mv", prod_path, temp_path])
    subprocess.call(["cp", dev_path, prod_path])

def backup_restore(path):
    dev_path, prod_path, temp_path = get_paths(path)

    subprocess.call(["rm", prod_path])
    subprocess.call(["mv", temp_path, prod_path])

def backup_save(path):
    dev_path, prod_path, temp_path = get_paths(path)

    split = list(os.path.split(dev_path))
    datestr = datetime.datetime.now().strftime("%Y-%m-%d")
    split[-1] += ".%s.backup" % datestr
    save_path = os.path.join(split[0], split[1])
    subprocess.call(["mv", temp_path, save_path])

def backup_delete(path):
    dev_path, prod_path, temp_path = get_paths(path)

    subprocess.call(["rm", temp_path])
