from Services.Advisor.advisor import Advisor
import anthropic
from config import Config

class AnthropicAdvisor(Advisor):
    def __init__(self):
        super().__init__()
        self.api_key = Config.anthropic_api_key()
        self.model = 'claude-sonnet-4-0'
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_message(self, system_prompt, user_prompt):
        return [
            {"role": "user", "content": user_prompt}
        ]

    def generate_advice(self, company_data):
        response = self.client.messages.create(
            model=self.model,
            system=self.generate_system_prompt(),
            messages=self.generate_message(None, self.generate_user_prompt(company_data)),
            max_tokens=1000
        )

        return response.content[0].text