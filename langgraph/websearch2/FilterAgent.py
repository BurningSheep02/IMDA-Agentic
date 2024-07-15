from Agent import Agent

class FilterAgent(Agent):
    def __init__(self, local_llm='elvee/hermes-2-pro-llama-3:8b-Q5_K_M', temperature=0.0):  
        super().__init__(self, local_llm=local_llm, temperature=temperature)
    
    def filter(self,id,context,text):
        self.system_prompt = f"""
        You are an expert whose job is to identify whether a piece of text is relevant to a stated topic.
        Return "Yes" if you believe that the text is relevant, and "No" otherwise.

        The stated topic is {context}.

        The given piece of text follows:
        """
        try:
            output = super().send(text)
            print(f"Finished filtering text #{id}\n----")
            match output:
                case "Yes":
                    return True
                case "No":
                    return False
                case _:
                    print(f"{output}")
                    return False
        except Exception as e:
            print(f"Error occured with filtering text #{id}:\n----")
            print(e)
            return False