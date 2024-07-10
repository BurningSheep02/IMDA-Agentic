from Agent import Agent

class Summariser(Agent):
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)

    def summarise(self,textArr, subject=""):
        prompt = """
        You are an expert whose task is to give a summary of texts pertaining to the following subject: """ + subject + """
        \n The texts are listed below:
        """ + "\n".join([f"{i}. {t}" for (i, t) in enumerate(textArr)])
        print(prompt)
        self.system_prompt = prompt
        return super().send()
    
