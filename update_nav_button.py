import glob

files = glob.glob("*.html")

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # We find the specific Let's Talk button line
    # Depending on if it has index.html#contact or #contact
    
    content = content.replace('href="#contact" class="btn-primary"', 'href="https://wa.me/593958831259" target="_blank" class="btn-primary"')
    content = content.replace('href="index.html#contact" class="btn-primary"', 'href="https://wa.me/593958831259" target="_blank" class="btn-primary"')
    
    with open(f, "w") as file:
        file.write(content)

print("Nav buttons updated.")
