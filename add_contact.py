import glob

files = glob.glob("*.html")

contact_html = """        <div class="footer-contact-info" style="margin-top: 4rem; display: flex; gap: 3rem; font-size: clamp(1rem, 2vw, 1.5rem); padding: 0 var(--padding-global);">
            <a href="mailto:dirom1988@gmail.com" style="border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; transition: color 0.3s; hover: color: var(--accent);">dirom1988@gmail.com</a>
            <a href="https://wa.me/593958831259" target="_blank" style="border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem; transition: color 0.3s;">+593 958 831 259</a>
        </div>"""

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    if '<div class="footer-bottom">' in content and 'footer-contact-info' not in content:
        # We replace the bottom string to inject our block right above it
        content = content.replace('        <div class="footer-bottom">', contact_html + '\n        <div class="footer-bottom">')
        
        # Link main button to mailto
        if "START A PROJECT" in content:
            content = content.replace('href="mailto:diego@ebru.com"', 'href="mailto:dirom1988@gmail.com"')
            
        with open(f, "w") as file:
            file.write(content)

print("Contact info injected in footers.")
