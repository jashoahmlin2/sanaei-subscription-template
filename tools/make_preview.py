from pathlib import Path
import re

root=Path('/home/ubuntu/sanaei-subscription-template')
s=(root/'index.html').read_text()
# Resolve conditional template blocks for sample data before replacing scalar fields.
s=re.sub(r'\{\{if \.subTitle\}\}(.*?)\{\{else\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.isOnline\}\}(.*?)\{\{else\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.enabled\}\}(.*?)\{\{else\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.subClashUrl\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.subJsonUrl\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.announce\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
s=re.sub(r'\{\{if \.subSupportUrl\}\}(.*?)\{\{end\}\}', r'\1', s, flags=re.S)
vals={
'{{.subTitle}}':'Imperium Gold · اشتراک ویژه','{{.used}}':'4.2 GB','{{.remained}}':'15.8 GB','{{.total}}':'20 GB','{{.expire}}':'1790208000','{{.lastOnline}}':'1789765200000','{{.totalByte}}':'21474836480','{{.downloadByte}}':'3221225472','{{.uploadByte}}':'1073741824','{{.subUrl}}':'#subscription','{{.subClashUrl}}':'#clash','{{.subJsonUrl}}':'#json','{{.sId}}':'roman-demo-2026','{{.subSupportUrl}}':'#support','{{.announce}}':'اشتراک شما با موفقیت فعال است.'}
for a,b in vals.items(): s=s.replace(a,b)
s=s.replace('{{len .links}}','3')
links=''.join(f'<div class="link item"><code id="link{i}">{x}</code><button class="btn" onclick="copyOne(\'link{i}\',this)">کپی</button></div>' for i,x in enumerate(['vless://demo-uuid@example.com:443?security=tls#Rome-01','vmess://eyJhZGQiOiJleGFtcGxlLmNvbSJ9#Rome-02','trojan://demo@example.com:443?sni=example.com#Rome-03']))
s=re.sub(r'\{\{range \$i, \$link := \.links\}\}.*?\{\{else\}\}.*?\{\{end\}\}',links,s,flags=re.S)
s=s.replace('{{end}}','')
(root/'preview.html').write_text(s)
