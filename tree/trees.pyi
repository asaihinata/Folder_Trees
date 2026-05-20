import os
class Tree:
    def __init__(
        self,
        path:str|os.PathLike=...,
        skip:str|list|tuple|None=None
    )->None:
        """
            ディレクトリツリーを表示する
            
            :param path: ディレクトリのパスを指定する。
            :type path: str|os.PathLike
            :param skip: 表示しないファイルとフォルダ名を指定する。
            :type skip: str|list|tuple|None
        """