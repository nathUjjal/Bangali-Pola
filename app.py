from huggingface_hub import hf_hub_download
from llama_cpp import Llama

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

    def generate(self, prompt: str, max_tokens: int = 256 , tempareture : float = 0.7 ) -> str:
        response = self.model.create_chat_completion(messages=prompt, max_tokens=max_tokens , temperature=tempareture)
        return response["choices"][0]["message"]["content"]