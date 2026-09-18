from pathlib import Path
from PIL import Image
p=Path('/home/ubuntu/sanaei-subscription-template/assets/roman-hero.jpg')
im=Image.open(p).convert('RGB'); im.thumbnail((1600,1600),Image.Resampling.LANCZOS); im.save(p,format='JPEG',quality=78,optimize=True,progressive=True); print(p.stat().st_size)
