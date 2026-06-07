const counters = document.querySelectorAll('.stat-number');
const speed = 200; 

const startCounters = () => {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const inc = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 15);
            } else {
                counter.innerText = target + (target === 100 ? '%' : '');
            }
        };
        updateCount();
    });
};

const observer = new IntersectionObserver((entries) => {
    if(entries[0].isIntersecting) {
        startCounters();
        observer.disconnect(); 
    }
}, { threshold: 0.5 });

const statsSection = document.querySelector('.stats-section');
if (statsSection) observer.observe(statsSection);







document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu-wrapper');

    menuToggle.addEventListener('click', () => {
        menuToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
        
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });

    const navLinks = document.querySelectorAll('.nav-links a, .header-phone');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            menuToggle.classList.remove('active');
            navMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-links a");

    navLinks.forEach(link => {
        const linkPath = new URL(link.href, window.location.origin).pathname;
        
        if (currentUrl === linkPath || currentUrl.endsWith(linkPath)) {
            link.classList.add("active");
        }
    });
});