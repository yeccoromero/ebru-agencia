import glob

files = glob.glob("*.html")

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # We find the <nav> block
    if '<button id="menu-toggle"' in content:
        continue # already done

    if 'index.html' in f:
        old_nav = """        <nav>
            <a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>
            <a href="#work" data-i18n="nav.work">Work</a>
            <a href="#about" data-i18n="nav.about">About</a>
            <a href="https://wa.me/593958831259" target="_blank" class="btn-primary" data-i18n="nav.contact">Let's Talk</a>
        </nav>"""
        new_nav = """        <div class="mobile-controls">
            <a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>
            <button id="menu-toggle" class="hamburger-btn"><i data-lucide="menu"></i></button>
        </div>
        <nav id="main-nav">
            <a href="#work" data-i18n="nav.work" class="nav-link">Work</a>
            <a href="#about" data-i18n="nav.about" class="nav-link">About</a>
            <a href="https://wa.me/593958831259" target="_blank" class="btn-primary" data-i18n="nav.contact">Let's Talk</a>
        </nav>"""
        content = content.replace(old_nav, new_nav)
    else:
        old_nav_inner = """        <nav>
            <a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>
            <a href="index.html#work" data-i18n="nav.work">Work</a>
            <a href="index.html#about" data-i18n="nav.about">About</a>
            <a href="https://wa.me/593958831259" target="_blank" class="btn-primary" data-i18n="nav.contact">Let's Talk</a>
        </nav>"""
        # some might miss the data-i18n tag on about, let me do a more generic replacement
        # splitting by sections
        content = content.replace('<a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>', '')
        
        # Now find the nav opening to inject mobile controls right before it
        controls = """        <div class="mobile-controls">
            <a href="#" id="lang-toggle" style="margin-right:1rem; font-weight:700; color:var(--accent);">EN</a>
            <button id="menu-toggle" class="hamburger-btn"><i data-lucide="menu"></i></button>
        </div>
        <nav id="main-nav">"""
        content = content.replace('<nav>', controls)
        content = content.replace('</a>\n        </nav>', '</a>\n        </nav>')

    with open(f, "w") as file:
        file.write(content)
print("done")
