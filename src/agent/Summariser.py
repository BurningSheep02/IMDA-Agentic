
from agent.Agent import Agent

class Summariser(Agent):
    def __init__(self,local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)

    def summarise(self, docArr, subject=""):
        textArr = [x.page_content for x in docArr]

        self.system_prompt = """
        You are an expert whose task is to give a summary of texts.
        """

        if subject != "":
            self.system_prompt += "Only include content relevant to " + subject + ". Ignore all content not relevant to " + subject
        return super().send("\n".join([f"{i}. {t}" for (i, t) in enumerate(textArr)]), printout=True)
    
    