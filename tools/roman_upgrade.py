from pathlib import Path
root=Path('/home/ubuntu/sanaei-subscription-template')
for name in ('index.html','sub.html'):
    p=root/name; s=p.read_text()
    s=s.replace('background-image:linear-gradient(90deg,rgba(7,10,28,.25),rgba(7,10,28,.72)),url("assets/nova-hero.jpg")','background-image:linear-gradient(90deg,rgba(22,8,5,.2),rgba(22,8,5,.78)),url("assets/roman-hero.jpg")')
    s=s.replace('--bg:#050816;--panel:rgba(13,19,42,.82);--panel2:#111936;--line:rgba(132,156,255,.2);--white:#f8fbff;--muted:#91a0c2;--cyan:#4deaff;--pink:#f472e8;--green:#35e0a0;--yellow:#ffd166','--bg:#120907;--panel:rgba(35,18,12,.88);--panel2:#3b2116;--line:rgba(210,157,74,.28);--white:#fff6df;--muted:#c7a982;--cyan:#e8b85b;--pink:#a73b3b;--green:#73c68e;--yellow:#ffd166')
    s=s.replace('N<b>Ø</b>VA / 3X-UI','IMPERIVM / 3X-UI')
    s=s.replace('SECURE SUBSCRIPTION · v4','ROMA AETERNA · v5')
    s=s.replace('NEXT GENERATION CONNECTION PANEL','IMPERIVM CONNECTION PORTAL')
    s=s.replace('color:#38bdf8','color:#e8b85b').replace('background:#087ba9','background:#79352b').replace('border-color:#38bdf8','border-color:#d9a74b')
    marker='<footer class="footer">'
    guide='''<section class="card wide"><div class="card-title"><h2>استفاده در نرم‌افزارها</h2><span>CLIENT GUIDE</span></div><div class="detail"><span>اندروید</span><strong>V2Box · NekoBox · Clash Meta</strong></div><div class="detail"><span>آیفون و آیپد</span><strong>Stash · Shadowrocket · FoXray</strong></div><div class="detail"><span>ویندوز و مک</span><strong>Clash Verge Rev · Hiddify · Nekoray</strong></div><div class="detail"><span>روش استفاده</span><strong>ابتدا «کپی همه» را بزنید، سپس در نرم‌افزار Import from Clipboard را انتخاب کنید.</strong></div></section>'''
    s=s.replace(marker,guide+marker)
    p.write_text(s)
inst=root/'install.sh'; s=inst.read_text().replace('nova-hero.jpg','roman-hero.jpg'); inst.write_text(s)
