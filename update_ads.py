import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/9c325edb11444b981f05c125df461966"></script>
<script data-cfasync="false" src="https://bauval.org/14/0abc88f2dd802abd1742a1e270b29f49"></script>
<script>
  atOptions = {
    'key' : 'e097430372913e471a35d79a13ceb4d2',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/e097430372913e471a35d79a13ceb4d2"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-9c325edb11444b981f05c125df461966"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'classes.html', 'builds.html', 'companions.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if 'e097430372913e471a35d79a13ceb4d2' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-9c325edb11444b981f05c125df461966' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')