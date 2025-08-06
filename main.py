import gradio as gr

from Services.Stock.stock_companies_information_manager import StockCompaniesInformationManager
from Services.Interface.gradio_wrapper import GradioWrapper

gradio_wrapper = GradioWrapper()

css = """
.row-container {
    align-items: center !important;  /* Alinea al final (bottom) */
}
.analysis-output {
    max-height: 400px;
    overflow-y: auto;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
}
"""

with gr.Blocks(css=css) as application:
    gr.Markdown("Ibex35 - Advisor")

    with gr.Row(elem_classes=["row-container"]):
        companies = gr.Dropdown(
            label="Selecciona un valor",
            choices=StockCompaniesInformationManager.retrieve_company_list(),
            filterable=True,
            interactive=True,
            scale=3
        )
        get_price_history_button = gr.Button(value="Mostrar histórico de precios", scale=1, size="lg")

    with gr.Row():
        chart_data = gr.Plot(label="Gráfico de precios")

    with gr.Row():
        ask_for_advice_button = gr.Button(value="Solicitar consejo de inversión", interactive=False)
    with gr.Row():
        with gr.Group():
            gr.Markdown("###Chat GPT")
            chatgpt_box = gr.Markdown(
                elem_classes=["analysis-output"],
                height=200
            )

        with gr.Group():
            gr.Markdown("###Claude")
            claude_box = gr.Markdown(
                elem_classes=["analysis-output"],
                height=200
            )

        with gr.Group():
            gr.Markdown("###Microsoft")
            microsoft_box = gr.Markdown(
                elem_classes=["analysis-output"],
                height=200
            )

    get_price_history_button.click(gradio_wrapper.load_company_history, inputs=companies, outputs=[chart_data, ask_for_advice_button])
    ask_for_advice_button.click(gradio_wrapper.generate_advice, outputs=[chatgpt_box, claude_box, microsoft_box])

application.launch()