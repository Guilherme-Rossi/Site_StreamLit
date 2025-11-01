import streamlit as st

# 1. Configurar a página para usar a largura```python
import streamlit as st

# 1. Configurar a página para usar a largura total e o tema claro
st.set_page_config(
    page_title="Doing total e o tema claro
st.set_page_config(
    page_title="Doing Work",
    page Work",
    page_icon="doingworkiconefinal_icone.ico", # Certifique-se que este arquivo existe
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Forçar o_icon="doingworkiconefinal_icone.ico", # Certifique-se que este arquivo existe
    layout tema branco do Streamlit
st.markdown("""
    <style>
        .stApp {
            background-color: white !important;
        }
    </style>
""", unsafe_allow_html=True="wide",
    initial_sidebar_state="collapsed"
)

# 2. Forçar o tema branco do Streamlit
st.markdown("""
    <style>
        .stApp {
            background-color: white)

# 3. Armazenar todo o código HTML e CSS corrigido em uma única string
html_string = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3 charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-. Armazenar todo o código HTML e CSS corrigido em uma única string
html_string = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DoingWork - Gestão de projetos, sem a complexidade</title>
    <style>
        /*scale=1.0">
    <title>DoingWork - Gestão de projetos, sem a complexidade</title> --- Configurações Globais e Fontes --- */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    <style>
        /* --- Configurações Globais e Fontes --- */
        @import url('

        :root {
            --dark-blue: #0d1b2a;
            --mediumhttps://fonts.googleapis.com/css2?family=Inter:wght@400;600;-blue: #1b263b;
            --light-blue: #415a77;
700&display=swap');

        :root {
            --dark-blue: #0d1b2a;
            --medium-blue: #1b263b;
            --light-blue            --text-gray: #778da9;
            --white: #ffffff;
            --primary-gradient: linear-gradient(90deg, #3a86ff 0%, #8338ec 100%);
            --border-radius: 12px;
            --shadow: #415a77;
            --text-gray: #778da9;
            ---sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, white: #ffffff;
            --primary-gradient: linear-gradient(90deg, #3a80, 0.04);
            --shadow-md: 0 10px 15px -6ff 0%, #8338ec 100%);
            --border-radius: 3px rgba(0, 0, 0, 0.08), 0 4px 12px;
            --shadow-sm: 0 4px 6px -1px rgba(06px -2px rgba(0, 0, 0, 0.05);
        }

        body {
            margin: 0;
            font-family: 'Inter', sans-serif; 
            background, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
            --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.0-color: var(--white) !important; 
            color: var(--text-gray); 
            line-height: 1.7; 
            -webkit-font-smoothing: antialiased;
        }

        8), 0 4px 6px -2px rgba(0, 0, 0, * { margin: 0; padding: 0; box-sizing: border-box; }
        html0.05);
        }

        body {
            margin: 0;
            font-family: ' { scroll-behavior: smooth; }
        .container { max-width: 1200px; marginInter', sans-serif; 
            background-color: var(--white) !important; 
            color:: 0 auto; padding: 0 24px; }
        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: var(--text-gray); 
            line-height: 1.7; 
            -webkit-font translateY(0); } }
        .fade-in { animation: fadeIn 0.8s ease-out forwards-smoothing: antialiased;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        .container { max; }

        header { 
            padding: 1.5rem 0; 
            position: sticky-width: 1200px; margin: 0 auto; padding: 0 24px; }
; 
            top: 0; 
            left: 0; 
            width: 1        
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity:00%; 
            z-index: 1000; 
            transition: background-color 1; transform: translateY(0); } }
        .fade-in { animation: fadeIn 0. 0.3s ease, box-shadow 0.3s ease, padding 0.3s ease;8s ease-out forwards; }

        header { 
            padding: 1.5rem 0;
            background-color: rgba(255, 255, 255, 0 
            position: sticky; 
            top: 0; 
            left: 0; 
            .95); 
            backdrop-filter: blur(10px); 
            box-shadow:width: 100%; 
            z-index: 1000; 
            transition var(--shadow-sm);
        }
        nav { display: flex; justify-content: space-between: background-color 0.3s ease, box-shadow 0.3s ease, padding 0.3; align-items: center; }
        .logo { font-size: 1.6rem; fonts ease;
            background-color: rgba(255, 255, 255, -weight: 700; color: var(--dark-blue); }
        .nav-links { list0.95); 
            backdrop-filter: blur(10px); 
            box-shadow:-style: none; display: flex; align-items: center; gap: 2.5rem; padding- var(--shadow-sm);
        }
        nav { display: flex; justify-content: space-between;top: 10px; margin-bottom: 8px}
        .nav-links a { text align-items: center; }
        .logo { font-size: 1.6rem; font-weight: -decoration: none; color: var(--medium-blue) !important; font-weight: 600;700; color: var(--dark-blue); }
        .nav-links { list-style: none transition: color 0.3s; }
        .nav-links a:hover { color: #3a86; display: flex; align-items: center; gap: 2.5rem; padding-top: 10px; margin-bottom: 8px}
        .nav-links a { text-decoration: none; color: var(--medium-blue) !important; font-weight: 600; transition: colorff !important; }
        .nav-actions { display: flex; align-items: center; gap: 1 0.3s; }
        .nav-links a:hover { color: #3a86.5rem; }
        .login-link { text-decoration: none; color: var(--medium-blue) !ff !important; }
        .nav-actions { display: flex; align-items: center; gap: 1.5rem; }
        .login-link { text-decoration: none; color: var(--medium-blue)important; font-weight: 600; transition: color 0.3s; }
        .login-link:hover { color: #3a86ff !important; }
        
        .dropdown !important; font-weight: 600; transition: color 0.3s; }
         { position: relative; display: inline-block; }
        .dropdown-toggle { cursor: pointer; display.login-link:hover { color: #3a86ff !important; }
        
        .: flex; align-items: center; }
        .dropdown-menu { display: none; position: absolutedropdown { position: relative; display: inline-block; }
        .dropdown-toggle { cursor: pointer; display: flex; align-items: center; }
        .dropdown-menu { display: none; position: absolute; top; top: 130%; left: 50%; transform: translateX(-50%); background: var(--white); border-radius: var(--border-radius); box-shadow: var(--shadow-md); list-style: none: 130%; left: 50%; transform: translateX(-50%); background: var(--white; padding: 0.5rem; width: 200px; z-index: 1; opacity); border-radius: var(--border-radius); box-shadow: var(--shadow-md); list-style: none; padding: 0.5rem; width: 200px; z-index: 1; opacity: 0; visibility: hidden; transition: opacity 0.3s ease; }
        .dropdown:hover .dropdown-menu { display: block; opacity: 1; visibility: visible; }
        .dropdown-menu a { display: block; padding: 0.75rem 1rem; border-radius: 8px; }
        .dropdown-menu a:hover { background-color: #f8f9fa; }
        : 0; visibility: hidden; transition: opacity 0.3s ease; }
        .dropdown:hover .dropdown.arrow { display: inline-block; transition: transform 0.3s ease; margin-left: -menu { display: block; opacity: 1; visibility: visible; }
        .dropdown-menu a { display4px; }
        .dropdown:hover .arrow { transform: rotate(180deg); }

: block; padding: 0.75rem 1rem; border-radius: 8px; }        .btn { padding: 12px 28px; border-radius: 8px; text
        .dropdown-menu a:hover { background-color: #f8f9fa; }
        -decoration: none; font-weight: 600; transition: all 0.3s ease; display: inline-block; border: none; font-size: 0.9rem;}
        .btn.arrow { display: inline-block; transition: transform 0.3s ease; margin-left: 4px;-gradient { background: var(--primary-gradient); color: var(--white) !important; box-shadow: }
        .dropdown:hover .arrow { transform: rotate(180deg); }

        .btn var(--shadow-sm); }
        .btn:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
        .btn-outline { background: transparent; color: var(--dark-blue) ! { padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; display: inline-important; border: 2px solid #e0e1dd; }
        .btn-outline:hover { backgroundblock; border: none; font-size: 0.9rem;}
        .btn-gradient { background: var(--primary-gradient); color: var(--white) !important; box-shadow: var(--shadow-sm); }
        .btn:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }
        .btn-outline { background: transparent; color: var(--dark-blue) !important; border: 2px solid: var(--dark-blue); color: var(--white) !important; }

        #hero { padding: 100px 0 120px 0; }
        .hero-content { display: flex; align-items: center; justify-content: space-between; gap: 4rem; }
        .hero #e0e1dd; }
        .btn-outline:hover { background: var(--dark-blue);-text { max-width: 50%; }
        .hero-text h1 { font-size:  color: var(--white) !important; }

        #hero { padding: 100px 0 3.8rem; color: var(--dark-blue) !important; line-height: 1.2;120px 0; }
        .hero-content { display: flex; align-items: center margin-bottom: 1.5rem; }
        .hero-text p { font-size: 1.25rem; margin-bottom: 2.5rem; color: var(--light-blue) !important;; justify-content: space-between; gap: 4rem; }
        .hero-text { max-width: 50%; }
        .hero-text h1 { font-size: 3.8rem; }
        .hero-mockup { width: 45%; height: 350px; background: # color: var(--dark-blue) !important; line-height: 1.2; margin-bottom:f0f4f9; border-radius: var(--border-radius); box-shadow: var(--shadow- 1.5rem; }
        .hero-text p { font-size: 1.25rem;md); padding: 1.5rem; border: 1px solid #e0e1dd; }
         margin-bottom: 2.5rem; color: var(--light-blue) !important; }
        .hero-.mockup-header { display: flex; gap: 8px; margin-bottom: 1rem; }mockup { width: 45%; height: 350px; background: #f0f4
        .mockup-header span { width: 12px; height: 12px; borderf9; border-radius: var(--border-radius); box-shadow: var(--shadow-md); padding: 1-radius: 50%; }
        .mockup-content { width: 100%; height:.5rem; border: 1px solid #e0e1dd; }
        .mockup-header { display: flex; gap: 8px; margin-bottom: 1rem; }
        .mockup-header span { width: 12px; height: 12px; border-radius: 50%; }
        .mockup-content { width: 100%; height: 85%; background: var(--white); border-radius: 8px; }
        .section { padding: 10 85%; background: var(--white); border-radius: 8px; }
        .section { padding: 100px 0; }
        .section-light { background-color: #f8f0px 0; }
        .section-light { background-color: #f8f9fa; }
9fa; }
        
        .section-title { text-align: center; font-size:         
        .section-title { text-align: center; font-size: 2.8rem; color: var2.8rem; color: var(--dark-blue) !important; margin-bottom: 1rem;(--dark-blue) !important; margin-bottom: 1rem; }
        
        .section-subtitle { 
            display: block !important;
            text-align: center !important; 
            font-size }
        
        .section-subtitle { 
            display: block !important;
            text-align: center !important; 
            font-size: 1.15rem; 
            margin-bottom: 5rem; 
            max-width: 700px; 
            margin-left: auto !important;: 1.15rem; 
            margin-bottom: 5rem; 
            max-width:  
            margin-right: auto !important; 
            color: var(--light-blue) !important700px; 
            margin-left: auto !important; 
            margin-right: auto !important; 
            color: var(--light-blue) !important; 
        }
        
; 
        }
        
        .features-grid { display: grid; grid-template-columns: repeat(auto        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(-fit, minmax(250px, 1fr)); gap: 2rem; }
        .feature-card { background: var(--white); padding: 2.5rem 2rem; border-radius: var(--border-radius); text-align: left; box-shadow: var(--shadow-sm); border: 1px250px, 1fr)); gap: 2rem; }
        .feature-card { background solid #e0e1dd; transition: all 0.3s ease; }
        .feature-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
        .feature-card .icon { margin-bottom: 1.5rem; background: var(--primary-gradient); width: 50: var(--white); padding: 2.5rem 2rem; border-radius: var(--border-radius); text-align: left; box-shadow: var(--shadow-sm); border: 1px solid #e0px; height: 50px; border-radius: 50%; display: flex; align-items: centere1dd; transition: all 0.3s ease; }
        .feature-card:hover { transform: translateY; justify-content: center; }
        .feature-card h3 { font-size: 1.(-5px); box-shadow: var(--shadow-md); }
        .feature-card .icon { margin3rem; color: var(--dark-blue) !important; margin-bottom: 0.5rem; }
        -bottom: 1.5rem; background: var(--primary-gradient); width: 50px; height:.feature-card p { color: var(--text-gray) !important; }

        .pricing-grid { display: 50px; border-radius: 50%; display: flex; align-items: center; justify grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: stretch; }
        .pricing-card { display: flex; flex-direction: column; background: var(--white); border-radius: var(--border-radius); padding-content: center; }
        .feature-card h3 { font-size: 1.3rem; color: var(--dark-blue) !important; margin-bottom: 0.5rem; }
        .feature-card p { color: var(--text-gray) !important; }

        .pricing-grid { display:: 2.5rem; text-align: center; border: 1px solid #e0e1dd; transition: all 0.3s ease; position: relative; box-shadow: var(--shadow-sm); }
         grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: stretch; }
        
        /* --- CORREÇÃO FINAL A.pricing-card:hover { transform: translateY(-10px); box-shadow: var(--shadow-md); }
        
        .pricing-card.popular { 
            border: 2px solid #3PLICADA AQUI (1/2) --- */
        .pricing-card { 
            display: flex; 
            flex-direction: column; 
            background: var(--white); 
            border-radius:a86ff; 
            transform: scale(1.05); 
            transform-origin: top var(--border-radius); 
            padding: 2.5rem; 
            text-align:;
        }
        .pricing-card.popular:hover { 
            transform: scale(1.05 center; 
            border: 1px solid #e0e1dd; 
            transition: all) translateY(-10px); 
        }

        .pricing-card h3 { font-size: 0.3s ease; 
            position: relative; 
            box-shadow: var(--shadow-sm); 1.5rem; color: var(--dark-blue) !important; }
        .pricing-card .price { font-size: 3.5rem; font-weight: 700; color: var 
        }

        .pricing-card:hover { transform: translateY(-10px); box-shadow: var(--dark-blue) !important; margin: 1rem 0; }
        .pricing-card .(--shadow-md); }
        .pricing-card.popular { border: 2px solid #3a86ffprice span { font-size: 1rem; font-weight: 400; color: var(--; transform: scale(1.05); transform-origin: top; }
        .pricing-card.populartext-gray) !important; }
        .pricing-card ul { list-style: none; margin: 2rem:hover { transform: scale(1.05) translateY(-10px); }
        .pricing-card h 0; text-align: left; flex-grow: 1; }
        .pricing-card ul3 { font-size: 1.5rem; color: var(--dark-blue) !important; } li { margin-bottom: 1rem; display: flex; align-items: center; color: var(--text-gray
        .pricing-card .price { font-size: 3.5rem; font-weight: 700) !important; }
        .pricing-card ul li svg { margin-right: 10px;; color: var(--dark-blue) !important; margin: 1rem 0; }
        .pricing-card .price span { font-size: 1rem; font-weight: 400; color: #3a86ff; }
        .popular-badge { position: absolute; top: - color: var(--text-gray) !important; }
        
        /* --- CORREÇÃO FINAL APLICADA AQUI15px; left: 50%; transform: translateX(-50%); background: var(--primary-gradient); color: (2/2) --- */
        .pricing-card ul { 
            list-style: none; var(--white) !important; padding: 5px 15px; border-radius: 20px 
            margin: 2rem 0; 
            text-align: left; 
            flex-grow:; font-size: 0.9rem; font-weight: 600; }
        
 1; /* Faz a lista ocupar todo o espaço vago */
        }

        .pricing-card ul li        /* --- CORREÇÃO FINAL APLICADA AQUI --- */
        .pricing-card .btn {
             { margin-bottom: 1rem; display: flex; align-items: center; color: var(--text-graymargin-top: auto; /* Força o botão para o fundo do card */
        }

        #final) !important; }
        .pricing-card ul li svg { margin-right: 10px;-cta { background: var(--medium-blue); text-align: center; }
        #final-cta h2 color: #3a86ff; }
        .popular-badge { position: absolute; top: - { color: var(--white) !important; }
        #final-cta p { color: #E8E815px; left: 50%; transform: translateX(-50%); background: var(--primary-gradientE8 !important; }
        
        footer { background-color: #f8f9fa; padding:); color: var(--white) !important; padding: 5px 15px; border-radius: 80px 0 40px 0; }
        .footer-grid { display: grid; grid 20px; font-size: 0.9rem; font-weight: 600; }
-template-columns: repeat(4, 1fr); gap: 2rem; margin-bottom:         
        #final-cta { background: var(--medium-blue); text-align: center; }
        4rem; }
        .footer-column .logo { margin-bottom: 1rem; }
        .footer#final-cta h2 { color: var(--white) !important; }
        #final-cta p-column p { max-width: 250px; margin-bottom: 1.5rem; color: var(--dark-blue) !important; }
        .social-icons a { display: inline-block { color: #E8E8E8 !important; }
        
        footer { background-color: #; margin-right: 1rem; opacity: 0.7; transition: opacity 0.3s;f8f9fa; padding: 80px 0 40px 0; }
         }
        .social-icons a:hover { opacity: 1; }
        .footer-column h.footer-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 4 { font-size: 1rem; color: var(--dark-blue) !important; margin-bottom: 12rem; margin-bottom: 4rem; }
        .footer-column .logo { margin-bottom: .5rem; text-transform: uppercase; letter-spacing: 0.5px; }
        .footer-column1rem; }
        .footer-column p { max-width: 250px; margin-bottom:  ul { list-style: none; }
        .footer-column ul li { margin-bottom: 1rem;1.5rem; color: var(--dark-blue) !important; }
        .social-icons a { display }
        .footer-column ul li a { text-decoration: none; color: var(--dark-blue) !: inline-block; margin-right: 1rem; opacity: 0.7; transition: opacity 0important; transition: color 0.3s; }
        .footer-column ul li a:hover { color.3s; }
        .social-icons a:hover { opacity: 1; }
        .: #3a86ff !important; }
        .footer-bottom { border-top: 1px solid #footer-column h4 { font-size: 1rem; color: var(--dark-blue) !importante0e1dd; padding-top: 2rem; display: flex; justify-content: space-between; align; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 0.5px-items: center; font-size: 0.9rem; }
        .footer-bottom p { color:; }
        .footer-column ul { list-style: none; }
        .footer-column ul li { margin-bottom: 1rem; }
        .footer-column ul li a { text-decoration: none; color var(--text-gray) !important; }
        .sminex-logo { text-align: right; }: var(--dark-blue) !important; transition: color 0.3s; }
        .footer-
        .sminex-logo p { font-size: 0.9rem; margin-bottom: column ul li a:hover { color: #3a86ff !important; }
        .footer-0.5rem; color: var(--text-gray) !important; }
        .sminex-bottom { border-top: 1px solid #e0e1dd; padding-top: 2rem; displaylogo .sminex-text { font-weight: 700; font-size: 1.2rem; background: var(--primary-gradient); -webkit-background-clip: text; -webkit-text-fill-: flex; justify-content: space-between; align-items: center; font-size: 0.9rem; }
        .footer-bottom p { color: var(--text-gray) !important; }
        .sminecolor: transparent; }

        .mobile-menu-icon, .nav-links-mobile { display: none; }
x-logo { text-align: right; }
        .sminex-logo p { font-size: 0.9rem; margin-bottom: 0.5rem; color: var(--text-gray) !important;        @media (max-width: 992px) {
            .nav-links, .nav-actions }
        .sminex-logo .sminex-text { font-weight: 700; { display: none; }
            .mobile-menu-icon { display: block; cursor: pointer; z-index: 1001; }
            .mobile-menu-icon div { width: 25px font-size: 1.2rem; background: var(--primary-gradient); -webkit-background-clip: text; height: 3px; background-color: var(--dark-blue); margin: 5px 0;; -webkit-text-fill-color: transparent; }

        .mobile-menu-icon, .nav-links- }
            .hero-content { flex-direction: column; text-align: center; }
            .mobile { display: none; }
        @media (max-width: 992px) {
hero-text { max-width: 100%; }
            .hero-mockup { display: none; }
            .footer-grid { grid-template-columns: 1fr 1fr; }            .nav-links, .nav-actions { display: none; }
            .mobile-menu-icon { display: block; cursor: pointer; z-index: 1001; }
            .mobile-menu-icon
        }
        @media (max-width: 768px) {
            #hero h div { width: 25px; height: 3px; background-color: var(--dark-blue);1 { font-size: 2.8rem; }
            .section-title { font-size: margin: 5px 0; }
            .hero-content { flex-direction: column; text-align: center 2.2rem; }
            .footer-grid { grid-template-columns: 1fr; text-align: center; }
            .footer-column p { margin-left: auto; margin-right; }
            .hero-text { max-width: 100%; }
            .hero-: auto; }
            .social-icons { text-align: center; }
            .footer-bottom { flexmockup { display: none; }
            .footer-grid { grid-template-columns: 1fr -direction: column; gap: 1rem; }
            .sminex-logo { text-align: center1fr; }
        }
        @media (max-width: 768px) {
            #; }
        }
    </style>
</head>
<body>
    <header class="fade-in">
hero h1 { font-size: 2.8rem; }
            .section-title { font-size:        <nav class="container">
            <div class="logo">DoingWork</div>
            <ul class="nav 2.2rem; }
            .footer-grid { grid-template-columns: 1fr;-links">
                <li><a href="#features">Funcionalidades</a></li>
                <li><a href="#"> text-align: center; }
            .footer-column p { margin-left: auto; margin-right: auto; }
            .social-icons { text-align: center; }
            .footer-bottom { flexPara Quem?</a></li>
                <li><a href="#pricing">Preços</a></li>
                <li><a href="#">Integra-direction: column; gap: 1rem; }
            .sminex-logo { text-align: centerções</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle">Recursos <; }
        }
    </style>
</head>
<body>
    <header class="fade-in">
        <nav class="container">
            <div class="logo">DoingWork</div>
            <ul class="navspan class="arrow">▾</span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Central de Ajuda</a></li>
                        <li><a href="#">Contato</a></li>
                    -links">
                <li><a href="#features">Funcionalidades</a></li>
                <li><a href="#"></ul>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="#" class="loginPara Quem?</a></li>
                <li><a href="#pricing">Preços</a></li>
                <li><a href="#">Integrações</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle">Rec-link">Login</a>
                <a href="#final-cta" class="btn btn-gradient">Começar Grátis</a>
            </div>
            <div class="mobile-menu-icon">
                <div class="ursos <span class="arrow">▾</span></a>
                    <ul class="dropdown-menu">
                        <li><aline1"></div>
                <div class="line2"></div>
                <div class="line3"></div> href="#">Blog</a></li>
                        <li><a href="#">Central de Ajuda</a></li>
                        <li><a href="#">Contato
            </div>
        </nav>
    </header>
    <main>
        <section id="hero"</a></li>
                    </ul>
                </li>
            </ul>
            <div class="nav-actions">
                <a href="#" class="login-link">Login</a>
                <a href="#final-cta" class="btn btn-gradient">Começar Grátis</a>
            </div>
            <div class="mobile-menu-icon">
                <div class="section fade-in">
            <div class="container hero-content">
                <div class="hero-text class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>">
                    <h1>Gestão de projetos, sem a complexidade.</h1>
                    <p>O DoingWork é
            </div>
        </nav>
    </header>
    <main>
        <section id="hero" a plataforma intuitiva que centraliza suas tarefas, melhora a comunicação e impulsiona a produtividade da sua equipe.</p>
                    <a href="#pricing" class="btn btn-gradient">Comece seu teste de 1 mês</a>
                </div>
                <div class="hero-mockup">
                    <div class="mockup-header"> class="section fade-in">
            <div class="container hero-content">
                <div class="hero-text
                        <span style="background:#ff5f56;"></span>
                        <span style="background:#ffbd">
                    <h1>Gestão de projetos, sem a complexidade.</h1>
                    <p>O DoingWork é2e;"></span>
                        <span style="background:#27c93f;"></span>
                    </div>
                     a plataforma intuitiva que centraliza suas tarefas, melhora a comunicação e impulsiona a produtividade da sua equipe.</<div class="mockup-content"></div>
                </div>
            </div>
        </section>
        <p>
                    <a href="#pricing" class="btn btn-gradient">Comece seu teste de 1 mês</a>section id="features" class="section section-light fade-in">
             <div class="container">
                
                </div>
                <div class="hero-mockup">
                    <div class="mockup-header<h2 class="section-title">Tudo o que você precisa em um só lugar</h2>
                <p">
                        <span style="background:#ff5f56;"></span>
                        <span style="background:#ffbd class="section-subtitle">Ferramentas poderosas e fáceis de usar para levar sua equipe ao próximo nível de organização2e;"></span>
                        <span style="background:#27c93f;"></span>
                    </div>
                    <div class="mockup-content"></div>
                </div>
            </div>
        </section>
        < e eficiência.</p>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/section id="features" class="section section-light fade-in">
             <div class="container">
                <hsvg" width="24" height="24" viewBox="0 0 24" fill="none2 class="section-title">Tudo o que você precisa em um só lugar</h2>
                <p class="section-" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path dsubtitle">Ferramentas poderosas e fáceis de usar para levar sua equipe ao próximo nível de organização e eficiência.</p>
                <div class="features-grid">
                    <div class="feature-card">
="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke 2-2V8z"></path><polyline points="14 2 14 8 2="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-0 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></2V8z"></path><polyline points="14 2 14 8 20 8"></svg></div>
                        <h3>Gestão de Tarefas</h3>
                        <p>Crie, atribua e acompanhe o progresso com status visuais e prazos claros para nunca mais perder uma entrega.</p>
                    </div>
                    <polyline><line x1="16" y1="13" x2="8" y2="13"></linediv class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3><line x1="16" y1="17" x2="8" y2="17.org/2000/svg" width="24" height="24" viewBox="0 "></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round
                        <h3>Gestão de Tarefas</h3>
                        <p>Crie, atribua e acompanhe o progresso com" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5  status visuais e prazos claros para nunca mais perder uma entrega.</p>
                    </div>
                    <div class="feature0 0 1-7.6 4.7 8.38 8.38 0 0-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2 1-3.8-.9L3 21l1.9-5.7a8.38000/svg" width="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin 8.38 0 0 1-.9-3.8 8.5 8.5 ="round"><path d="M21 11.5a8.38 8.38 0 0 1 4.7-7.6 8.38 8.38 0 0 0 1-.9 3.8 8.5 8.5 0 0 0 1 3.8-.9h.5a8.48 8.48 01-7.6 4.7 8.38 8.38 0 0 1-3 0 1 8 8v.5z"></path></svg></div>
                        <h3>Comunicação Central.8-.9L3 21l1.9-5.7a8.38 8.38izada</h3>
                        <p>Anexe arquivos, adicione comentários e receba notificações. Mantenha toda a equipe na mesma 0 0 1-.9-3.8 8.5 8.5 0 0  página, sempre.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><1 4.7-7.6 8.38 8.38 0 0 1 svg xmlns="http://www.w3.org/2000/svg" width="24"3.8-.9h.5a8.48 8.48 0 0 1 height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width=" 8 8v.5z"></path></svg></div>
                        <h3>Comunicação Centralizada</h3>
                        2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v<p>Anexe arquivos, adicione comentários e receba notificações. Mantenha toda a equipe na mesma página,6a2 2 0 0 1-2 2H5a2 2 0 0  sempre.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon1-2-2V8a2 2 0 0 1 2-2h6"></"><svg xmlns="http://www.w3.org/2000/svg" width="24path><polyline points="15 3 21 3 21 9"></polyline><line x1="" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v10" y1="14" x2="21" y2="3"></line></svg></div>
6a2 2 0 0 1-2 2H5a2 2 0 0                         <h3>Relatórios e Insights</h3>
                        <p>Acesse dados em tempo real e gere relatórios para analisar o1-2-2V8a2 2 0 0 1 2-2h6"></ desempenho e tomar decisões mais inteligentes.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" widthpath><polyline points="15 3 21 3 21 9"></polyline><line x1="1="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff"0" y1="14" x2="21" y2="3"></line></svg></div>
                        <h3>Relatórios e Insights</h3>
                        <p>Acesse dados em tempo real e gere relatórios para analisar stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="1 o desempenho e tomar decisões mais inteligentes.</p>
                    </div>
                    <div class="feature-card">
                        <div class="icon"><svg xmlns="http://www.w3.org/2000/svg" width2" y1="18" x2="12.01" y2="18"></line></svg>="24" height="24" viewBox="0 0 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2</div>
                        <h3>Mobilidade Total</h3>
                        <p>Gerencie seus projetos de onde estiver com nosso site e aplicativo" width="14" height="20" rx="2" ry="2"></rect><line x1="1 móvel. Sua equipe conectada a qualquer momento.</p>
                    </div>
                </div>
            </div>
        </section>
        <section id="pricing" class="section fade-in">
            <div class="2" y1="18" x2="12.01" y2="18"></linecontainer">
                <h2 class="section-title">Planos flexíveis para cada equipe</h2>
                <></svg></div>
                        <h3>Mobilidade Total</h3>
                        <p>Gerencie seus projetos de onde estiver comp class="section-subtitle">Comece com um teste gratuito de 1 mês. Sem compromisso. Escolha o plano nosso site e aplicativo móvel. Sua equipe conectada a qualquer momento.</p>
                    </div>
                </div>
 ideal para você após o período de avaliação.</p>
                <div class="pricing-grid">
                    <div            </div>
        </section>
        <section id="pricing" class="section fade-in">
            <div class class="pricing-card">
                        <h3>Básico</h3>
                        <div class="price">R$50="container">
                <h2 class="section-title">Planos flexíveis para cada equipe</h2>
                <<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 p class="section-subtitle">Comece com um teste gratuito de 1 mês. Sem compromisso. Escolha24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke o plano ideal para você após o período de avaliação.</p>
                <div class="pricing-grid">
-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>                    <div class="pricing-card">
                        <h3>Básico</h3>
                        <div class="price">R$50<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/Até 10 usuários</li>
                            <li><svg xmlns="http://www.w3.org/20002000/svg" width="20" height="20" viewBox="0 0 24" fill/svg" width="20" height="20" viewBox="0 0 24" fill="="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Gerenciamento de tarefaspolyline points="20 6 9 17 4 12"></polyline></svg>Até 1</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor"0 usuários</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 ="20" height="20" viewBox="0 0 24" fill="none" stroke="6 9 17 4 12"></polyline></svg>Notificações por e-mail</li>
currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="2                            <li><svg xmlns="http://www.w3.org/2000/svg" width="0 6 9 17 4 12"></polyline></svg>Gerenciamento de tarefas</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor"20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 " stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="206 9 17 4 12"></polyline></svg>Notificações por e-mail</li>
 6 9 17 4 12"></polyline></svg>Relatórios básicos</li>
                        </ul>
                        <a href="#" class="btn btn-outline">Começar Teste</a>
                    </div>
                    <div class="                            <li><svg xmlns="http://www.w3.org/2000/svg" width="pricing-card popular">
                        <span class="popular-badge">Mais Popular</span>
                        <h3>Premium</h3>
                        20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20<div class="price">R$150<span>/mês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width 6 9 17 4 12"></polyline></svg>Relatórios básicos</li>
                        </ul>
                        <a href="#" class="btn btn-outline">Começar Teste</a>
                    </div>
                    <="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Até 50 usuários</li>
                            <li><div class="pricing-card popular">
                        <span class="popular-badge">Mais Popular</span>
                        <h3>svg xmlns="http://www.w3.org/2000/svg" width="20"Premium</h3>
                        <div class="price">R$150<span>/mês</span></div>
                        <ul>
 height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-                            <li><svg xmlns="http://www.w3.org/2000/svg" width="width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor9 17 4 12"></polyline></svg>Tudo do plano Básico</li>
                            <li><svg xmlns" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20="http://www.w3.org/2000/svg" width="20" height=" 6 9 17 4 12"></polyline></svg>Até 50 usuários</li>20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="
                            <li><svg xmlns="http://www.w3.org/2000/svg" width2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 ="20" height="20" viewBox="0 0 24" fill="none" stroke="17 4 12"></polyline></svg>Integrações com ferramentas</li>
                            <li><svg xmlns="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="2http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="20 6 9 17 4 12"></polyline></svg>Tudo do plano Básico</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Suporte prioritário</li>
                        </ul>
                        <a href="#" class0" height="20" viewBox="0 0 24" fill="none" stroke="currentColor"="btn btn-gradient">Começar Teste</a>
                    </div>
                    <div class="pricing-card"> stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 
                        <h3>Enterprise</h3>
                        <div class="price">R$500<span>/mês</span></div>6 9 17 4 12"></polyline></svg>Integrações com ferramentas</li>
                            
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2000/<li><svg xmlns="http://www.w3.org/2000/svg" width="2svg" width="20" height="20" viewBox="0 0 24" fill="none0" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 " stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline6 9 17 4 12"></polyline></svg>Suporte prioritário</li>
                        </ul>
                        < points="20 6 9 17 4 12"></polyline></svg>Usuários ilimitadosa href="#" class="btn btn-gradient">Começar Teste</a>
                    </div>
                    <div class="</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg"pricing-card">
                        <h3>Enterprise</h3>
                        <div class="price">R$500<span>/ width="20" height="20" viewBox="0 0 24" fill="none" strokemês</span></div>
                        <ul>
                            <li><svg xmlns="http://www.w3.org/2="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="000/svg" width="20" height="20" viewBox="0 0 2420 6 9 17 4 12"></polyline></svg>Tudo do plano Premium" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor">Usuários ilimitados</li>
                            <li><svg xmlns="http://www.w3.org/2 stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 000/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin6 9 17 4 12"></polyline></svg>Gerente de conta dedicado</li>
                            <li><svg xmlns="http://www.w3.org/2000/svg" width="20="round"><polyline points="20 6 9 17 4 12"></polyline></svg" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width=">Tudo do plano Premium</li>
                            <li><svg xmlns="http://www.w3.org/202" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 00/svg" width="20" height="20" viewBox="0 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="17 4 12"></polyline></svg>Segurança avançada (SSO)</li>
                        </ul>round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <a href="#" class="btn btn-outline">Fale Conosco</a>
                    </div>
                </div>Gerente de conta dedicado</li>
                            <li><svg xmlns="http://www.w3.org/200
            </div>
        </section>
        <section id="final-cta" class="section fade-in">
            <div class="container" style="display:flex; flex-direction:column; align-items:center;">0/svg" width="20" height="20" viewBox="0 0 24" fill
                <h2 class="section-title">Pronto para transformar sua gestão?</h2>
                <p class="="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>Segurança avançada (SSO)</li>
                        </ul>
                        <a href="#" class="btn btn-outline">Fsection-subtitle">Junte-se a milhares de equipes que já organizam seu trabalho com o DoingWork. Comece seu testeale Conosco</a>
                    </div>
                </div>
            </div>
        </section>
        <section id="final gratuito hoje mesmo.</p>
                <a href="#" class="btn btn-gradient">Aumentar minha produtividade</a>
-cta" class="section fade-in">
            <div class="container" style="display:flex; flex-            </div>
        </section>
    </main>
    <footer class="fade-in">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-columndirection:column; align-items:center;">
                <h2 class="section-title">Pronto para transformar sua gestão?</h2>
                <p class="section-subtitle">Junte-se a milhares de equipes que">
                    <div class="logo">DoingWork</div>
                    <p>A plataforma intuitiva para gestão de projetos modernos já organizam seu trabalho com o DoingWork. Comece seu teste gratuito hoje mesmo.</p>
                <a href="#".</p>
                    <div class="social-icons">
                        <a href="#"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 class="btn btn-gradient">Aumentar minha produtividade</a>
            </div>
        </section>
    </main> 0 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="
    <footer class="fade-in">
        <div class="container">
            <div class="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1footer-grid">
                <div class="footer-column">
                    <div class="logo">DoingWork</div>
                    <p>A plataforma intuitiva para gestão de projetos modernos.</p>
                    <div class="social-icons 6 6v7h-4v-7a2 2 0 0 0-2-">
                        <a href="#"><svg xmlns="http://www.w3.org/2000/svg" width2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="="20" height="20" viewBox="0 0 24" fill="none" stroke="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svgcurrentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M></a>
                        <a href="#"><img src="https://raw.githubusercontent.com/Guilherme-Ross16 8a6 6 0 0 1 6 6v7h-4v-i/Site_StreamLit/main/twitter_sem_fundo.png" alt="Twitter / X" width7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect="20" height="20"></a> 
                    </div>
                </div>
                <div class="footer-column">
                    <h4>Produto</h4>
                    <ul>
                        <li><a href="#features">Funcionalidades</a></li>
                        ><circle cx="4" cy="4" r="2"></circle></svg></a>
                        <a href="#"><<li><a href="#pricing">Preços</a></li>
                        <li><a href="#">Integrações</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Empresa</h4>
                    <ul>
                        <li><a href="#">Sobre Nós</a></li>
                        <li><a href="#">Carreiras</a></li>
                        <li><img src="https://raw.githubusercontent.com/Guilherme-Rossi/Site_StreamLit/maina href="#">Contato</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    /twitter_sem_fundo.png" alt="Twitter / X" width="20" height="20<h4>Legal</h4>
                    <ul>
                        <li><a href="#">Termos de Serviço</a></li>
                        <li><a"></a> 
                    </div>
                </div>
                <div class="footer-column">
                    <h4>Produto</h4>
                    <ul> href="#">Política de Privacidade</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">

                        <li><a href="#features">Funcionalidades</a></li>
                        <li><a href="#pricing">Pre                <p>&copy; 2025 DoingWork. Todos os direitos reservados.</p>
                <div class="sminex-logo">
                    <p>Um produto da</p>
                    <span class="sminexços</a></li>
                        <li><a href="#">Integrações</a></li>
                    </ul>
                </div>
                <-text">SMINEX ENTERPRISE</span>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>div class="footer-column">
                    <h4>Empresa</h4>
                    <ul>
                        <li><a href="#">Sobre Nós</a></li>
                        <li><a href="#">Carreiras</a></li>
                        <li><a href="#">Contato</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Legal</h4>
                    
"""

# 4. RENDERIZAR O HTML NO STREAMLIT
st.markdown(html_string, unsafe_allow_html=True)
```<ul>
                        <li><a href="#">Termos de Serviço</a></li>
                        <li><a href="#">Política de Privacidade</a></li>
