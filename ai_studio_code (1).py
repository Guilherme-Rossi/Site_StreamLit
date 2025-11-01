import streamlit as st

# 1. Configurar a página para usar a largura total e o tema claro
st.set_page_config(
    page_title="Doing Work",
    page_icon="doingworkiconefinal_icone.ico", # Certifique-se que este arquivo existe
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Adicionar os links de navegação à barra lateral
with st.sidebar:
    st.title("Menu - DoingWork")
    st.markdown("---")
    st.markdown("[Funcionalidades](#features)")
    st.markdown("[Para Quem?](#)")
    st.markdown("[Preços](#pricing)")
    st.markdown("[Integrações](#)")
    st.markdown("---")
    st.markdown("**Recursos**")
    st.markdown("- [Blog](#)")
    st.markdown("- [Central de Ajuda](#)")
    st.markdown("- [Contato](#)")
    st.markdown("---")
    st.markdown("[Login](#)") 
    st.link_button("Começar Grátis", "#final-cta")


# 3. Forçar o tema branco e injetar o CSS CORRIGIDO
st.markdown("""
    <style>
        .stApp {
            background-color: white !important;
        }

        /* --- CORREÇÃO DEFINITIVA APLICADA AQUI --- */
        
        /* 1. Em telas grandes (desktop), ESCONDA o botão que abre o menu lateral. */
        @media (min-width: 992px) {
            button[data-testid="stSidebarNavToggler"] {
                display: none !important;
            }
        }

        /* 2. Estiliza o conteúdo da barra lateral para combinar com o site */
        [data-testid="stSidebar"] h1 { /* Título "Menu - DoingWork" */
            font-family: 'Inter', sans-serif;
            color: #0d1b2a; /* Cor --dark-blue */
        }

        [data-testid="stSidebar"] a { /* Todos os links na sidebar */
            font-family: 'Inter', sans-serif;
            color: #1b263b !important; /* Cor --medium-blue */
            font-weight: 600;
            text-decoration: none;
        }

        [data-testid="stSidebar"] a:hover {
            color: #3a86ff !important;
        }

        [data-testid="stSidebar"] strong { /* Subtítulo "Recursos" */
            font-family: 'Inter', sans-serif;
            color: #0d1b2a;
        }
    </style>
""", unsafe_allow_html=True)

# 4. Armazenar todo o código HTML e CSS (inalterado)
html_string = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DoingWork - Gestão de projetos, sem a complexidade</title>
    <style>
        /* --- Configurações Globais e Fontes --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        :root {
            --dark-blue: #0d1b2a;
            --medium-blue: #1b263b;
            --light-blue: #415a77;
            --text-gray: #778da9;
            --white: #ffffff;
            --primary-gradient: linear-gradient(90deg, #3a86ff 0%, #8338ec 100%);
            --border-radius: 12px;
            --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
            --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif; 
            background-color: var(--white) !important; 
            color: var(--text-gray); 
            line-height: 1.7; 
            -webkit-font-smoothing: antialiased;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .fade-in { animation: fadeIn 0.8s ease-out forwards; }

        header { 
            padding: 1.5rem 0; 
            position: sticky; 
            top: 0; 
            left: 0; 
            width: 100%; 
            z-index: 1000; 
            transition: background-color 0.3s ease, box-shadow 0.3s ease, padding 0.3s ease;
            background-color: rgba(255, 255, 255, 0.95); 
            backdrop-filter: blur(10px); 
            box-shadow: var(--shadow-sm);
        }
        nav { display: flex; justify-content: space-between; align-items: center; }
        .logo { font-size: 1.6rem; font-weight: 700; color: var(--dark-blue); }
        .nav-links { list-style: none; display: flex; align-items: center; gap: 2.5rem; padding-top: 10px; margin-bottom: 8px}
        .nav-links a { text-decoration: none; color: var(--medium-blue) !important; font-weight: 600; transition: color 0.3s; }
        .nav-links a:hover { color: #3a86ff !important; }
        .nav-actions { display: flex; align-items: center; gap: 1.5rem; }
        .login-link { text-decoration: none; color: var(--medium-blue) !important; font-weight: 600; transition: color 0.3s; }
        .login-link:hover { color: #3a86ff !important; }
        
        .dropdown { position: relative; display: inline-block; }
        .dropdown-toggle { cursor: pointer; display: flex; align-items: center; }
        .dropdown-menu { display: none; position: absolute; top: 130%; left: 50%; transform: translateX(-50%); background: var(--white); border-radius: var(--border-radius); box-shadow: var(--shadow-md); list-style: none; padding: 0.5rem; width: 200px; z-index: 1; opacity: 0; visibility: hidden; transition: opacity 0.3s ease; }
        .dropdown:hover .dropdown-menu { display: block; opacity: 1; visibility: visible; }
        .dropdown-menu a { display: block; padding: 0.75rem 1rem; border-radius: 8px; }
        .dropdown-menu a:hover { background-color: #f8f9fa; }
        .arrow { display: inline-block; transition: transform 0.3s ease; margin-left: 4px; }
        .dropdown:hover .arrow { transform: rotate(180deg); }

        .btn { padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; display: inline-block; border: none; font-size: 0.9rem;}
        .btn-gradient { background: var(--primary-gradient); color: var(--white) !important; box-shadow: var(--shadow-sm); }
        .btn:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
        .btn-outline { background: transparent; color: var(--dark-blue) !important; border: 2px solid #e0e1dd; }
        .btn-outline:hover { background: var(--dark-blue); color: var(--white) !important; }

        #hero { padding: 100px 0 120px 0; }
        .hero-content { display: flex; align-items: center; justify-content: space-between; gap: 4rem; }
        .hero-text { max-width: 50%; }
        .hero-text h1 { font-size: 3.8rem; color: var(--dark-blue) !important; line-height: 1.2; margin-bottom: 1.5rem; }
        .hero-text p { font-size: 1.25rem; margin-bottom: 2.5rem; color: var(--light-blue) !important; }
        .hero-mockup { width: 45%; height: 350px; background: #f0f4f9; border-radius: var(--border-radius); box-shadow: var(--shadow-md); padding: 1.5rem; border: 1px solid #e0e1dd; }
        .mockup-header { display: flex; gap: 8px; margin-bottom: 1rem; }
        .mockup-header span { width: 12px; height: 12px; border-radius: 50%; }
        .mockup-content { width: 100%; height: 85%; background: var(--white); border-radius: 8px; }
        .section { padding: 100px 0; }
        .section-light { background-color: #f8f9fa; }
        
        .section-title { text-align: center; font-size: 2.8rem; color: var(--dark-blue) !important; margin-bottom: 1rem; }
        
        .section-subtitle { 
            display: block !important;
            text-align: center !important; 
            font-size: 1.15rem; 
            margin-bottom: 5rem; 
            max-width: 700px; 
            margin-left: auto !important; 
            margin-right: auto !important; 
            color: var(--light-blue) !important; 
        }
        
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
        .feature-card { background: var(--white); padding: 2.5rem 2rem; border-radius: var(--border-radius); text-align: left; box-shadow: var(--shadow-sm); border: 1px solid #e0e1dd; transition: all 0.3s ease; }
        .feature-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
        .feature-card .icon { margin-bottom: 1.5rem; background: var(--primary-gradient); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .feature-card h3 { font-size: 1.3rem; color: var(--dark-blue) !important; margin-bottom: 0.5rem; }
        .feature-card p { color: var(--text-gray) !important; }

        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: stretch; }
        
        .pricing-card { 
            display: flex; 
            flex-direction: column; 
            background: var(--white); 
            border-radius: var(--border-radius); 
            padding: 2.5rem; 
            text-align: center; 
            border: 1px solid #e0e1dd; 
            transition: all 0.3s ease; 
            position: relative; 
            box-shadow: var(--shadow-sm); 
        }

        .pricing-card:hover { transform: translateY(-10px); box-shadow: var(--shadow-md); }
        
        .pricing-card.popular { 
            border: 2px solid #3a86ff;
        }

        .pricing-card h3 { font-size: 1.5rem; color: var(--dark-blue) !important; }
        .pricing-card .price { font-size: 3.5rem; font-weight: 700; color: var(--dark-blue) !important; margin: 1rem 0; }
        .pricing-card .price span { font-size: 1rem; font-weight: 400; color: var(--text-gray) !important; }
        
        .pricing-card ul { 
            list-style: none; 
            margin: 2rem 0; 
            text-align: left; 
            flex-grow: 1;
        }

        .pricing-card ul li { margin-bottom: 1rem; display: flex; align-items: center; color: var(--text-gray) !important; }
        .pricing-card ul li svg { margin-right: 10px; color: #3a86ff; }
        .popular-badge { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--primary-gradient); color: var(--white) !important; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; font-weight: 600; }
        
        #final-cta { background: var(--medium-blue); text-align: center; }
        #final-cta h2 { color: var(--white) !important; }
        #final-cta p { color: #E8E8E8 !important; }
        
        footer { background-color: #f8f9fa; padding: 80px 0 40px 0; }
        .footer-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom: 4rem; }
        .footer-column .logo { margin-bottom: 1rem; }
        .footer-column p { max-width: 250px; margin-bottom: 1.5rem; color: var(--dark-blue) !important; }
        .social-icons a { display: inline-block; margin-right: 1rem; opacity: 0.7; transition: opacity 0.3s; }
        .social-icons a:hover { opacity: 1; }
        .footer-column h4 { font-size: 1rem; color: var(--dark-blue) !important; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 0.5px; }
        .footer-column ul { list-style: none; }
        .footer-column ul li { margin-bottom: 1rem; }
        .footer-column ul li a { text-decoration: none; color: var(--dark-blue) !important; transition: color 0.3s; }
        .footer-column ul li a:hover { color: #3a86ff !important; }
        .footer-bottom { border-top: 1px solid #e0e1dd; padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; font-size: 0.9rem; }
        .footer-bottom p { color: var(--text-gray) !important; }
        .sminex-logo { text-align: right; }
        .sminex-logo p { font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--text-gray) !important; }
        .sminex-logo .sminex-text { font-weight: 700; font-size: 1.2rem; background: var(--primary-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

        @media (max-width: 992px) {
            .nav-links, .nav-actions { display: none; }
            .hero-content { flex-direction: column; text-align: center; }
            .hero-text { max-width: 100%; }
            .hero-mockup { display: none; }
            .footer-grid { grid-template-columns: 1fr 1fr; }
        }
        @media (max-width: 768px) {
            #hero h1 { font-size: 2.8rem; }
            .section-title { font-size: 2.2rem; }
            .footer-grid { grid-template-columns: 1fr; text-align: center; }
            .footer-column p { margin-left: auto; margin-right: auto; }
            .social-icons { text-align: center; }
            .footer-bottom { flex-direction: column; gap: 1rem; }
            .sminex-logo { text-align: center; }
        }
    </style>
</head>
<body>
    <header class="fade-in">
        <nav class="container">
            <div class="logo">DoingWork</div>
            <ul class="nav-links">
                <li><a href="#features">Funcionalidades</a></li>
                <li><a href="#">Para Quem?</a></li>
                <li><a href="#pricing">Preços</a></li>
                <li><a href="#">Integrações</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle">Recursos <span class="arrow">▾</span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Central de Ajuda</a></li>
                        <li><a href="#">Contato</a></li>
                    </ul>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="#" class="login-link">Login</a>
                <a href="#final-cta" class="btn btn-gradient">Começar Grátis</a>
            </div>
        </nav>
    </header>
    <main>
        <section id="hero" class="section fade-in">
            <div class="container hero-content">
                <div class="hero-text">
                    <h1>Gestão de projetos, sem a complexidade.</h1>
                    <p>O DoingWork é a plataforma intuitiva que centraliza suas tarefas, melhora a comunicação e impulsiona a produtividade da sua equipe.</p>
                    <a href="#pricing" class="btn btn-gradient">Comece seu teste de 1 mês</a>
                </div>
                <div class="hero-mockup">
                    <div class="mockup-header">
                        <span style="background:#ff5f56;"></span>
                        <span style="background:#ffbd2e;"></span>
                        <span style="background:#27c93f;"></span>
                    </div>
                    <div class="mockup-content"></div>
                </div>
            </div>
        </section>
        <section id="features" class="section section-light fade-in">
             <div class="container">
                <h2 class="section-title">Tudo o que você precisa em um só lugar</h2>
                <p class="section-subtitle">Ferramentas poderosas e fáceis de usar para levar sua equipe ao próximo nível de organização e eficiência.</p>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
                        <h3>Gestão de Tarefas</h3>
                        <p>Crie, atribua e acompanhe o progresso com status visuais e prazos claros para nunca mais perder uma entrega.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></div>
                        <h3>Comunicação Centralizada</h3>
                        <p>Anexe arquivos, adicione comentários e receba notificações. Mantenha toda a equipe na mesma página, sempre.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></div>
                        <h3>Relatórios e Insights</h3>
                        <p>Acesse dados em tempo real e gere relatórios para analisar o desempenho e tomar decisões mais inteligentes.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg></div>
                        <h3>Mobilidade Total</h3>
                        <p>Gerencie seus projetos de onde estiver com nosso site e aplicativo móvel. Sua equipe conectada a qualquer momento.</p>
                    </div>
                </div>
            </div>
        </section>
        <section id="pricing" class="section fade-in">
            <div class="container">
                <h2 class="section-title">Planos flexíveis para cada equipe</h2>
                <p class="section-subtitle">Comece com um teste gratuito de 1 mês. Sem compromisso. Escolha o plano ideal para você após o período de avaliação.</p>
                <div class="pricing-grid">
                    <div class="pricing-card">
                        <h3>Básico</h3>
                        <div class="price">R$50<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Até 10 usuários</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Gerenciamento de tarefas</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Notificações por e-mail</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Relatórios básicos</li>
                        </ul>
                        <a href="#" class="btn btn-outline">Começar Teste</a>
                    </div>
                    <div class="pricing-card popular">
                        <span class="popular-badge">Mais Popular</span>
                        <h3>Premium</h3>
                        <div class="price">R$150<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Até 50 usuários</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Tudo do plano Básico</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Integrações com ferramentas</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Suporte prioritário</li>
                        </ul>
                        <a href="#" class="btn btn-gradient">Começar Teste</a>
                    </div>
                    <div class="pricing-card">
                        <h3>Enterprise</h3>
                        <div class="price">R$500<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Usuários ilimitados</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Tudo do plano Premium</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Gerente de conta dedicado</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Segurança avançada (SSO)</li>
                        </ul>
                        <a href="#" class="btn btn-outline">Fale Conosco</a>
                    </div>
                </div>
            </div>
        </section>
        <section id="final-cta" class="section fade-in">
            <div class="container" style="display:flex; flex-direction:column; align-items:center;">
                <h2 class="section-title">Pronto para transformar sua gestão?</h2>
                <p class="section-subtitle">Junte-se a milhares de equipes que já organizam seu trabalho com o DoingWork. Comece seu teste gratuito hoje mesmo.</p>
                <a href="#" class="btn btn-gradient">Aumentar minha produtividade</a>
            </div>
        </section>
    </main>
    <footer class="fade-in">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-column">
                    <div class="logo">DoingWork</div>
                    <p>A plataforma intuitiva para gestão de projetos modernos.</p>
                    <div class="social-icons">
                        <a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                        <a href="#"><img src="https://raw.githubusercontent.com/Guilherme-Rossi/Site_StreamLit/main/twitter_sem_fundo.png" alt="Twitter / X" width="20" height="20"></a> 
                    </div>
                </div>
                <div class="footer-column">
                    <h4>Produto</h4>
                    <ul>
                        <li><a href="#features">Funcionalidades</a></li>
                        <li><a href="#pricing">Preços</a></li>
                        <li><a href="#">Integrações</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Empresa</h4>
                    <ul>
                        <li><a href="#">Sobre Nós</a></li>
                        <li><a href="#">Carreiras</a></li>
                        <li><a href="#">Contato</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="#">Termos de Serviço</a></li>
                        <li><a href="#">Política de Privacidade</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 DoingWork. Todos os direitos reservados.</p>
                <div class="sminex-logo">
                    <p>Um produto da</p>
                    <span class="sminex-text">SMINEX ENTERPRISE</span>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
"""

# 5. RENDERIZAR O HTML NO STREAMLIT
st.markdown(html_string, unsafe_allow_html=True)
