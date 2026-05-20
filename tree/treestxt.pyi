import os
class Treetxt:
    def __init__(
        self,
        path:str|os.PathLike=...,
        save:str|os.PathLike=...,
        skip:str|list|tuple|None=None
    )->None:
        """
            ドライブ内のパスまたはディスクのディレクトリ構造をテキストファイルで保存する。
            
            :param path: ディレクトリ構造を表示するディレクトリを指定する。
            :type path: str|os.PathLike
            :param save: 保存するテキストファイルのファイルパスを指定する。
            :type save: str|os.PathLike
            :param skip: 表示しないファイル名とフォルダ名を指定する。
            :type skip: str|list|tuple|None
        """