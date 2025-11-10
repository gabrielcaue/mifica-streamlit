import streamlit as st
from PIL import Image
import json
from components.user_card import exibir_user_card
from utils.charts import grafico_reputacao
from services.blockchain_api import listar_transacoes  # ✅ NOVO: Importa função da API

st.set_page_config(
    page_title="Mifica Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar dados dos usuários
from utils.data import carregar_usuarios
usuarios = carregar_usuarios()

nomes_usuarios = [u["nome"] for u in usuarios]
usuario_selecionado = st.sidebar.selectbox("Selecionar usuário:", nomes_usuarios)

# Sidebar
st.sidebar.title("🔍 Navegação")
opcao = st.sidebar.radio("Ir para:", ["Dashboard", "Perfil", "Configurações"])

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

    fig = grafico_reputacao(usuarios)
    st.plotly_chart(fig, use_container_width=True)

    # ✅ NOVO BLOCO: Transações Blockchain
    st.markdown("### 🔗 Transações Blockchain")
    transacoes = listar_transacoes()

    if transacoes:
        for tx in transacoes:
            st.write(f"• {tx['remetente']} → {tx['destinatario']} | R$ {tx['valor']} | {tx['dataTransacao']}")
    else:
        st.info("Nenhuma transação registrada ainda.")

elif opcao == "Perfil":
    st.subheader(f"👤 Perfil de {usuario_selecionado}")
    st.write("Aqui você pode exibir mais detalhes do perfil futuramente.")

elif opcao == "Configurações":
    st.subheader("⚙️ Configurações")
    st.write("Ajustes e preferências do sistema.")
