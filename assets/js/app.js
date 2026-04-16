// Inicializar iconos de Lucide
lucide.createIcons();

// Custom cursor o lógicas adicionales pueden ir aquí
console.log("Agency Portfolio Initialized. Elevating Standards.");

// Simple intersection observer for fade-up animations (to be expanded)
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.project-card').forEach(el => {
    el.style.opacity = 0;
    el.style.transform = 'translateY(50px)';
    el.style.transition = 'all 0.8s cubic-bezier(0.19, 1, 0.22, 1)';
    observer.observe(el);
});

// Lógica para el fondo del Header al hacer scroll
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

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
