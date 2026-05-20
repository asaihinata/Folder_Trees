from pathlib import Path
from trees import Tree
if __name__=="__main__":
    file=Path(__file__).parent
    target_path=file/"test_target"
    Tree(target_path)