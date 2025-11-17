import streamlit as st
import streamlit.components.v1 as components

# 1. Configurar a página para usar a largura total
st.set_page_config(
    page_title="Doing Work",
    page_icon="doingworkiconefinal_icone.ico",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Adicionar os links de navegação à barra lateral
with st.sidebar:
    st.title("Menu - DoingWork")
    st.markdown("---")
    st.markdown("[Funcionalidades](#features)")
    st.markdown("[Para Quem?](#for-who)")
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

# 3. Forçar o tema branco e injetar o CSS para a barra lateral
st.markdown("""
    <style>
        /* CSS para o app Streamlit em si */
        .stApp { background-color: white !important; }
        iframe { margin: 0; padding: 0; border: none; } /* Remove qualquer borda do iframe */

        @media (min-width: 992px) {
            [data-testid="stSidebar"] { display: none !important; }
            button[data-testid="stSidebarNavToggler"] { display: none !important; }
        }
        [data-testid="stSidebar"] { background-color: #f8f9fa !important; }
        [data-testid="stSidebar"] h1 { font-family: 'Inter', sans-serif; color: #0d1b2a; }
        [data-testid="stSidebar"] a:not([data-testid="stLinkButton"] a) { font-family: 'Inter', sans-serif; color: #1b263b !important; font-weight: 600; text-decoration: none !important; }
        [data-testid="stSidebar"] a:hover:not([data-testid="stLinkButton"] a) { color: #3a86ff !important; }
        [data-testid="stSidebar"] strong { font-family: 'Inter', sans-serif; color: #0d1b2a; }
        [data-testid="stSidebar"] [data-testid="stLinkButton"] a { background: linear-gradient(90deg, #3a86ff 0%, #8338ec 100%) !important; color: white !important; padding: 12px 28px !important; border-radius: 8px !important; font-weight: 600 !important; text-align: center; display: block; transition: all 0.3s ease; }
        [data-testid="stSidebar"] [data-testid="stLinkButton"] a:hover { transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); color: white !important; }
    </style>
""", unsafe_allow_html=True)


# 4. String ÚNICA contendo todo o site (HTML, CSS e AMBOS os Scripts)
full_html_code = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DoingWork</title>
    
    <!-- SCRIPT NOVO E ESSENCIAL: Comunicação com o Streamlit -->
    <script src="https://cdn.jsdelivr.net/gh/streamlit/streamlit@develop/frontend/public/streamlit-component-lib.js"></script>

    <style>
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
        body { margin: 0; font-family: 'Inter', sans-serif; background-color: var(--white) !important; color: var(--text-gray); line-height: 1.7; -webkit-font-smoothing: antialiased; }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        .container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        header { padding: 1.5rem 0; border-bottom: 1px solid #e0e1dd; }
        nav.container { display: grid; grid-template-columns: 1fr auto 1fr; align-items: baseline; }
        .logo { justify-self: start; }
        .nav-links { justify-self: center; }
        .nav-actions { justify-self: end; }
        .logo { font-size: 1.6rem; font-weight: 700; color: var(--dark-blue); }
        .nav-links { list-style: none; display: flex; align-items: center; gap: 2.5rem; }
        .nav-links a { text-decoration: none; color: var(--medium-blue) !important; font-weight: 600; transition: all 0.3s ease; }
        .nav-links a:hover { color: #3a86ff !important; transform: translateY(-2px); }
        .nav-actions { display: flex; align-items: center; gap: 1.5rem; }
        .login-link { text-decoration: none; color: var(--medium-blue) !important; font-weight: 600; transition: all 0.3s ease; }
        .login-link:hover { color: #3a86ff !important; transform: translateY(-2px); }
        .dropdown { position: relative; display: inline-block; }
        .dropdown-toggle { cursor: pointer; display: flex; align-items: center; }
        .dropdown-menu { display: none; position: absolute; top: 130%; left: 50%; transform: translateX(-50%); background: var(--white); border-radius: var(--border-radius); box-shadow: var(--shadow-md); list-style: none; padding: 0.5rem; width: 200px; z-index: 10; opacity: 0; visibility: hidden; transition: opacity 0.3s ease; }
        .dropdown:hover .dropdown-menu { display: block; opacity: 1; visibility: visible; }
        .dropdown-menu a { display: block; padding: 0.75rem 1rem; border-radius: 8px; }
        .dropdown-menu a:hover { background-color: #f8f9fa; }
        .arrow { display: inline-block; transition: transform 0.3s ease; margin-left: 4px; }
        .dropdown:hover .arrow { transform: rotate(180deg); }
        .btn { padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; display: inline-block; border: none; font-size: 0.9rem;}
        .btn-gradient { background: var(--primary-gradient); color: var(--white) !important; box-shadow: var(--shadow-sm); }
        .btn:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
        #hero { padding: 100px 0 120px 0; opacity: 0; animation: fadeInUp 1.2s ease-out forwards; }
        .hero-content { display: flex; align-items: center; justify-content: space-between; gap: 4rem; }
        .hero-text { max-width: 50%; }
        .hero-text h1 { font-size: 3.8rem; color: var(--dark-blue) !important; line-height: 1.2; margin-bottom: 1.5rem; }
        .hero-text p { font-size: 1.25rem; margin-bottom: 2.5rem; color: var(--light-blue) !important; }
        .hero-mockup { width: 45%; height: 350px; background: #f0f4f9; border-radius: var(--border-radius); box-shadow: var(--shadow-md); padding: 1.5rem; border: 1px solid #e0e1dd; }
        .mockup-header { display: flex; gap: 8px; margin-bottom: 1rem; }
        .mockup-header span { width: 12px; height: 12px; border-radius: 50%; }
        .mockup-content { width: 100%; height: 85%; background: var(--white); border-radius: 8px; position: relative; overflow: hidden; padding: 1rem; }
        .mockup-task { background: #f8f9fa; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem; box-shadow: var(--shadow-sm); opacity: 0; animation: fadeInUp 1.0s ease-out forwards; }
        #hero .mockup-task.task1 { animation-delay: 1.0s; }
        #hero .mockup-task.task2 { animation-delay: 1.3s; }
        #hero .mockup-task.task3 { animation-delay: 1.6s; }
        .section { padding: 100px 0; }
        .section-light { background-color: #f8f9fa; }
        .section-title { text-align: center; font-size: 2.8rem; color: var(--dark-blue) !important; margin-bottom: 1rem; }
        .section-subtitle { display: block !important; text-align: center !important; font-size: 1.15rem; margin-bottom: 5rem; max-width: 700px; margin-left: auto !important; margin-right: auto !important; color: var(--light-blue) !important; }
        .features-interactive-wrapper { display: grid; grid-template-rows: auto 1fr; gap: 4rem; }
        .feature-showcase { width: 100%; max-width: 900px; height: 500px; margin: 0 auto; background: #fff; border-radius: var(--border-radius); box-shadow: var(--shadow-md); border: 1px solid #e0e1dd; display: flex; justify-content: center; align-items: center; padding: 25px; transition: background-color 0.3s ease; }
        .showcase-content { display: none; width: 100%; height: 100%; animation: fadeInUp 0.5s ease-out forwards; }
        #showcase-default { display: flex; }
        .features-interactive-wrapper:has(#card-1:hover) #showcase-default, .features-interactive-wrapper:has(#card-2:hover) #showcase-default, .features-interactive-wrapper:has(#card-3:hover) #showcase-default, .features-interactive-wrapper:has(#card-4:hover) #showcase-default { display: none; }
        .features-interactive-wrapper:has(#card-2:hover) #showcase-2 { display: block; }
        .features-interactive-wrapper:has(#card-3:hover) #showcase-3 { display: grid; }
        .features-interactive-wrapper:has(#card-4:hover) #showcase-4 { display: flex; justify-content: center; align-items: center; }
        #showcase-1.showcase-content { padding: 0; display: none; flex-direction: column; width: 100%; }
        .features-interactive-wrapper:has(#card-1:hover) #showcase-1 { display: flex; }
        .features-interactive-wrapper:has(#card-1:hover) .feature-showcase { background-color: #f8f9fa; }
        .kanban-group + .kanban-group { margin-top: 1.25rem; }
        .kanban-group h3 { font-size: 1rem; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-gray); margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #e0e1dd; }
        .kanban-task { display: flex; align-items: center; justify-content: space-between; background-color: var(--white); padding: 1rem; border-radius: 8px; box-shadow: var(--shadow-sm); gap: 1rem; }
        .kanban-task + .kanban-task { margin-top: 0.5rem; }
        .kanban-task-title { font-weight: 600; color: var(--medium-blue); }
        .kanban-task-details { display: flex; align-items: center; gap: 1rem; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
        .feature-card { background: var(--white); padding: 2.5rem 2rem; border-radius: var(--border-radius); text-align: left; box-shadow: var(--shadow-sm); border: 1px solid #e0e1dd; transition: all 0.3s ease; cursor: pointer; }
        .feature-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-md); }
        .feature-card .icon { margin-bottom: 1.5rem; background: var(--primary-gradient); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .feature-card h3 { font-size: 1.3rem; color: var(--dark-blue) !important; margin-bottom: 0.5rem; }
        .feature-card p { color: var(--text-gray) !important; }
        .showcase-default-content { flex-direction: column; justify-content: center; align-items: center; text-align: center; }
        .showcase-default-content .logo { font-size: 2.5rem; font-weight: 700; color: #0d1b2a; margin-bottom: 10px; }
        .showcase-default-content svg { width: 50px; height: 50px; color: #3a86ff; margin-bottom: 20px; }
        .showcase-default-content .prompt-text { font-size: 1.2rem; font-weight: 600; color: #415a77; }
        .task-tags span { font-size: 0.75rem; font-weight: 600; padding: 4px 8px; border-radius: 12px; }
        .tag-ui { background-color: #e7d8ff; color: #8338ec; }
        .tag-backend { background-color: #dbeaff; color: #3a86ff; }
        .task-avatars { display: flex; }
        .avatar { width: 28px; height: 28px; border-radius: 50%; background: #ced4da; border: 2px solid #fff; margin-left: -8px; }
        .avatar:first-child { margin-left: 0; }
        .chat-container { width: 100%; padding: 25px; background: #f8f9fa; border-radius: 8px; }
        .task-header { padding-bottom: 20px; border-bottom: 1px solid #e9ecef; }
        .task-header h1 { font-size: 1.8rem; color: #0d1b2a; margin: 0 0 10px 0; }
        .attachment { display: inline-flex; align-items: center; background: #fff; padding: 8px 12px; border-radius: 6px; font-size: 0.9rem; font-weight: 500; border: 1px solid #e9ecef; }
        .attachment svg { margin-right: 8px; }
        .comments-section { margin-top: 25px; }
        .comment { display: flex; margin-bottom: 20px; }
        .avatar.comment-avatar { width: 40px; height: 40px; border-radius: 50%; background: #ced4da; margin-right: 15px; flex-shrink: 0; }
        .comment-body { display: flex; flex-direction: column; }
        .comment-author { font-weight: 700; color: #1b263b; margin-bottom: 4px; }
        .comment-text { line-height: 1.6; }
        .comment-input { width: 100%; border: 1px solid #ced4da; border-radius: 8px; padding: 12px; font-family: 'Inter', sans-serif; font-size: 0.9rem; margin-top: 10px; }
        #showcase-3.dashboard-grid { grid-template-columns: 2fr 1fr; grid-template-rows: auto auto; gap: 15px; background-color: #f8f9fa; border-radius: 8px; padding: 15px; }
        #showcase-3 .widget { background: #fff; border: 1px solid #e9ecef; border-radius: 12px; padding: 15px; }
        #showcase-3 .widget-title { font-size: 0.9rem; font-weight: 700; color: #0d1b2a; margin: 0 0 15px 0; text-align: left;}
        #showcase-3 .kpi-widget { grid-column: 1 / 3; display: flex; justify-content: space-around; }
        #showcase-3 .kpi-item { text-align: center; }
        #showcase-3 .kpi-value { font-size: 2rem; font-weight: 700; color: #3a86ff; }
        #showcase-3 .kpi-label { font-size: 0.75rem; color: #778da9; }
        #showcase-3 .chart-widget { grid-column: 1 / 2; }
        #showcase-3 .donut-widget { grid-column: 2 / 3; grid-row: 2 / 4; }
        #showcase-3 .bar-chart { display: flex; justify-content: space-around; align-items: flex-end; height: 120px; border-left: 2px solid #e9ecef; border-bottom: 2px solid #e9ecef; padding: 10px; }
        #showcase-3 .bar { width: 25px; background: linear-gradient(180deg, #3a86ff 0%, #8338ec 100%); border-radius: 4px 4px 0 0; }
        #showcase-3 .donut-chart { width: 120px; height: 120px; border-radius: 50%; background: conic-gradient(#3a86ff 0% 75%, #f8f9fa 75% 100%); margin: 10px auto; display: flex; justify-content: center; align-items: center; }
        #showcase-3 .donut-center { width: 75px; height: 75px; background: #fff; border-radius: 50%; display: flex; justify-content: center; align-items: center; flex-direction: column; }
        #showcase-4 .mobile-mockup { width: 240px; height: 420px; background: #0d1b2a; border-radius: 25px; padding: 10px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .mobile-screen { background: #fff; height: 100%; border-radius: 15px; overflow: hidden; display: flex; flex-direction: column; }
        .mobile-content { padding: 15px; overflow-y: auto; flex-grow: 1; scrollbar-width: none; -ms-overflow-style: none; }
        .mobile-content::-webkit-scrollbar { display: none; }
        .mobile-header { font-size: 1rem; font-weight: 700; color: #0d1b2a; margin-bottom: 15px; }
        .mobile-nav { display: flex; justify-content: space-around; padding: 8px 0; border-top: 1px solid #e9ecef; background: #fff; flex-shrink: 0; }
        .nav-item { display: flex; flex-direction: column; align-items: center; color: #778da9; }
        .nav-item.active { color: #3a86ff; }
        .nav-icon { width: 20px; height: 20px; background-color: currentColor; border-radius: 4px; margin-bottom: 3px; }
        .nav-label { font-size: 0.6rem; font-weight: 600; }
        .team-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        .team-card { background: var(--white); padding: 2.5rem 2rem; border-radius: var(--border-radius); text-align: left; box-shadow: var(--shadow-sm); border: 1px solid #e0e1dd; transition: all 0.3s ease; }
        .team-card:hover { transform: translateY(-8px); box-shadow: var(--shadow-md); }
        .team-card .icon { margin-bottom: 1.5rem; background: var(--primary-gradient); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
        .team-card h3 { font-size: 1.3rem; color: var(--dark-blue) !important; margin-bottom: 0.5rem; }
        .team-card p { color: var(--text-gray) !important; }
        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: stretch; }
        .pricing-card { display: flex; flex-direction: column; background: var(--white); border-radius: var(--border-radius); padding: 2.5rem; text-align: center; border: 1px solid #e0e1dd; transition: all 0.3s ease; position: relative; box-shadow: var(--shadow-sm); }
        .pricing-card:hover { transform: translateY(-10px); box-shadow: var(--shadow-md); }
        .pricing-card.popular { border: 2px solid #3a86ff; }
        .pricing-card h3 { font-size: 1.5rem; color: var(--dark-blue) !important; }
        .pricing-card .price { font-size: 3.5rem; font-weight: 700; color: var(--dark-blue) !important; margin: 1rem 0; }
        .pricing-card .price span { font-size: 1rem; font-weight: 400; color: var(--text-gray) !important; }
        .pricing-card ul { list-style: none; margin: 2rem 0; text-align: left; flex-grow: 1; }
        .pricing-card ul li { margin-bottom: 1rem; display: flex; align-items: center; color: var(--text-gray) !important; }
        .pricing-card ul li svg { margin-right: 10px; color: #3a86ff; }
        .popular-badge { position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--primary-gradient); color: var(--white) !important; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; font-weight: 600; }
        #final-cta { background: var(--medium-blue); text-align: center; }
        #final-cta h2 { color: var(--white) !important; }
        #final-cta p { color: #E8E8EE !important; }
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

        .animate-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease-out, transform 0.8s ease-out;
            transition-delay: var(--delay, 0s);
        }
        .animate-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 992px) { .nav-links, .nav-actions { display: none; } nav.container { display: flex; justify-content: space-between; } .hero-content { flex-direction: column; text-align: center; } .hero-text { max-width: 100%; } .hero-mockup { width: 100%; margin-top: 2rem; } .footer-grid { grid-template-columns: 1fr 1fr; } .feature-showcase { height: 350px; } }
        @media (max-width: 768px) { #hero h1 { font-size: 2.8rem; } .section-title { font-size: 2.2rem; } .footer-grid { grid-template-columns: 1fr; text-align: center; } .footer-column p { margin-left: auto; margin-right: auto; } .social-icons { text-align: center; } .footer-bottom { flex-direction: column; gap: 1rem; } .sminex-logo { text-align: center; } .feature-showcase { height: auto; padding: 15px; } #showcase-1 { flex-direction: column; } }
    </style>
</head>
<body>
    <header>
        <!-- Conteúdo do seu Header -->
        <nav class="container">
            <div class="logo">DoingWork</div>
            <ul class="nav-links">
                <li><a href="#features">Funcionalidades</a></li>
                <li><a href="#for-who">Para Quem?</a></li>
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
        <!-- Todo o conteúdo do seu Main -->
        <section id="hero">
            <div class="container hero-content">
                <div class="hero-text">
                    <h1>Gestão de projetos, sem a complexidade.</h1>
                    <p>O DoingWork é a plataforma intuitiva que centraliza suas tarefas, melhora a comunicação e impulsiona a produtividade da sua equipe.</p>
                    <a href="#pricing" class="btn btn-gradient">Comece seu teste de 1 mês</a>
                </div>
                <div class="hero-mockup"><div class="mockup-header"><span style="background:#ff5f56;"></span><span style="background:#ffbd2e;"></span><span style="background:#27c93f;"></span></div><div class="mockup-content"><div class="mockup-task task1"></div><div class="mockup-task task2 done"></div><div class="mockup-task task3"></div></div></div>
            </div>
        </section>
        <section id="features" class="section section-light">
             <div class="container">
                <h2 class="section-title animate-on-scroll">Tudo o que você precisa em um só lugar</h2>
                <p class="section-subtitle animate-on-scroll" style="--delay: 0.2s;">Ferramentas poderosas e fáceis de usar para levar sua equipe ao próximo nível de organização e eficiência.</p>
                <div class="features-interactive-wrapper">
                    <div class="feature-showcase animate-on-scroll" style="--delay: 0.3s;">
                        <div id="showcase-default" class="showcase-content showcase-default-content"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 11.09V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h11"/><path d="m22 12-7 7-4-4-3 3"/></svg><h1 class="logo">DoingWork</h1><p class="prompt-text">Selecione um card abaixo para ver a funcionalidade.</p></div>
                        <div id="showcase-1" class="showcase-content">
                            <div class="kanban-group">
                                <h3>A Fazer</h3>
                                <div class="kanban-task"><span class="kanban-task-title">Desenhar a nova tela de login</span><div class="kanban-task-details"><div class="task-tags"><span class="tag-ui">UI Design</span></div><div class="task-avatars"><div class="avatar"></div></div></div></div>
                                <div class="kanban-task"><span class="kanban-task-title">Criar endpoint da API de usuários</span><div class="kanban-task-details"><div class="task-tags"><span class="tag-backend">Backend</span></div><div class="task-avatars"><div class="avatar"></div><div class="avatar"></div></div></div></div>
                            </div>
                            <div class="kanban-group">
                                <h3>Em Andamento</h3>
                                <div class="kanban-task"><span class="kanban-task-title">Implementar a interface do dashboard</span><div class="kanban-task-details"><div class="task-tags"><span class="tag-ui">UI Design</span></div><div class="task-avatars"><div class="avatar"></div></div></div></div>
                            </div>
                            <div class="kanban-group">
                                <h3>Concluído</h3>
                                <div class="kanban-task"><span class="kanban-task-title">Definir arquitetura do banco de dados</span><div class="kanban-task-details"><div class="task-tags"><span class="tag-backend">Backend</span></div></div></div>
                            </div>
                        </div>
                        <div id="showcase-2" class="showcase-content chat-container"><div class="task-header"><h1>Revisar proposta de novo cliente</h1><div class="attachment"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path></svg><span>proposta_final.pdf</span></div></div><div class="comments-section"><div class="comment"><div class="avatar comment-avatar"></div><div class="comment-body"><span class="comment-author">Ana</span><p class="comment-text">Pessoal, adicionei o anexo com a versão final. Por favor, revisem o mais rápido possível.</p></div></div><div class="comment"><div class="avatar comment-avatar" style="background-color: #adb5bd;"></div><div class="comment-body"><span class="comment-author">Bruno</span><p class="comment-text">Perfeito, Ana! Dei uma olhada e fiz um pequeno ajuste na cláusula 3. Fora isso, está ótimo.</p></div></div><input type="text" class="comment-input" placeholder="Escreva um comentário..."></div></div>
                        <div id="showcase-3" class="showcase-content dashboard-grid"><div class="widget kpi-widget"><div class="kpi-item"><div class="kpi-value">142</div><div class="kpi-label">Tarefas Concluídas</div></div><div class="kpi-item"><div class="kpi-value">23</div><div class="kpi-label">Em Andamento</div></div><div class="kpi-item"><div class="kpi-value">8</div><div class="kpi-label">Atrasadas</div></div></div><div class="widget chart-widget"><h2 class="widget-title">Tarefas por Status</h2><div class="bar-chart"><div class="bar" style="height: 60%;"></div><div class="bar" style="height: 90%;"></div><div class="bar" style="height: 40%;"></div><div class="bar" style="height: 75%;"></div></div></div><div class="widget donut-widget"><h2 class="widget-title">Progresso do Projeto</h2><div class="donut-chart"><div class="donut-center"><div class="kpi-value" style="font-size: 1.5rem;">75%</div><div class="kpi-label">Concluído</div></div></div></div></div>
                        <div id="showcase-4" class="showcase-content"><div class="mobile-mockup"><div class="mobile-screen"><div class="mobile-content"><h1 class="mobile-header">Projeto Alpha</h1><div class="task-card"><p class="task-title">Desenhar a nova tela de login</p><div class="task-tags"><span class="tag-ui">UI Design</span></div></div><div class="task-card"><p class="task-title">Implementar a interface do dashboard</p><div class="task-tags"><span class="tag-ui">UI Design</span></div></div><div class="task-card"><p class="task-title">Corrigir bug na autenticação</p></div><div class="task-card"><p class="task-title">Definir arquitetura do banco de dados</p><div class="task-tags"><span class="tag-backend">Backend</span></div></div><div class="task-card"><p class="task-title">Reunião de alinhamento com stakeholders</p></div></div><div class="mobile-nav"><div class="nav-item"><div class="nav-icon" style="border-radius: 50%;"></div><span class="nav-label">Início</span></div><div class="nav-item active"><div class="nav-icon"></div><span class="nav-label">Tarefas</span></div><div class="nav-item"><div class="nav-icon"></div><span class="nav-label">Perfil</span></div></div></div></div></div>
                    </div>
                    <div class="features-grid">
                        <div id="card-1" class="feature-card animate-on-scroll" style="--delay: 0.4s;"><div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div><h3>Gestão de Tarefas</h3><p>Crie, atribua e acompanhe o progresso com status visuais e prazos claros para nunca mais perder uma entrega.</p></div>
                        <div id="card-2" class="feature-card animate-on-scroll" style="--delay: 0.5s;"><div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg></div><h3>Comunicação Centralizada</h3><p>Anexe arquivos, adicione comentários e receba notificações. Mantenha toda a equipe na mesma página, sempre.</p></div>
                        <div id="card-3" class="feature-card animate-on-scroll" style="--delay: 0.6s;"><div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></div><h3>Relatórios e Insights</h3><p>Acesse dados em tempo real e gere relatórios para analisar o desempenho e tomar decisões mais inteligentes.</p></div>
                        <div id="card-4" class="feature-card animate-on-scroll" style="--delay: 0.7s;"><div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg></div><h3>Mobilidade Total</h3><p>Gerencie seus projetos de onde estiver com nosso site e aplicativo móvel. Sua equipe conectada a qualquer momento.</p></div>
                    </div>
                </div>
            </div>
        </section>
        <section id="for-who" class="section section-light">
            <div class="container">
                <h2 class="section-title animate-on-scroll">Perfeito para equipes como a sua</h2>
                <p class="section-subtitle animate-on-scroll" style="--delay: 0.2s;">Seja qual for o seu setor, o DoingWork se adapta ao seu fluxo de trabalho para otimizar processos e maximizar resultados.</p>
                <div class="team-grid">
                    <div class="team-card animate-on-scroll" style="--delay: 0.3s;">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg></div>
                        <h3>Marketing</h3>
                        <p>Planeje campanhas, gerencie calendários de conteúdo e colabore em criativos, tudo em um só lugar para manter os prazos em dia.</p>
                    </div>
                    <div class="team-card animate-on-scroll" style="--delay: 0.4s;">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg></div>
                        <h3>Engenharia</h3>
                        <p>Organize sprints, rastreie bugs e gerencie o roadmap do produto com quadros Kanban flexíveis e integrações com o GitHub.</p>
                    </div>
                    <div class="team-card animate-on-scroll" style="--delay: 0.5s;">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"></path><path d="M12 12v9"></path><path d="M8 17l4 4 4-4"></path></svg></div>
                        <h3>Startups</h3>
                        <p>Mova-se rápido e de forma organizada. Centralize ideias, tarefas e comunicação para escalar seu negócio com agilidade e foco.</p>
                    </div>
                </div>
            </div>
        </section>
        <section id="pricing" class="section">
            <div class="container">
                <h2 class="section-title animate-on-scroll">Planos flexíveis para cada equipe</h2>
                <p class="section-subtitle animate-on-scroll" style="--delay: 0.2s;">Comece com um teste gratuito de 1 mês. Sem compromisso. Escolha o plano ideal para você após o período de avaliação.</p>
                <div class="pricing-grid">
                    <div class="pricing-card animate-on-scroll" style="--delay: 0.3s;"><h3>Básico</h3><div class="price">R$50<span>/mês</span></div><ul><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Até 10 usuários</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Gerenciamento de tarefas</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Notificações por e-mail</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Relatórios básicos</li></ul><a href="#" class="btn btn-outline">Começar Teste</a></div>
                    <div class="pricing-card popular animate-on-scroll" style="--delay: 0.4s;"><span class="popular-badge">Mais Popular</span><h3>Premium</h3><div class="price">R$150<span>/mês</span></div><ul><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Até 50 usuários</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Tudo do plano Básico</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Integrações com ferramentas</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Suporte prioritário</li></ul><a href="#" class="btn btn-gradient">Começar Teste</a></div>
                    <div class="pricing-card animate-on-scroll" style="--delay: 0.5s;"><h3>Enterprise</h3><div class="price">R$500<span>/mês</span></div><ul><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Usuários ilimitados</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Tudo do plano Premium</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Gerente de conta dedicado</li><li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Segurança avançada (SSO)</li></ul><a href="#" class="btn btn-outline">Fale Conosco</a></div>
                </div>
            </div>
        </section>
        <section id="final-cta" class="section">
            <div class="container" style="display:flex; flex-direction:column; align-items:center;">
                <h2 class="section-title animate-on-scroll">Pronto para transformar sua gestão?</h2>
                <p class="section-subtitle animate-on-scroll" style="--delay: 0.2s;">Junte-se a milhares de equipes que já organizam seu trabalho com o DoingWork. Comece seu teste gratuito hoje mesmo.</p>
                <a href="#" class="btn btn-gradient animate-on-scroll" style="--delay: 0.4s;">Aumentar minha produtividade</a>
            </div>
        </section>
    </main>
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-column animate-on-scroll" style="--delay: 0.1s;"><div class="logo">DoingWork</div><p>A plataforma intuitiva para gestão de projetos modernos.</p><div class="social-icons"><a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a><a href="#"><img src="https://raw.githubusercontent.com/Guilherme-Rossi/Site_StreamLit/main/twitter_sem_fundo.png" alt="Twitter / X" width="20" height="20"></a></div></div>
                <div class="footer-column animate-on-scroll" style="--delay: 0.2s;"><h4>Produto</h4><ul><li><a href="#features">Funcionalidades</a></li><li><a href="#pricing">Preços</a></li><li><a href="#">Integrações</a></li></ul></div>
                <div class="footer-column animate-on-scroll" style="--delay: 0.3s;"><h4>Empresa</h4><ul><li><a href="#">Sobre Nós</a></li><li><a href="#">Carreiras</a></li><li><a href="#">Contato</a></li></ul></div>
                <div class="footer-column animate-on-scroll" style="--delay: 0.4s;"><h4>Legal</h4><ul><li><a href="#">Termos de Serviço</a></li><li><a href="#">Política de Privacidade</a></li></ul></div>
            </div>
            <div class="footer-bottom animate-on-scroll" style="--delay: 0.5s;"><p>&copy; 2025 DoingWork. Todos os direitos reservados.</p><div class="sminex-logo"><p>Um produto da</p><span class="sminex-text">SMINEX ENTERPRISE</span></div></div>
        </div>
    </footer>

    <!-- SCRIPT 1: Animação de Scroll -->
    <script>
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
        elementsToAnimate.forEach((el) => observer.observe(el));
    </script>
    
    <!-- SCRIPT 2: Ajuste dinâmico da altura para o Streamlit -->
    <script>
      window.addEventListener("load", function() {
        Streamlit.setFrameHeight(document.documentElement.scrollHeight);
      });
      const resizeObserver = new ResizeObserver(() => {
        Streamlit.setFrameHeight(document.documentElement.scrollHeight);
      });
      resizeObserver.observe(document.body);
    </script>

</body>
</html>
"""

# 5. RENDERIZAR o site completo usando components.html
# O height inicial é 1500px para evitar um "pulo" na tela, mas o script ajustará para o tamanho exato.
# scrolling=False é importante para que a barra de rolagem principal da página controle tudo.
components.html(full_html_code, height=1500, scrolling=False)
