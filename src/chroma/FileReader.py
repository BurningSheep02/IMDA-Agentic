
import os
from langchain_community.document_loaders import DirectoryLoader

class FileReader():
    def __init__(self, fpath):

        # Build the VectorStore from a list of given documents.
        if fpath:
            self.loader = DirectoryLoader(fpath, glob="**/*.txt")
        else:
            self.loader = DirectoryLoader(f"{os.getcwd()}/files/", glob="**/*.txt")
        return self.loader.load()