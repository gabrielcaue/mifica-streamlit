import streamlit as st
import requests
import jwt
import os

def render():
    # Estilo visual aplicado diretamente aos componentes
    st.markdown(
        """
        <style>
        .main {
            background-color: #0E1117;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #00C896;
            text-align: center;
        }
        div[data-testid="stTextInput"] > div > input {
            background-color: #2A2D35 !important;
            color: #FAFAFA !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: none !important;
            font-size: 0.95rem !important;
        }
        button[kind="primary"] {
            background-color: #00C896 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            padding: 0.6rem 1.2rem !important;
            margin-top: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Logotipo e frase de impacto
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
    else:
        st.warning("⚠️ Logo não encontrada em 'assets/logo.png'")

    st.markdown("## Mifica — Inteligência Modular para Software")
    st.markdown("### 🔐 Painel de Autenticação JWT")

    # Inicializa o estado da sessão
    if "token" not in st.session_state:
        st.session_state["token"] = None
    if "usuario" not in st.session_state:
        st.session_state["usuario"] = None

    # Campos de entrada
    email = st.text_input("Email", placeholder="Digite seu email")
    senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

    # Botão de login
    if st.button("Entrar"):
        with st.spinner("Autenticando..."):
            try:
                r = requests.post("http://localhost:8080/api/auth/login", json={"email": email, "senha": senha})
                if r.status_code == 200:
                    token = r.json()["token"]
                    st.session_state["token"] = token

                    decoded = jwt.decode(token, options={"verify_signature": False})
                    st.session_state["usuario"] = {
                        "nome": decoded.get("nome", "Usuário"),
                        "email": decoded.get("email", decoded.get("sub", "")),
                        "role": decoded.get("role", "")
                    }

                    st.toast("Login realizado com sucesso!", icon="✅")
                    st.success("Login realizado com sucesso!")
                    st.text_area("Token JWT", token[:10] + "...", height=100)
                    st.markdown(f"👤 **Usuário:** {st.session_state['usuario']['nome']}")
                    st.markdown(f"📧 **Email:** {st.session_state['usuario']['email']}")
                else:
                    st.error("Credenciais inválidas ou erro no servidor.")
            except Exception as e:
                st.error(f"Erro ao conectar com o backend: {e}")

if __name__ == "__main__":
    render()
