from Services.Advisor.advisor import Advisor
from config import Config
from huggingface_hub import InferenceClient
from transformers import AutoTokenizer

class MicrosoftAdvisor(Advisor):
    def __init__(self):
        super().__init__()
        self.api_key = Config.huggingface_api_key()
        self.model = 'microsoft/Phi-3-mini-4k-instruct'
        self.url = Config.phi_model_url()

    def generate_message(self, system_prompt, user_prompt):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    def generate_advice(self, company_data):
        tokenizer = AutoTokenizer.from_pretrained(self.model)
        messages = self.generate_message(self.generate_system_prompt(), self.generate_user_prompt(company_data))
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        client = InferenceClient(self.url, token=self.api_key)
        response = client.text_generation(text, details=True, max_new_tokens=3000, return_full_text=False)
        return response.generated_text

