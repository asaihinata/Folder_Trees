import glob
from pathlib import Path,PosixPath,WindowsPath
TypePath=Path|WindowsPath|PosixPath
class Treetxt:
    def __init__(self,path,save,skip=None):
        if isinstance(path,TypePath):
            path=self._pathlist(path)
        if isinstance(save,TypePath):
            save=self._pathlist(save)
        if isinstance(skip,str):
            self.skiplist=[skip]
        elif isinstance(skip,list|tuple|TypePath):
            self.skiplist=self._pathlist(skip)
        else:
            self.skiplist=None
        self.txt=""
        self.tree(path=path,root=str(Path(path).parent))
        with open(save,"w",encoding="utf-8") as f:
            f.write(self.txt[:-1])
    def _pathlist(self,path):
        def types(path):
            if isinstance(path,TypePath):
                return True
            else:
                return False
        if types(path):
            return str(path)
        elif isinstance(path,str):
            return path
        elif isinstance(path,list|tuple):
            return[str(i) if types(i) else i for i in path]
    def tree(
        self,path="",layer=0,
        is_last=False,indent_current=" ",
        root="",skip=None
    ):
        def replaces(path:str):
            return Path(path).name
        if skip is not None:
            effective_skip=skip
        else:
            effective_skip=self.skiplist
        current=replaces(path.split("/")[::-1][0])
        if layer==0:
            self.txt+=f"{current}\n"
        else:
            self.txt+=f"{indent_current}{"└── " if is_last else "├── "}{current}\n"
        paths=[p for p in sorted(glob.glob(path+"/*")) if Path(p).is_dir() or Path(p).is_file()]
        ps=[p for p in sorted(glob.glob(path+"/.*")) if Path(p).is_dir() or Path(p).is_file()]
        if ps!=[]:
            for i in ps:
                paths.append(i)
        filtered_paths=[p for p in paths if effective_skip is None or Path(p).name not in effective_skip]
        for i,p in enumerate(filtered_paths):
            lens=(i==len(filtered_paths)-1)
            indent_lower=indent_current
            if layer!=0:
                if is_last:
                    indent_lower+="    "
                else:
                    indent_lower+="│   "
            if Path(p).is_dir():
                self.tree(p,layer=layer+1,is_last=lens,indent_current=indent_lower,root=root,skip=effective_skip)
            else:
                self.txt+=f"{indent_lower}{"└── " if lens else "├── "}{replaces(p.split("/")[::-1][0])}\n"