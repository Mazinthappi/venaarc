// Preloader & Loading Animation #1 (Solar Panel Loader)
const preloader = document.getElementById('preloader');
const loaderPerc = document.getElementById('loader-perc');
const btnReplay = document.getElementById('btn-replay');

let loaderInterval;


function startLoaderAnimation() {
    if (!preloader || !loaderPerc) return;

    preloader.style.display = 'flex';
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
                setTimeout(() => {
                    preloader.style.display = 'none';
                }, 300);
            }, 150);
        }
    }, 25);
}

// Page Reveal Logic
window.addEventListener('load', () => {
    const miniLoader = document.getElementById('mini-loader');
    
    if (document.getElementById('preloader')) {
        // We are on index.html, let the big loader handle it
        if(miniLoader) miniLoader.style.display = 'none';
        startLoaderAnimation();
    } else {
        // We are on an inner page, hide the mini loader
        if(miniLoader) {
            setTimeout(() => {
                miniLoader.classList.add('fade-out');
            }, 300); // Show mini loader for 300ms before revealing page
        }
    }
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

// Page Transition Logic for Navbar Links (Mini Loader)
document.querySelectorAll('.nav-menu a.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('#') && href !== window.location.pathname.split('/').pop()) {
            e.preventDefault();
            const miniLoader = document.getElementById('mini-loader');
            if(miniLoader) {
                miniLoader.style.display = 'flex';
                miniLoader.classList.remove('fade-out');
                miniLoader.style.visibility = 'visible';
                miniLoader.style.opacity = '1';
            }
            
            setTimeout(() => {
                window.location.href = href;
            }, 300); // Wait for mini-loader to fade in
        }
    });
});

// INTERACTIVE SOLAR TIMELINE SCRIPT
const timelineWrapper = document.querySelector('.timeline-wrapper');
const timelineSteps = document.querySelectorAll('.timeline-step');
const progressFill = document.getElementById('timeline-progress-fill');

if (timelineWrapper && timelineSteps.length > 0) {
    window.addEventListener('scroll', () => {
        const viewportCenter = window.innerHeight / 2;
        let activeIndex = -1;

        timelineSteps.forEach((step, index) => {
            const rect = step.getBoundingClientRect();
            const stepCenter = rect.top + rect.height / 2;
            
            // Check if step is above or at center
            if (stepCenter < viewportCenter + 150) {
                activeIndex = index;
            }
        });

        timelineSteps.forEach((step, index) => {
            step.classList.remove('active', 'passed');
            if (index === activeIndex) {
                step.classList.add('active');
            } else if (index < activeIndex) {
                step.classList.add('passed');
            }
        });

        // Calculate line fill
        if (activeIndex >= 0) {
            const activeStep = timelineSteps[activeIndex];
            const wrapperRect = timelineWrapper.getBoundingClientRect();
            const activeStepRect = activeStep.getBoundingClientRect();
            
            // progress is from top of wrapper to center of active step
            const fillHeight = (activeStepRect.top + activeStepRect.height / 2) - wrapperRect.top;
            const totalHeight = wrapperRect.height;
            let percentage = (fillHeight / totalHeight) * 100;
            
            if (percentage < 0) percentage = 0;
            if (percentage > 100) percentage = 100;
            
            if (progressFill) {
                progressFill.style.height = `${percentage}%`;
            }
        } else {
            if (progressFill) progressFill.style.height = `0%`;
        }
    });
    
    // Initial trigger
    window.dispatchEvent(new Event('scroll'));
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

const resetCounters = () => {
    counters.forEach(counter => {
        counter.innerText = '0';
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
            if (entry.target.id === 'stats-container' && !entry.target.dataset.hasCounted) {
                animateCounters();
                entry.target.dataset.hasCounted = 'true';
            }
        } else {
            entry.target.classList.remove('animated');
            if (entry.target.id === 'stats-container') {
                resetCounters();
                entry.target.dataset.hasCounted = '';
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

// TN Solar Bill Calculator Logic
(function() {
  const billAmtInput = document.getElementById('billAmt');
  const cycleSelect = document.getElementById('cycle');
  if (!billAmtInput || !cycleSelect) return;

  var slabs = [
    [0, 100, 0],
    [100, 400, 4.70],
    [400, 500, 6.30],
    [500, 600, 8.40],
    [600, 800, 9.45],
    [800, 1000, 10.50],
    [1000, Infinity, 11.55]
  ];

  var COST_PER_KW = 70000;
  var MAX_KW = 10;

  function subsidyFor(kw) {
    if (kw <= 1) return 30000;
    if (kw === 2) return 60000;
    return 78000;
  }

  function slabBill(units) {
    var bill = 0, remaining = units;
    for (var i = 0; i < slabs.length; i++) {
      var lo = slabs[i][0], hi = slabs[i][1], rate = slabs[i][2];
      var band = Math.min(remaining, hi - lo);
      if (band <= 0) break;
      bill += band * rate;
      remaining -= band;
    }
    return bill;
  }

  function unitsFromBill(targetBill) {
    if (targetBill <= 0) return 0;
    var lo = 0, hi = 5000;
    for (var i = 0; i < 40; i++) {
      var mid = (lo + hi) / 2;
      if (slabBill(mid) < targetBill) lo = mid; else hi = mid;
    }
    return Math.round((lo + hi) / 2);
  }

  function sizeSolar(monthlyUnits) {
    var unitsPerKwMonth = 150;
    var kwNeeded = monthlyUnits / unitsPerKwMonth;
    var kw = Math.ceil(kwNeeded);
    if (kw < 1) kw = 1;
    if (kw > MAX_KW) kw = MAX_KW;
    return kw;
  }

  function costFor(kw) {
    return kw * COST_PER_KW;
  }

  function fmt(n) {
    return '₹' + Math.round(n).toLocaleString('en-IN');
  }

  function recompute() {
    var bill = parseFloat(document.getElementById('billAmt').value) || 0;
    var cycleMonths = parseInt(document.getElementById('cycle').value, 10);

    var units = unitsFromBill(bill);
    var monthlyUnits = units / cycleMonths;

    document.getElementById('unitsOut').textContent = units.toLocaleString('en-IN');
    document.getElementById('unitsMonthly').textContent = '(' + Math.round(monthlyUnits).toLocaleString('en-IN') + ' / month)';

    var kw = sizeSolar(monthlyUnits);
    var cost = costFor(kw);
    var subsidy = subsidyFor(kw);
    var net = cost - subsidy;

    var annualBill = slabBill(monthlyUnits) * 12;
    var annualSavings = annualBill;
    var payback = annualSavings > 0 ? net / annualSavings : 0;

    document.getElementById('kwOut').textContent = kw + ' kW';
    document.getElementById('saveOut').textContent = fmt(annualSavings);
    document.getElementById('costOut').textContent = fmt(cost);
    document.getElementById('subOut').textContent = '-' + fmt(subsidy);
    document.getElementById('netOut').textContent = fmt(net);
    document.getElementById('paybackOut').textContent = (payback > 0 ? payback.toFixed(1) : '0') + ' yrs';
  }

  billAmtInput.addEventListener('input', recompute);
  cycleSelect.addEventListener('change', recompute);
  recompute();
})();
