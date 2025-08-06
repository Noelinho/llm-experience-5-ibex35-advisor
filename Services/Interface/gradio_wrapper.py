import gradio as gr
from Services.Interface.data_information_helper import DataInformationHelper
from Services.Advisor.advisor_generator import AdvisorGenerator

class GradioWrapper:
    def __init__(self):
        self.historical_data = None
        self.advisor_generator = AdvisorGenerator()
        pass

    def load_company_history(self, company_name: str):
        fig, historical_data = DataInformationHelper.get_data_information(company_name)
        self.historical_data = historical_data

        return fig, gr.Button(value="Solicitar consejo de inversión", interactive=True)

    def generate_advice(self):
        if self.historical_data is None:
            return "No hay datos históricos disponibles. Por favor, carga los datos primero."

        return self.advisor_generator.generate_advice(self.historical_data['Close'])