from pathlib import Path
p=Path('/home/ubuntu/sanaei-subscription-template/install.sh')
s=p.read_text()
s=s.replace('REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"', 'REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"\nASSET_RAW="${SUB_THEME_ASSET_BASE:-https://github.com/jashoahmlin2/sanaei-subscription-template/raw/refs/heads/main}"')
s=s.replace('"$REPO_RAW/assets/nova-hero.jpg"', '"$ASSET_RAW/assets/nova-hero.jpg"')
p.write_text(s)
