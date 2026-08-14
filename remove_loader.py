import glob
import re

html_files = glob.glob('*.html')

# Regex to match the preloader div and its contents completely
preloader_pattern = re.compile(r'<!-- 1\. Solar Panel Loading Animation \(Preloader Overlay\) -->.*?</div>\s*<!-- Floating Replay Preloader Button -->.*?</button>', re.DOTALL)

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove preloader and replay button
    content = re.sub(preloader_pattern, '', content)
    
    # Update script version to bust cache
    content = content.replace('script.js?v=8', 'script.js?v=9')
    
    with open(file, 'w') as f:
        f.write(content)

# Update script.js to just handle smooth fade-in
with open('script.js', 'r') as f:
    js = f.read()

# Replace startLoaderAnimation entirely
new_js = re.sub(r'function startLoaderAnimation\(\).*?// Initial preloader run\nwindow\.addEventListener\(\'load\', \(\) => \{\n.*?\}\);\n\n// Replay Preloader Button Click\nif \(btnReplay\) \{.*?\}\n', 
                "// Smooth Page Reveal\nwindow.addEventListener('load', () => {\n    document.body.classList.add('page-entered');\n});\n", js, flags=re.DOTALL)

with open('script.js', 'w') as f:
    f.write(new_js)

print("Completely removed preloader from HTML and updated JS logic.")
