document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); 

        const formData = {
            first_name: document.getElementById('first_name').value,
            last_name: document.getElementById('last_name').value,
            email: document.getElementById('email').value,
            phone: `${document.getElementById('phone_1').value}${document.getElementById('phone_2').value}${document.getElementById('phone_3').value}`,
            // subject: document.getElementById('subject').value,
            message: document.getElementById('message').value
        };

        try {
            const response = await fetch('https://singing-aflutter-encrust.ngrok-free.devsubmit-contact', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                alert('✅ Успішно! Повідомлення надіслано в базу та адміну в ТГ.');
                form.reset(); 
            } else {
                const result = await response.json();
                
                if (response.status === 422 && Array.isArray(result.detail)) {
                    let errorMessages = result.detail.map(err => {
                        if (err.loc.includes("first_name")) return "👤 Ім'я: мінімум 2 символи.";
                        if (err.loc.includes("last_name")) return "👤 Прізвище: занадто коротке.";
                        if (err.loc.includes("email")) return "📧 Email: введіть коректну адресу.";
                        if (err.loc.includes("phone")) return "📞 Номер телефону: занадто короткий (перевірте всі 3 блоки).";
                        if (err.loc.includes("message")) return "💬 Повідомлення: має бути від 5 символів.";
                        return `❓ ${err.msg}`; 
                    }).join("\n");
                    
                    alert("⚠️ Виправте помилки у формі:\n\n" + errorMessages);
                } else {
                    alert("❌ Помилка сервера: " + (result.detail || "Невідома помилка"));
                }
            }
        } catch (error) {
            console.error('Error:', error);
            alert('🔌 Сервер не відповідає. Перевір, чи запущений backend на порту 8000.');
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const phoneInputs = [
        document.getElementById('phone_1'),
        document.getElementById('phone_2'),
        document.getElementById('phone_3')
    ];

    phoneInputs.forEach((input, index) => {
        input.addEventListener('input', function() {
            if (this.value.length >= this.maxLength) {
                const nextInput = phoneInputs[index + 1];
                if (nextInput) {
                    nextInput.focus();
                }
            }
        });

        input.addEventListener('keydown', function(e) {
            if (e.key === 'Backspace' && this.value.length === 0) {
                const prevInput = phoneInputs[index - 1];
                if (prevInput) {
                    prevInput.focus();
                }
            }
        });
    });
});





// NAVIGATION MENU TOGGLE
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