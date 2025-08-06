import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from Stock.stock_companies_information_manager import StockCompaniesInformationManager

class DataInformationHelper:

    @staticmethod
    def get_data_information(company_name):
        company_data = StockCompaniesInformationManager.retrieve_company_data(company_name, period="3y")

        if company_data.historical_prices is None:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, f'Error', ha='center', va='center',transform=ax.transAxes, fontsize=12)
            ax.set_title("Error al cargar los datos")
            return fig

        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(12, 6))

        # Gráfico de línea del precio de cierre
        ax.plot(company_data.historical_prices.index, company_data.historical_prices, linewidth=2, color="#1f77b4", label='Precio de Cierre')
        ax.fill_between(company_data.historical_prices.index, company_data.historical_prices, alpha=0.3, color="#1f77b4")

        # Configurar el gráfico
        ax.set_title(f"Evolución del precio de {company_name} ({company_data.symbol})", fontsize=14, fontweight='bold')
        ax.set_xlabel("Fecha", fontsize=12)
        ax.set_ylabel("Precio (€)", fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()

        # Mejorar formato de fechas en el eje X
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
        plt.xticks(rotation=45)

        plt.tight_layout()

        return fig, company_data