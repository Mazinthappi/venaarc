import glob
import re

# 1. Update style.css
with open('style.css', 'r') as f:
    css = f.read()

# Remove slow opacity transition
css = css.replace('opacity: 0;\n    transition: background-color 0.5s ease, color 0.5s ease, opacity 0.8s ease-in-out;', 'transition: background-color 0.5s ease, color 0.5s ease;')
css = re.sub(r'body\.page-entered\s*\{\s*opacity:\s*1;\s*\}\s*body\.page-exiting\s*\{\s*opacity:\s*0;\s*\}', '', css)

# Add mini-loader CSS
if '#mini-loader' not in css:
    mini_loader_css = """
/* Mini Loader */
#mini-loader {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: var(--bg-darker);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9998;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}

#mini-loader.fade-out {
    opacity: 0;
    visibility: hidden;
}

.spinner {
    width: 40px;
    height: 40px;
    border: 3px solid rgba(230, 28, 36, 0.2);
    border-top: 3px solid var(--primary-red);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
"""
    css += mini_loader_css

with open('style.css', 'w') as f:
    f.write(css)


# 2. Update all HTML files
mini_loader_html = '\n    <div id="mini-loader"><div class="spinner"></div></div>'
for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    if 'id="mini-loader"' not in html:
        html = html.replace('<body>', f'<body>{mini_loader_html}')
        # Cache bust
        html = html.replace('script.js?v=9', 'script.js?v=10')
        html = html.replace('script.js?v=8', 'script.js?v=10')
        with open(file, 'w') as f:
            f.write(html)


# 3. Update script.js
with open('script.js', 'r') as f:
    js = f.read()

# Replace transition logic with mini-loader logic
# First, update the navbar click listener
old_nav_logic = """// Page Transition Logic for Navbar Links
document.querySelectorAll('.nav-menu a.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        // Only trigger transition for actual page links, not hash links
        if (href && !href.startsWith('#') && href !== window.location.pathname.split('/').pop()) {
            e.preventDefault();
            document.body.classList.remove('page-entered');
            document.body.classList.add('page-exiting');
            
            setTimeout(() => {
                window.location.href = href;
            }, 800); // 800ms CSS transition duration
        }
    });
});"""

new_nav_logic = """// Page Transition Logic for Navbar Links (Mini Loader)
document.querySelectorAll('.nav-menu a.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && !href.startsWith('#') && href !== window.location.pathname.split('/').pop()) {
            e.preventDefault();
            const miniLoader = document.getElementById('mini-loader');
            if(miniLoader) {
                miniLoader.classList.remove('fade-out');
                miniLoader.style.visibility = 'visible';
                miniLoader.style.opacity = '1';
            }
            
            setTimeout(() => {
                window.location.href = href;
            }, 300); // Wait for mini-loader to fade in
        }
    });
});"""
js = js.replace(old_nav_logic, new_nav_logic)

# Update page load logic
old_load_logic = """// Smooth Page Reveal
window.addEventListener('load', () => {
    document.body.classList.add('page-entered');
    startLoaderAnimation();
});"""

new_load_logic = """// Page Reveal Logic
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
});"""
js = js.replace(old_load_logic, new_load_logic)

with open('script.js', 'w') as f:
    f.write(js)

print("Swapped slow transition for mini loader.")
