from Advisor.openai_advisor import OpenAIAdvisor
from Advisor.anthropic_advisor import AnthropicAdvisor
from Advisor.microsoft_advisor import MicrosoftAdvisor
from Advisor.deactivated_advisor import DeactivatedAdvisor
from config import Config

class AdvisorGenerator:
    def __init__(self):
        pass

    @staticmethod
    def create_advisor(advisor_type, is_enabled):
        if not is_enabled:
            return DeactivatedAdvisor()

        if advisor_type == "openai":
            return OpenAIAdvisor()
        elif advisor_type == "anthropic":
            return AnthropicAdvisor()
        elif advisor_type == "microsoft":
            return MicrosoftAdvisor()
        else:
            raise ValueError(f"Unknown advisor type: {advisor_type}")

    def get_active_advisors(self):
        return [AdvisorGenerator.create_advisor(config["type"], config["enabled"]) for config in Config.advisors_config()]

    def generate_advice(self, company_data):
        advices = []
        for advisor in self.get_active_advisors():
            advices.append(advisor.generate_advice(company_data))

        return advices