import pathlib, re
text = pathlib.Path('index.html').read_text('utf-8')
match = re.search(r'class="profile-picture".*?src="(data:image/[^"]+)"', text, re.S)
if match:
    pathlib.Path('profile_image.txt').write_text(match.group(1), encoding='utf-8')
else:
    pathlib.Path('profile_image.txt').write_text('NOTFOUND', encoding='utf-8')
