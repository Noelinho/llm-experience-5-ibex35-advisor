from abc import ABC, abstractmethod
import pandas as pd
from Models.company_data import CompanyData

class Advisor(ABC):
    @abstractmethod
    def generate_advice(self, company_data):
        pass

    def generate_system_prompt(self):
        return """
        Eres un asesor financiero experto. Tu tarea es proporcionar consejos de inversión basados en los datos de la empresa proporcionados. Analiza la información y ofrece recomendaciones claras y concisas.
        Ten en cuenta:
            - Analiza e informa de los datos de todo el periodo de tiempo proporcionado.
            - Analiza a parte los datos de los últimos 3 meses.
            - Proporciona respuestas claras y concisas.
        
        """

    def generate_user_prompt(self, company_data: CompanyData):
        return f"Analiza los siguientes datos de la empresa y proporciona un consejo de inversión. Los dstos que vas a recibir es la cotización al cierre del día.:\n\n{company_data.retrieve_historical_prices()}\n\n" \

    @abstractmethod
    def generate_message(self, system_prompt, user_prompt):
        pass
