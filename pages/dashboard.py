import streamlit as st
from PIL import Image
import plotly.express as px

from components.user_card import exibir_user_card
from utils.charts import grafico_reputacao
from utils.data import carregar_usuarios

def render():
    st.set_page_config(page_title="Mifica Dashboard", page_icon="🧠", layout="wide")

    # Sidebar
    st.sidebar.title("🔍 Navegação")
    opcao = st.sidebar.radio("Ir para:", ["Dashboard", "Perfil", "Configurações"])

    # Carregar dados dos usuários com feedback visual
    with st.spinner("Carregando dados dos usuários..."):
        usuarios = carregar_usuarios()
        nomes_usuarios = [u["nome"] for u in usuarios]
        usuario_selecionado = st.sidebar.selectbox("Selecionar usuário:", nomes_usuarios)

    st.toast("Dados carregados com sucesso!", icon="📊")

    # Logo e título
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120)
    st.markdown("## Mifica — Inteligência Modular para Software")
    st.markdown("---")

    # Dados do usuário selecionado
    usuario_dados = next((u for u in usuarios if u["nome"] == usuario_selecionado), None)

    # Conteúdo condicional
    if opcao == "Dashboard":
        st.subheader(f"📊 Dashboard de {usuario_selecionado}")

        if usuario_dados:
            exibir_user_card(usuario_dados)

        with st.spinner("Gerando gráfico de reputação..."):
            fig = grafico_reputacao(usuarios)
            st.plotly_chart(fig, use_container_width=True)

    elif opcao == "Perfil":
        st.subheader(f"👤 Perfil de {usuario_selecionado}")
        st.write("Aqui você pode exibir mais detalhes do perfil futuramente.")

    elif opcao == "Configurações":
        st.subheader("⚙️ Configurações")
        st.write("Ajustes e preferências do sistema.")

if __name__ == "__main__":
    render()
