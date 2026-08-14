import glob
import re

# Update index.html and others
inline_script = """
    <style>
        html.hide-loader #preloader { display: none !important; }
    </style>
    <script>
        if (localStorage.getItem('loaderShown') === 'true') {
            document.documentElement.classList.add('hide-loader');
        }
    </script>
</head>"""

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
        
    # Remove the old sessionStorage inline script
    old_script_pattern = re.compile(r'<style>\s*html\.hide-loader #preloader \{ display: none !important; \}\s*</style>\s*<script>\s*if \(sessionStorage\.getItem\(\'loaderShown\'\) === \'true\'\) \{\s*document\.documentElement\.classList\.add\(\'hide-loader\'\);\s*\}\s*</script>', re.DOTALL)
    content = re.sub(old_script_pattern, '', content)
    
    # Insert new localStorage inline script
    if 'localStorage.getItem' not in content:
        content = content.replace('</head>', inline_script)
        with open(file, 'w') as f:
            f.write(content)

print("Updated inline scripts to use localStorage.")
