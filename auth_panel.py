import streamlit as st
import requests
import jwt

def render():
    # Estilo visual
    st.markdown(
        """
        <style>
        .login-box {
            background-color: #1C1F26;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
            max-width: 400px;
            margin: auto;
            color: #FAFAFA;
        }
        div[data-testid="stTextInput"] > div > input {
            background-color: #2A2D35 !important;
            color: #FAFAFA !important;
            border-radius: 8px !important;
            padding: 10px !important;
            border: none !important;
        }
        button[kind="primary"] {
            background-color: #00C896 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: bold !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Caixa de login
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("### 🔐 Painel de Autenticação")

    # Campos funcionais
    email = st.text_input("Email", placeholder="Digite seu email")
    senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

    if st.button("Entrar"):
        with st.spinner("Autenticando..."):
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

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render()
