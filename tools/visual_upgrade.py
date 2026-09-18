from pathlib import Path
root=Path('/home/ubuntu/sanaei-subscription-template')
for name in ('index.html','sub.html'):
    p=root/name
    s=p.read_text()
    s=s.replace('.hero{position:relative;overflow:hidden;', '.hero{position:relative;overflow:hidden;background-image:linear-gradient(90deg,rgba(7,10,28,.25),rgba(7,10,28,.72)),url("assets/nova-hero.jpg");background-size:cover;background-position:center;')
    s=s.replace('.btn.primary{background:linear-gradient(120deg,#2570e8,#bd3bc6);', '.btn{transition:transform .2s,box-shadow .2s}.btn:hover{transform:translateY(-2px);box-shadow:0 8px 22px #42dfff33}.btn.primary{background:linear-gradient(120deg,#2570e8,#bd3bc6);')
    s=s.replace('<div class="logo">N<b>Ø</b>VA / 3X-UI</div>', '<div class="logo">✦ N<b>Ø</b>VA / 3X-UI</div>')
    s=s.replace('<a class="btn primary" href="{{.subUrl}}">دریافت اشتراک</a>', '<a class="btn primary" href="{{.subUrl}}">↳ دریافت اشتراک</a>')
    p.write_text(s)
inst=root/'install.sh'
s=inst.read_text().replace('mkdir -p "$PREFIX/assets"', '"${SUDO[@]}" mkdir -p "$PREFIX/assets"')
inst.write_text(s)
