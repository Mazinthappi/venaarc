import re

loader_html = """
    <!-- 1. Solar Panel Loading Animation (Preloader Overlay) -->
    <div id="preloader">
        <svg class="solar-loader-svg" viewBox="0 0 200 200">
            <!-- Sun with rotating rays -->
            <g class="sun-rays-group">
                <circle cx="100" cy="60" r="22" fill="#F5BE0B" filter="drop-shadow(0 0 10px #F5BE0B)" />
                <!-- Sun rays -->
                <line x1="100" y1="25" x2="100" y2="15" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="100" y1="95" x2="100" y2="105" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="65" y1="60" x2="55" y2="60" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="135" y1="60" x2="145" y2="60" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="75" y1="35" x2="68" y2="28" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="125" y1="85" x2="132" y2="92" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="75" y1="85" x2="68" y2="92" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
                <line x1="125" y1="35" x2="132" y2="28" stroke="#F5BE0B" stroke-width="4" stroke-linecap="round" />
            </g>

            <!-- Light particles travelling from Sun to Solar Panel -->
            <path class="light-particle" d="M100 82 L100 135" stroke="#F5BE0B" stroke-width="3" fill="none" />
            <path class="light-particle" d="M80 75 L70 135" stroke="#E63946" stroke-width="2" fill="none" />
            <path class="light-particle" d="M120 75 L130 135" stroke="#FF6B00" stroke-width="2" fill="none" />

            <!-- Solar Panel Grid (Illuminating cells one by one) -->
            <g class="panel-grid-group">
                <polygon points="50,140 150,140 165,180 35,180" fill="#1C1121" stroke="#382542" stroke-width="2" />
                <polygon class="cell-1" points="53,142 83,142 80,158 48,158" />
                <polygon class="cell-2" points="86,142 114,142 114,158 83,158" />
                <polygon class="cell-3" points="117,142 147,142 152,158 117,158" />
                <polygon class="cell-4" points="46,161 80,161 77,178 38,178" />
                <polygon class="cell-5" points="83,161 114,161 114,178 80,178" />
                <polygon class="cell-6" points="117,161 154,161 162,178 117,178" />
            </g>
        </svg>
        <div class="loader-text">HARNESSING SOLAR ENERGY...</div>
        <div class="energy-progress-container">
            <div class="energy-progress-bar"></div>
        </div>
        <div class="loader-percentage" id="loader-perc">0%</div>
    </div>

    <!-- Floating Replay Preloader Button -->
    <button class="btn-replay-loader" id="btn-replay" title="Replay Solar Panel Loading Animation">
        <i class="fa-solid fa-rotate-right"></i> Play Loader Animation
    </button>
"""

with open('index.html', 'r') as f:
    content = f.read()

if 'id="preloader"' not in content:
    # Insert after <canvas id="particles-canvas"></canvas>
    content = content.replace('<canvas id="particles-canvas"></canvas>', '<canvas id="particles-canvas"></canvas>\n' + loader_html)
    with open('index.html', 'w') as f:
        f.write(content)

# Now restore script.js loader logic
with open('script.js', 'r') as f:
    js = f.read()

js_restore = """// Preloader & Loading Animation #1 (Solar Panel Loader)
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

// Smooth Page Reveal
window.addEventListener('load', () => {
    document.body.classList.add('page-entered');
    startLoaderAnimation();
});

// Replay Preloader Button Click
if (btnReplay) {
    btnReplay.addEventListener('click', () => {
        startLoaderAnimation();
    });
}
"""

# Replace the single // Smooth Page Reveal block with the full logic
js = re.sub(r'// Smooth Page Reveal\nwindow\.addEventListener\(\'load\', \(\) => \{\n    document\.body\.classList\.add\(\'page-entered\'\);\n\}\);\n', js_restore, js)

with open('script.js', 'w') as f:
    f.write(js)

print("Restored loader to index.html ONLY.")
