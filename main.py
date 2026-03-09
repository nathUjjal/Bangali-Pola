from app import LlamaModel , ChatGroqLLM
from generate_prompts import GeneratePrompts
from banner import banner

MODEL_NAME = "Mistral-7B-Instruct-v0.3-Q4_K_M.gguf"
REPO_ID = "bartowski/Mistral-7B-Instruct-v0.3-GGUF"

# model = LlamaModel(model_name=MODEL_NAME, repo_id=REPO_ID)
model = ChatGroqLLM()
prompts = GeneratePrompts(prompts_file="prompts.yml")

def main( input_query = "Introduce your self breifly" ):
    full_prompt = prompts.get_completed_prompt(new_usr_prompt=input_query)
    response = model.generate_response(prompt=full_prompt)
    prompts.append_llm_response(response)
    print("Response from the model:")
    print(response)

if __name__ == "__main__":
    banner()
    while True:
        query = input("Enter your query: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting the agent. Goodbye!")
            break
        main(input_query=query)

