from pathlib import Path

root = Path('/home/ubuntu/sanaei-subscription-template')
index = root / 'index.html'
s = index.read_text()

s = s.replace('</style></head>', '''
/* motion and chart */
.card{animation:rise .55s ease both}.card:nth-child(2){animation-delay:.08s}.card:nth-child(3){animation-delay:.16s}.card:nth-child(4){animation-delay:.24s}.bar span{animation:grow 1.2s ease-out both}.metric b{transition:color .3s}.metric b.flash{color:var(--cyan)}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}@keyframes grow{from{width:0}}@keyframes draw{to{stroke-dashoffset:0}}
@media(prefers-reduced-motion:reduce){.card,.bar span,.chart .line{animation:none}}
.chart{position:relative;height:150px;margin-top:10px;border:1px solid var(--line);border-radius:12px;background:#091523;overflow:hidden}.chart svg{width:100%;height:100%;display:block}.chart .area{fill:url(#fill)}.chart .line{fill:none;stroke:var(--cyan);stroke-width:2.5;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:600;stroke-dashoffset:600;animation:draw 1.5s ease-out forwards}.chart .gridline{stroke:#28405d;stroke-width:1;opacity:.55}.chart-labels{display:flex;justify-content:space-between;color:var(--muted);font-size:10px;margin-top:5px}.chart-value{position:absolute;top:8px;left:10px;color:var(--cyan);font:bold 12px Arial}
</style></head>''')

s = s.replace('<section class="card full"><h2>جزئیات حساب</h2>', '''<section class="card full"><h2>نمودار مصرف حجم</h2><div class="chart"><span class="chart-value" id="chartValue">--</span><svg viewBox="0 0 600 150" preserveAspectRatio="none" aria-label="نمودار مصرف"><defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#32d5ff" stop-opacity=".35"/><stop offset="1" stop-color="#32d5ff" stop-opacity="0"/></linearGradient></defs><path class="gridline" d="M0 30H600M0 75H600M0 120H600"/><path id="chartArea" class="area" d="M0 150 L0 135 L100 125 L200 115 L300 95 L400 80 L500 55 L600 35 L600 150Z"/><path id="chartLine" class="line" d="M0 135 L100 125 L200 115 L300 95 L400 80 L500 55 L600 35"/></svg></div><div class="chart-labels"><span>شروع دوره</span><span>اکنون</span></div></section><section class="card full"><h2>جزئیات حساب</h2>''')

old = "var pct=total?Math.min(100,Math.max(0,used/total*100)):0;g('bar').style.width=pct+'%';g('pct').textContent=total?pct.toFixed(1)+'٪ مصرف':'بدون محدودیت';"
new = """var pct=total?Math.min(100,Math.max(0,used/total*100)):0;g('bar').style.width=pct+'%';g('pct').textContent=total?pct.toFixed(1)+'٪ مصرف':'بدون محدودیت';g('chartValue').textContent=total?pct.toFixed(1)+'٪ مصرف':'بدون محدودیت';var points=[0,Math.max(8,pct*.18),Math.max(12,pct*.34),Math.max(18,pct*.52),Math.max(25,pct*.68),Math.max(30,pct*.84),Math.max(35,pct)].map(function(v){return (150-v*1.15).toFixed(1)});var d='M0 '+points[0]+' '+points.slice(1).map(function(y,i){return 'L'+((i+1)*100)+' '+y}).join(' ');g('chartLine').setAttribute('d',d);g('chartArea').setAttribute('d',d+' L600 150 L0 150Z');"""
if old not in s:
    raise SystemExit('target JS not found')
s = s.replace(old, new)
index.write_text(s)
(root / 'sub.html').write_text(s)
