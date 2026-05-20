from pathlib import Path
from treestxt import Treetxt
if __name__=="__main__":
    file=Path(__file__).parent
    target_path=file/"test_target"
    save_path=file/"test_tree.txt"
    Treetxt(target_path,save=save_path)