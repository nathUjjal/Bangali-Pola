import yaml
class GeneratePrompts:
    def __init__(self, prompts_file = "prompts.yml"):
        self.prompts_file = prompts_file
        self.index = 0
        self.prompts = []

    def get_system_prompt(self):
        with open(self.prompts_file, 'r') as file:
            self.sys_prompts = yaml.safe_load(file)
        #print("----------System prompt loaded!----------")
        self.prompts.extend(self.sys_prompts.get('system_prompt'))
    
    def append_user_prompt(self, new_prompt):
        #print("----------Appending user prompt to system prompt!----------")
        self.index += 1
        self.prompts.append({ "role": "user", 
                               "query_number": f"{self.index}",
                                    "content": new_prompt })
    
    def append_llm_response(self, response):
        self.prompts.append( { "role": "assistant", 
                                "query_number": f"{self.index}",
                                    "content": response })
    
    def get_completed_prompt(self,new_usr_prompt = None , new_llm_response = None):
        #print("----------Generating prompt for the model!----------")
        if not self.prompts:
            self.get_system_prompt()
        if new_usr_prompt is not None:
            self.append_user_prompt(new_usr_prompt);
        if new_llm_response is not None:
            self.append_llm_response(new_llm_response)
        for message in self.prompts:
            print(f"{message['query_number']} ||| {message['role']} : {message['content']}")
        return self.prompts
    
if __name__ == "__main__":
    prompts = GeneratePrompts(prompts_file="prompts.yml")
    while True:
        query = input("Enter your query: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting the agent. Goodbye!")
            break
        full_prompt = prompts.get_completed_prompt(new_usr_prompt=query)
        print("Generated prompt for the model:")
        print(full_prompt)
        for message in full_prompt:
            print(f"{message['query_number']} ||| {message['role']} : {message['content']}")