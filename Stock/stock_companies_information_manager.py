import yfinance as yf
from typing import Optional, List
from Models.company_data import CompanyData
import pandas as pd

class DataRetrievalException(Exception):
    pass

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
    def retrieve_company_list() -> List[str]:
        return list(StockCompaniesInformationManager.IBEX35_COMPANIES)

    @staticmethod
    def retrieve_company_data(company_name: str, period: str = "1y") -> CompanyData:
        try:
            if company_name not in StockCompaniesInformationManager.IBEX35_COMPANIES:
                raise DataRetrievalException(f"Empresa '{company_name}' no encontrada en IBEX35")

            ticker_symbol = StockCompaniesInformationManager.IBEX35_COMPANIES[company_name]
            stock = yf.Ticker(ticker_symbol)
            historical_data = stock.history(period=period)

            if historical_data.empty:
                raise DataRetrievalException(f"No se pudieron obtener datos históricos para {company_name}")

            return CompanyData(
                name=company_name,
                symbol=ticker_symbol,
                historical_prices=historical_data['Close'],
                period=period
            )


        except DataRetrievalException:

            raise
        except Exception as e:
            raise DataRetrievalException(f"Error obteniendo datos para {company_name}: {str(e)}")