🧠 Mifica — Inteligência Modular para Software
Mifica é um sistema modular que integra autenticação via JWT, painéis administrativos com Streamlit, e uma interface frontend moderna. O projeto está em desenvolvimento e tem como objetivo oferecer uma plataforma inteligente para gestão de reputação, contratos e desafios gamificados.

⚠️ Status do projeto: Em construção A estilização visual (especialmente no painel Streamlit) ainda está sendo refinada para garantir uma experiência mais profissional e elegante.

🚀 Tecnologias utilizadas
Frontend: React + TailwindCSS

Backend: FastAPI + JWT

Painel administrativo: Streamlit

Banco de dados: PostgreSQL

Autenticação: JWT com controle de acesso por role

📦 Estrutura do projeto
mifica/
├── frontend/         # Interface do usuário
├── backend/          # API com autenticação e lógica de negócio
├── streamlit/        # Painel administrativo para admins
└── README.md

🧪 Como rodar localmente
1. Backend (FastAPI)
cd backend/
uvicorn main:app --reload

2. Frontend (React)
cd frontend/
npm install
npm run dev

3. Painel administrativo (Streamlit)
cd streamlit/
streamlit run main.py

🔐 Acesso ao painel administrativo
O painel Streamlit é acessível apenas para usuários com perfil de administrador (role: "admin"). Após login no frontend, o botão “🧠 Painel de Inteligência Mifica” estará disponível para admins e redirecionará para o painel em http://localhost:8501.

📌 Próximos passos
[ ] Finalizar estilização do painel Streamlit

[ ] Implementar controle de reputação via blockchain

[ ] Criar deploy com Docker ou GCP

[ ] Adicionar testes automatizados

📫 Contato
Gabriel — Engenheiro de Software 
📧 [gabrielcaue3@gmail.com] 
🔗 linkedin.com/in/gabrielcaues

