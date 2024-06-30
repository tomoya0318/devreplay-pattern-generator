import os
from dotenv import load_dotenv, find_dotenv

def load_env_file(item):
    # .envファイルを探す
    dotenv_path = find_dotenv()
    
    # .envファイルが見つからない場合はエラーを表示して終了
    if not dotenv_path:
        raise FileNotFoundError(".env file not found. Please create a .env file with the necessary configuration.")
        
    #.envファイルの読み込み
    load_dotenv()
    PATH = os.getenv(item)

    #ROOTがない時
    if not PATH:
        raise ValueError("ROOT is not set in .env file")
    
    return PATH

def create_directory(dir_name):
    ROOT = load_env_file('ROOT')
    # 指定されたディレクトリのパスを設定
    dir_path = os.path.join(ROOT, dir_name)
    
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"'{dir_name}' directory created at {dir_path}")
    else:
        print(f"'{dir_name}' directory already exists at {dir_path}")

# if __name__ == "__main__":
#     create_directory('out')