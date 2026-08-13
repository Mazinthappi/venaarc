// Preloader & Loading Animation #1 (Solar Panel Loader)
const preloader = document.getElementById('preloader');
const loaderPerc = document.getElementById('loader-perc');
const btnReplay = document.getElementById('btn-replay');

let loaderInterval;

function startLoaderAnimation() {
    if (!preloader || !loaderPerc) return;

    preloader.classList.remove('fade-out');
    let count = 0;
    loaderPerc.innerText = '0%';

    clearInterval(loaderInterval);
    loaderInterval = setInterval(() => {
        count += 4;
        if (count <= 100) {
            loaderPerc.innerText = count + '%';
        } else {
            clearInterval(loaderInterval);
            setTimeout(() => {
                preloader.classList.add('fade-out');
            }, 150);
        }
    }, 25); // Faster 1-second total loading time
}

// Initial preloader run
window.addEventListener('load', () => {
    startLoaderAnimation();
});

// Replay Preloader Button Click
if (btnReplay) {
    btnReplay.addEventListener('click', () => {
        startLoaderAnimation();
    });
}

// Day / Night Mode Toggle
const themeToggle = document.getElementById('theme-toggle');
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('day-mode');
        const icon = themeToggle.querySelector('i');
        if (document.body.classList.contains('day-mode')) {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    });
}

// PREMIUM FLOATING ROUNDED TRANSFORMING NAVBAR
const header = document.getElementById('header');
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('section[id]');

function handleNavbarScrollTransformation() {
    const scrollPos = window.scrollY;

    // Continuous progress between 0 and 200px scroll
    const progress = Math.min(1, Math.max(0, scrollPos / 200));

    if (header && window.innerWidth > 992) {
        if (scrollPos > 30) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Fluid continuous interpolation (94% width -> 78% width; 20px top -> 10px top)
        const widthPercent = 94 - (progress * 16);
        const topPx = 20 - (progress * 10);
        header.style.width = `${widthPercent}%`;
        header.style.top = `${topPx}px`;
    }

    // Active section scroll spy logic
    let currentSectionId = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 160;
        const sectionHeight = section.offsetHeight;
        if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
            currentSectionId = section.getAttribute('id');
        }
    });

    if (currentSectionId) {
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    }
}

window.addEventListener('scroll', handleNavbarScrollTransformation);

// CINEMATIC 3D SOLAR SCROLL JOURNEY RENDERER (CLEAN 3-SCENE FLOW)
const journeyWrapper = document.getElementById('journey');
const cinematicCanvas = document.getElementById('cinematic-canvas');

const sceneStepLbl = document.getElementById('scene-step-lbl');
const sceneTitleTxt = document.getElementById('scene-title-txt');
const sceneDescTxt = document.getElementById('scene-desc-txt');
const sceneStatTxt = document.getElementById('scene-stat-txt');
const sceneProgressFill = document.getElementById('scene-progress-fill');

const indicators = [
    document.getElementById('ind-1'),
    document.getElementById('ind-2'),
    document.getElementById('ind-3')
];

if (journeyWrapper && cinematicCanvas) {
    const cctx = cinematicCanvas.getContext('2d');
    let cWidth, cHeight;

    function resizeCinematicCanvas() {
        cWidth = cinematicCanvas.width = journeyWrapper.querySelector('.cinematic-sticky-box').clientWidth;
        cHeight = cinematicCanvas.height = journeyWrapper.querySelector('.cinematic-sticky-box').clientHeight;
    }
    window.addEventListener('resize', resizeCinematicCanvas);
    resizeCinematicCanvas();

    const scenesData = [
        {
            step: "SCENE 1 OF 3",
            title: "Scene 1: The Sunrise",
            desc: "The journey begins as a warm, radiant horizon glow illuminates the landscape in dusk-to-dawn transition.",
            stat: "<i class='fa-solid fa-sun'></i> Solar Irradiance: 1,000 W/m²"
        },
        {
            step: "SCENE 2 OF 3",
            title: "Scene 2: Energy Harvest & Storage",
            desc: "Photovoltaic technology converts solar radiation into DC electricity, feeding high-efficiency storage batteries.",
            stat: "<i class='fa-solid fa-bolt'></i> Power Generation: 1.2 MW Generated"
        },
        {
            step: "SCENE 3 OF 3",
            title: "Scene 3: Sustainable Future",
            desc: "Clean, reliable solar power energizes residential homes and commercial infrastructure with zero emissions.",
            stat: "<i class='fa-solid fa-leaf'></i> Carbon Reduction: 4,500 Tons CO₂ Saved"
        }
    ];

    function renderCinematicFrame(progress) {
        cctx.clearRect(0, 0, cWidth, cHeight);

        // Clamp progress
        const p = Math.max(0, Math.min(1, progress));
        if (sceneProgressFill) {
            sceneProgressFill.style.width = (p * 100) + '%';
        }

        // Determine scene index (0 to 2 for 3 scenes)
        const sceneIndex = Math.min(2, Math.floor(p * 3));

        // Update Text Cards and Step Indicators
        indicators.forEach((ind, i) => {
            if (ind) {
                if (i === sceneIndex) ind.classList.add('active');
                else ind.classList.remove('active');
            }
        });

        const currentData = scenesData[sceneIndex];
        if (currentData && sceneStepLbl && sceneStepLbl.innerText !== currentData.step) {
            sceneStepLbl.innerText = currentData.step;
            sceneTitleTxt.innerText = currentData.title;
            sceneDescTxt.innerText = currentData.desc;
            sceneStatTxt.innerHTML = currentData.stat;
        }

        // Clean Dark Background Sky Gradient matching Venaarc brand
        const skyGradient = cctx.createLinearGradient(0, 0, 0, cHeight);
        skyGradient.addColorStop(0, '#050505');
        skyGradient.addColorStop(0.5, '#0A0A0A');
        skyGradient.addColorStop(1, '#000000');

        cctx.fillStyle = skyGradient;
        cctx.fillRect(0, 0, cWidth, cHeight);

        // Ground Horizon Line
        const horizonY = cHeight * 0.75;

        // Warm Horizon Ambient Glow on Scroll
        const glowRadius = Math.min(cWidth, cHeight) * 0.65;
        const glowY = horizonY - p * 100;
        const ambientGlow = cctx.createRadialGradient(cWidth * 0.5, glowY, 10, cWidth * 0.5, glowY, glowRadius);
        ambientGlow.addColorStop(0, `rgba(230, 28, 36, ${0.2 + p * 0.3})`);
        ambientGlow.addColorStop(0.5, `rgba(245, 190, 11, ${0.1 + p * 0.2})`);
        ambientGlow.addColorStop(1, 'rgba(0, 0, 0, 0)');

        cctx.fillStyle = ambientGlow;
        cctx.fillRect(0, 0, cWidth, cHeight);
    }

    // Window Scroll Handler for Pinned Section
    window.addEventListener('scroll', () => {
        const rect = journeyWrapper.getBoundingClientRect();
        const wrapperHeight = journeyWrapper.clientHeight;
        const windowHeight = window.innerHeight;

        const scrollDist = -rect.top;
        const maxScroll = wrapperHeight - windowHeight;
        const progress = scrollDist / maxScroll;

        renderCinematicFrame(progress);
    });

    // Initial Frame
    renderCinematicFrame(0);
}

// Mobile Menu Toggle
const mobileToggle = document.querySelector('.mobile-toggle');
const navMenu = document.querySelector('.nav-menu');

if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        const icon = mobileToggle.querySelector('i');
        if (navMenu.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-xmark');
        } else {
            icon.classList.remove('fa-xmark');
            icon.classList.add('fa-bars');
        }
    });

    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileToggle.querySelector('i').classList.remove('fa-xmark');
            mobileToggle.querySelector('i').classList.add('fa-bars');
        });
    });
}

// Statistics Counter Animation
const counters = document.querySelectorAll('.counter');
let hasCounted = false;

const animateCounters = () => {
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const duration = 2000;
        const increment = target / (duration / 16);

        let current = 0;
        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.innerText = Math.ceil(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.innerText = target;
            }
        };
        updateCounter();
    });
};

// Battery Charging Dynamic Percentage Animation
const liveBatteryPerc = document.getElementById('live-battery-perc');
if (liveBatteryPerc) {
    let batteryVal = 5;
    setInterval(() => {
        batteryVal += 2;
        if (batteryVal > 100) batteryVal = 5;
        liveBatteryPerc.innerText = batteryVal + '%';
    }, 50);
}

// Scroll Triggered Viewport Animations
const scrollElements = document.querySelectorAll('.scroll-animate');

const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
            if (entry.target.classList.contains('stat-item') && !hasCounted) {
                animateCounters();
                hasCounted = true;
            }
        }
    });
}, { threshold: 0.15 });

scrollElements.forEach(el => scrollObserver.observe(el));

// Testimonial Slider
const track = document.querySelector('.testimonial-track');
const cards = document.querySelectorAll('.testimonial-card');
const prevBtn = document.getElementById('prevTestimonial');
const nextBtn = document.getElementById('nextTestimonial');

let currentIndex = 0;

if (track && cards.length > 0 && prevBtn && nextBtn) {
    const updateSlider = () => {
        track.style.transform = `translateX(-${currentIndex * 100}%)`;
    };

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % cards.length;
        updateSlider();
    });

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + cards.length) % cards.length;
        updateSlider();
    });
}

// FAQ Accordion
const accordionItems = document.querySelectorAll('.accordion-item');

accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');

    header.addEventListener('click', () => {
        const currentActive = document.querySelector('.accordion-item.active');
        if (currentActive && currentActive !== item) {
            currentActive.classList.remove('active');
            currentActive.querySelector('.accordion-content').style.maxHeight = null;
        }

        item.classList.toggle('active');
        const content = item.querySelector('.accordion-content');

        if (item.classList.contains('active')) {
            content.style.maxHeight = content.scrollHeight + 40 + "px";
        } else {
            content.style.maxHeight = null;
        }
    });
});

// Floating Solar Energy Particle Canvas Effect
const canvas = document.getElementById('particles-canvas');
if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height;

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    class Particle {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.size = Math.random() * 3 + 1;
            this.speedX = Math.random() * 1 - 0.5;
            this.speedY = Math.random() * -1 - 0.2;
            this.alpha = Math.random() * 0.6 + 0.2;
            this.color = Math.random() > 0.5 ? '#E61C24' : '#F5BE0B';
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.y < 0 || this.x < 0 || this.x > width) {
                this.reset();
                this.y = height + 10;
            }
        }

        draw() {
            ctx.save();
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.shadowBlur = 8;
            ctx.shadowColor = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }
    }

    const particles = [];
    for (let i = 0; i < 40; i++) {
        particles.push(new Particle());
    }

    function animateParticles() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animateParticles);
    }
    animateParticles();
}
