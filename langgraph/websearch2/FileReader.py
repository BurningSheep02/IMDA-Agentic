from Agent import Agent
import os
class FileReader(Agent):
    def __init__(self, basepath, local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M', temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)
        if (basepath):
            self.basepath = os.path.join(os.getcwd(), basepath)
        else:
            self.basepath = os.getcwd()
        self.file = None
    
    def read(self, file):
        with open(os.path.join(self.basepath, file), 'tr') as f:
            self.file = f.read()
            print(self.file)