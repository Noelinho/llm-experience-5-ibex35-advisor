import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockCompaniesInformationManager:
    IBEX35_COMPANIES = {
        "Acciona": "ANA.MC",
        "Acerinox": "ACX.MC",
        "ACS": "ACS.MC",
        "Aena": "AENA.MC",
        "Almirall": "ALM.MC",
        "Amadeus": "AMS.MC",
        "ArcelorMittal": "MT.MC",
        "Banco Sabadell": "SAB.MC",
        "Banco Santander": "SAN.MC",
        "BBVA": "BBVA.MC",
        "CaixaBank": "CABK.MC",
        "Cellnex": "CLNX.MC",
        "Endesa": "ELE.MC",
        "Ferrovial": "FER.MC",
        "Fluidra": "FDR.MC",
        "Grifols": "GRF.MC",
        "IAG": "IAG.MC",
        "Iberdrola": "IBE.MC",
        "Inditex": "ITX.MC",
        "Indra": "IDR.MC",
        "Inmobiliaria Colonial": "COL.MC",
        "Logista": "LOG.MC",
        "Mapfre": "MAP.MC",
        "Meliá Hotels": "MEL.MC",
        "Merlin Properties": "MRL.MC",
        "Naturgy": "NTGY.MC",
        "PharmaMar": "PHM.MC",
        "Red Eléctrica": "REE.MC",
        "Repsol": "REP.MC",
        "Rovi": "ROVI.MC",
        "Sacyr": "SCYR.MC",
        "Solaria": "SLR.MC",
        "Telefónica": "TEF.MC",
        "Viscofan": "VIS.MC"
    }

    @staticmethod
    def retrieve_company_list():
        return list(StockCompaniesInformationManager.IBEX35_COMPANIES)

    def get_stock_data(company_name, period="1y"):
        try:
            if company_name not in StockCompaniesInformationManager.IBEX35_COMPANIES:
                return None, None, "Empresa no encontrada en la lista de IBEX35."

            company = StockCompaniesInformationManager.IBEX35_COMPANIES[company_name]
            stock = yf.Ticker(company)

            historical_data = stock.history(period=period)

            data_info = stock.info

            return historical_data, data_info, stock

        except Exception as e:
            return None, None, f"Error obteniendo datos: {str(e)}"
