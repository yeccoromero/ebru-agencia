import glob

# File targets
files = glob.glob("*.html")

html_nav_replace = """<nav>
            <a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>"""

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # Inject toggle in nav
    if "index.html" in f:
        content = content.replace("<nav>", html_nav_replace)
    else:
        # inner pages might have <nav><a href="index.html#work">Work</a>...
        content = content.replace("<nav>", html_nav_replace.replace("index.html#", "index.html#"))

    # Inject i18n.js right before app.js
    if 'src="assets/js/i18n.js"' not in content:
        content = content.replace('<script src="assets/js/app.js"></script>', '<script src="assets/js/i18n.js"></script>\n    <script src="assets/js/app.js"></script>')

    # specific tags for everything:
    if "index.html" in f:
        content = content.replace('<a href="#work">Work</a>', '<a href="#work" data-i18n="nav.work">Work</a>')
        content = content.replace('<a href="#about">About</a>', '<a href="#about" data-i18n="nav.about">About</a>')
        content = content.replace('class="btn-primary">Let\'s Talk</a>', 'class="btn-primary" data-i18n="nav.contact">Let\'s Talk</a>')
        
        content = content.replace('<h1 class="hero-title">WE BUILD<br><span class="accent-text">BETTER BRANDS</span></h1>', '<h1 class="hero-title" data-i18n="hero.title">WE BUILD<br><span class="accent-text">BETTER BRANDS</span></h1>')
        content = content.replace('<p class="hero-subtitle">Estudio de diseño visual', '<p class="hero-subtitle" data-i18n="hero.sub">Visual design studio')

        content = content.replace('<h2>CREATIVE<br><span class="accent-text">DIRECTION</span></h2>', '<h2 data-i18n="about.title">CREATIVE<br><span class="accent-text">DIRECTION</span></h2>')
        content = content.replace('<p>I am Diego Romero, a visual designer', '<p data-i18n="about.desc">I am Diego Romero, a visual designer')

        content = content.replace('<h2>LET\'S CREATE<br>YOUR BRAND.</h2>', '<h2 data-i18n="footer.cta">LET\'S CREATE<br>YOUR BRAND.</h2>')
        content = content.replace('START A PROJECT <i', '<span data-i18n="footer.btn">START A PROJECT <i data-lucide="arrow-right"></i></span> <i')

        # Projects tags on index
        content = content.replace('<p>Branding & Visual Identity</p>', '<p data-i18n="card.visual">Branding & Visual Identity</p>')
        content = content.replace('<p>Branding</p>', '<p data-i18n="card.branding">Branding</p>')
        content = content.replace('<p>Branding & Packaging</p>', '<p data-i18n="card.pkg">Branding & Packaging</p>')
        content = content.replace('<p>Visual Identity</p>', '<p data-i18n="card.visual">Visual Identity</p>')
        content = content.replace('<p>Corporate Identity</p>', '<p data-i18n="card.corp">Corporate Identity</p>')
        content = content.replace('<p>Tech Branding</p>', '<p data-i18n="card.tech">Tech Branding</p>')

    else:
        content = content.replace('<a href="index.html#work">Work</a>', '<a href="index.html#work" data-i18n="nav.work">Work</a>')
        content = content.replace('class="btn-primary">Let\'s Talk</a>', 'class="btn-primary" data-i18n="nav.contact">Let\'s Talk</a>')
        content = content.replace('<p>Client</p>', '<p data-i18n="project.client">Client</p>')
        content = content.replace('<p>Services</p>', '<p data-i18n="project.services">Services</p>')
        
        # Descriptions
        if "catleya" in f: content = content.replace('<p>Conceptualizamos marcas que hablan con autenticidad', '<p data-i18n="catleya.desc">We conceptualize brands that speak with authenticity. We ensure design becomes an integral experience.</p>')
        if "vixmed" in f: content = content.replace('<div class="project-description">\n                <p>Centro especializado', '<div class="project-description">\n                <p data-i18n="vixmed.desc">Centro especializado')
        if "lulas" in f: content = content.replace('<div class="project-description">\n                <p>Una marca que entiende', '<div class="project-description">\n                <p data-i18n="lulas.desc">Una marca que entiende')
        if "wewine" in f: content = content.replace('<div class="project-description">\n                <p>Experiencia premium', '<div class="project-description">\n                <p data-i18n="wewine.desc">Experiencia premium')
        if "sazon" in f: content = content.replace('<div class="project-description">\n                <p>Tradición urbana', '<div class="project-description">\n                <p data-i18n="sazon.desc">Tradición urbana')
        if "kapital" in f: content = content.replace('<div class="project-description">\n                <p>Boutique especializada', '<div class="project-description">\n                <p data-i18n="kapital.desc">Boutique especializada')
        if "bitbit" in f: content = content.replace('<div class="project-description">\n                <p>Plataforma de alta escalabilidad', '<div class="project-description">\n                <p data-i18n="bitbit.desc">Plataforma de alta escalabilidad')
        if "mutta" in f: content = content.replace('<p><strong>Redefinimos la arquitectura', '<p data-i18n="mutta.desc"><strong>Redefinimos la arquitectura')
        if "pilotscafe" in f: content = content.replace('<div class="project-description">\n                <p>Nació como idea', '<div class="project-description">\n                <p data-i18n="pilots.desc">Nació como idea')
        if "samay" in f: content = content.replace('<div class="project-description">\n                <p>En SAMAY, entendemos', '<div class="project-description">\n                <p data-i18n="samay.desc">En SAMAY, entendemos')
        if "swipe" in f: content = content.replace('<div class="project-description">\n                <p>En Swipe, comprendemos', '<div class="project-description">\n                <p data-i18n="swipe.desc">En Swipe, comprendemos')

    with open(f, "w") as file:
        file.write(content)

print("Applied tags everywhere.")
