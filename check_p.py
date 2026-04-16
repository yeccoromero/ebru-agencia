import glob, re

files = glob.glob("*.html")
for f in files:
    if "index.html" in f: continue
    
    with open(f, "r") as file:
        content = file.read()
    
    match = re.search(r'<div class="project-description">(.*?)</div>', content, re.DOTALL)
    if match:
        desc = match.group(1)
        p_count = desc.count('<p')
        if p_count > 1:
            print(f"{f} has {p_count} paragraphs in description.")
