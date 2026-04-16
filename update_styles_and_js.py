import re

## 1. Updating style.css
with open("assets/css/style.css", "r") as file:
    css = file.read()

# Fix desktop header flex
css = css.replace('.site-header {\n    display: flex;\n    justify-content: space-between;', '.site-header {\n    display: flex;\n    align-items: center;')

# Add auto margin to logo to push others to the right
css = css.replace('.logo {\n    font-family: var(--font-heading);', '.logo {\n    font-family: var(--font-heading);\n    margin-right: auto;')

# Inject base styling for mobile controls & nav before the mobile media query
base_styles = """
.mobile-controls { display: flex; align-items: center; }
.hamburger-btn { display: none; background: none; border: none; color: white; cursor: pointer; padding: 0.5rem; }
#main-nav { display: flex; gap: 2rem; align-items: center; }
#main-nav a.nav-link { font-size: 1.2rem; }
"""
if ".hamburger-btn" not in css:
    css = css.replace('/* ==============================================\n   MOBILE RESPONSIVENESS', base_styles + '\n/* ==============================================\n   MOBILE RESPONSIVENESS')

# Rewrite the Mobile Nav CSS
new_mobile_nav = """    /* Header & Nav */
    .site-header { padding: 1.5rem var(--padding-global); }
    .hamburger-btn { display: block; }
    #main-nav { 
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: #0a0a0a; flex-direction: column; justify-content: center;
        z-index: 95; opacity: 0; pointer-events: none;
        transform: translateY(-20px); transition: all 0.4s var(--ease-out-expo);
    }
    #main-nav.active { opacity: 1; pointer-events: auto; transform: translateY(0); }
    #main-nav a.nav-link { font-size: 3rem; font-family: var(--font-heading); font-weight: 700; }
    .mobile-controls { z-index: 100; }"""

# Using regex to replace the old mobile nav block since we have modified it a few times
css = re.sub(r'/\* Header & Nav \*/.*?/\* Hero Adjustments \*/', new_mobile_nav + '\n    \n    /* Hero Adjustments */', css, flags=re.DOTALL)

with open("assets/css/style.css", "w") as file:
    file.write(css)


## 2. Updating app.js
with open("assets/js/app.js", "r") as file:
    js = file.read()

hamburger_logic = """
    // Hamburger Menu Logic
    const menuBtn = document.getElementById("menu-toggle");
    const mainNav = document.getElementById("main-nav");
    if(menuBtn && mainNav) {
        menuBtn.addEventListener("click", () => {
            const isActive = mainNav.classList.toggle("active");
            if(window.lucide) {
                menuBtn.innerHTML = isActive ? "<i data-lucide='x'></i>" : "<i data-lucide='menu'></i>";
                lucide.createIcons();
            }
        });
        
        // Close menu on link click
        document.querySelectorAll("#main-nav a").forEach(link => {
            link.addEventListener("click", () => {
                mainNav.classList.remove("active");
                if(window.lucide){
                    menuBtn.innerHTML = "<i data-lucide='menu'></i>";
                    lucide.createIcons();
                }
            });
        });
    }
"""

if "menuBtn.addEventListener" not in js:
    js = js + hamburger_logic
    with open("assets/js/app.js", "w") as file:
        file.write(js)

print("CSS and JS updated!")
