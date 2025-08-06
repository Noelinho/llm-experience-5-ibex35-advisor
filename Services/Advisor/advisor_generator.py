from Services.Advisor.openai_advisor import OpenAIAdvisor
from Services.Advisor.anthropic_advisor import AnthropicAdvisor
from Services.Advisor.microsoft_advisor import MicrosoftAdvisor

class AdvisorGenerator:
    def __init__(self):
        self.openai_advisor = OpenAIAdvisor()
        self.antropic_advisor = AnthropicAdvisor()
        self.microsoft_advisor = MicrosoftAdvisor()
        pass

    def generate_advice(self, company_data):
        openai_advising = self.openai_advisor.generate_advice(company_data)
        anthropic_advising = self.antropic_advisor.generate_advice(company_data)
        microsoft_advising = self.microsoft_advisor.generate_advice(company_data)

        return [openai_advising, anthropic_advising, microsoft_advising]