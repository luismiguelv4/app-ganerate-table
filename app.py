import streamlit as st
import pandas as pd


# Função para gerar o HTML específico
def generate_html():
    if 'df' in st.session_state and not st.session_state.df.empty:
        df = st.session_state.df
        html_content = '<div id="progressive-discounts-form">\n'
        if not df.empty:
            first_row = df.iloc[0]
            html_content += f'    <input id="progressive-discounts-min" type="hidden" value="{first_row["quantidade"]}" /> \n'
            html_content += f'    <input id="progressive-discounts-percentage" type="hidden" value="{first_row["desconto (%)"]}" />\n'
        html_content += '</div>\n'

        html_content += '<div id="progressive-discounts-table">\n'
        for index, row in df.iterrows():
            html_content += f'    <div id="line-table">\n'
            html_content += f'        <input id="value-min-qt" type="hidden" value="{row["quantidade"]}" /> \n'
            html_content += f'        <input id="value-min-percent" type="hidden" value="{row["desconto (%)"]}" />\n'
            html_content += f'    </div>\n'
        html_content += '</div>'

        # Exibir o HTML na tela
        st.code(html_content, language='html')
    else:
        st.write("A tabela está vazia.")


# Inicializar a tabela se não existir
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame({'quantidade': [0], 'desconto (%)': [0.00]})

# Interface do usuário
st.title("Tabela de Descontos")

# Exibir a tabela
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic", hide_index=True, key="data_editor")

# Atualizar o DataFrame no estado da sessão com os dados editados
st.session_state.df = edited_df

# Botão para gerar HTML
if st.button("Gerar HTML"):
    generate_html()