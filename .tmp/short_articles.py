import re, os, glob

CN = '一二三四五六七八九十百零〇两'
ART = re.compile(r'第([' + CN + r'\d]{1,6})条')

def cn2int(s):
    if s.isdigit():
        return int(s)
    d = {'零':0,'〇':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
    if s == '十':
        return 10
    total = 0; num = 0
    for ch in s:
        if ch in d:
            num = d[ch]
        elif ch == '十':
            total += (num if num else 1) * 10; num = 0
        elif ch == '百':
            total += (num if num else 1) * 100; num = 0
    return total + num

out = []
for f in sorted(glob.glob('.tmp/condensed/*.md')):
    text = open(f, encoding='utf-8').read()
    ms = list(ART.finditer(text))
    out.append('\n=== %s | 条数 %d' % (os.path.basename(f), len(ms)))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        body = text[m.end():end].strip()
        n = cn2int(m.group(1))
        if len(body) < 30:
            out.append('  [短/空] %s (n=%d) len=%d :: %s' % (m.group(0), n, len(body), body[:60].replace('\n', ' ')))
    # trailing 80 chars
    out.append('  [尾部] ' + text[-80:].replace('\n', ' '))
open('.tmp/short_articles.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('ok')
