from Services.Advisor.advisor import Advisor
from openai import OpenAI
from config import Config

class OpenAIAdvisor(Advisor):
    def __init__(self):
        super().__init__()
        self.api_key = Config.open_ai_api_key()
        self.client = OpenAI(api_key=self.api_key)
        self.model = 'gpt-4o-mini'

    def generate_message(self, system_prompt, user_prompt):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]


    def generate_advice(self, company_data):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.generate_message(self.generate_system_prompt(), self.generate_user_prompt(company_data))
        )

        return response.choices[0].message.content