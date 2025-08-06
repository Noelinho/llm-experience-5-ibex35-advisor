import gradio as gr
from Interface.data_information_helper import DataInformationHelper
from Advisor.advisor_generator import AdvisorGenerator
from Models.company_data import CompanyData

class GradioWrapper:
    def __init__(self):
        self.company_data: CompanyData = None
        self.advisor_generator = AdvisorGenerator()
        pass

    def load_company_history(self, company_name: str):
        fig, company_data = DataInformationHelper.get_data_information(company_name)
        self.company_data = company_data

        return fig, gr.Button(value="Solicitar consejo de inversión", interactive=True)

    def generate_advice(self):
        if self.company_data.historical_prices is None:
            return "No hay datos históricos disponibles. Por favor, carga los datos primero."

        return self.advisor_generator.generate_advice(self.company_data)