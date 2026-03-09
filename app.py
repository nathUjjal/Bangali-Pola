from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

class LlamaModel:
    def __init__(self, model_name: str , repo_id: str):
        self.model_path = hf_hub_download(
            repo_id=repo_id, 
            filename=model_name,
            local_dir="./models"
        )
        self.model = Llama(
            model_path=self.model_path,
            n_threads=4,
            n_ctx=2048,
            verbose=False
        )

    def generate_responce(self, prompt: str, max_tokens: int = 256 , tempareture : float = 0.7 ) -> str:
        response = self.model.create_chat_completion(messages=prompt, max_tokens=max_tokens , temperature=tempareture)
        return response["choices"][0]["message"]["content"]
    
class ChatGroqLLM:
    def __init__(self,model_name="llama-3.1-8b-instant", temperature=0.5 , max_tokens=1024):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = ChatGroq(api_key = groq_api_key, 
                            model=model_name, 
                            temperature=temperature,
                            max_tokens=max_tokens)

    def generate_response(self, prompt: str):
        response = self.llm.invoke(input=prompt)
        return response.content
    
if __name__ == "__main__":
    # Example usage of LlamaModel
    # llama_model = LlamaModel(model_name="ggml-alpaca-7b-q4.bin", repo_id="chungmin99/ggml-alpaca-7b-q4")
    prompt = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "tell a stupid bengali joke."}]
    # response = llama_model.generate(prompt)
    # print("Response from LlamaModel:", response)

    # Example usage of ChatGroq
    chat_groq = ChatGroqLLM()
    groq_response = chat_groq.generate_response(prompt)
    print("Response from ChatGroq:", groq_response)