from Advisor.advisor import Advisor


class DeactivatedAdvisor(Advisor):
    def __init__(self):
        super().__init__()

    def generate_message(self, system_prompt, user_prompt):
        return []


    def generate_advice(self, company_data):
        return "Este advisor está desactivado"