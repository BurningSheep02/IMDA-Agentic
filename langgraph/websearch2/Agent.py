from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

class Agent:
    def __init__(self, system_prompt="", local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M',temperature=0.0):  
        self.llm = ChatOllama(model=local_llm, temperature=temperature)
        self.system_prompt = system_prompt
        self.log = {"inputs":[],"outputs":[]}

    def send(self, input="", printout=False) -> str:
        prompt = ChatPromptTemplate.from_messages(
        [("system", self.system_prompt), ("user", "{input}")]
        )

        output_chain = prompt | self.llm
        output = output_chain.invoke({"input": input})
        
        self.log["inputs"].append(input)
        self.log["outputs"].append(output.content)

        return output.content
    