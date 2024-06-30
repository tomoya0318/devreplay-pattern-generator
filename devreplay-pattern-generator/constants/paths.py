import os
import sys
sys.path.append("../")
from _utils.setup_directories import load_env_file, create_directory

def get_project_paths():
    root = load_env_file('ROOT')
    config_path = os.path.join(root, "config.json")

    repo_dir = os.path.join(root, "tmp", "repos")
    pulls_dir = os.path.join(root, "tmp", "pulls")
    changes_dir = os.path.join(root, "out", "changes")


    return {
        "root": root,
        "config_path": config_path,
        "repo_dir": repo_dir,
        "pulls_dir": pulls_dir,
        "changes_dir": changes_dir
    }