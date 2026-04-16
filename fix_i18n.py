import glob, re

files = glob.glob("*.html")
for f in files:
    if "index.html" in f: continue
    
    # Map file name to key
    key = f.replace(".html", "").replace("-cafeteria", "").replace("delSebas", "")
    if "pilotscafe" in key: key = "pilots"
    if "sazon" in key: key = "sazon"
    if "catleya" in key: key = "catleya"
    
    with open(f, "r") as file:
        content = file.read()
    
    # Use regex to inject data-i18n attribute into the first <p> inside project-description
    # We look for <div class="project-description"> followed by whatever spaces, then <p> OR <p data-i18n="..."> 
    # to avoid double injecting if it's already there
    
    # Clean up old bad injects if they happened
    content = re.sub(r'<p data-i18n="[^"]+">', '<p>', content)
    
    # Inject client and services
    content = content.replace('<p>Client</p>', f'<p data-i18n="project.client">Client</p>')
    content = content.replace('<p>Services</p>', f'<p data-i18n="project.services">Services</p>')
    
    # Inject main description
    pattern = r'(<div class="project-description">\s*)<p>'
    replacement = r'\1<p data-i18n="' + key + r'.desc">'
    
    content = re.sub(pattern, replacement, content, count=1)
    
    with open(f, "w") as file:
        file.write(content)

print("Fixed description tags everywhere.")
