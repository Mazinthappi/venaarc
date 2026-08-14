import glob

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        html = f.read()
    
    html = html.replace('script.js?v=10', 'script.js?v=11')
    
    with open(file, 'w') as f:
        f.write(html)

print("Bumped cache.")
