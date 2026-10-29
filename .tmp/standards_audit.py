import os, re, glob, sys

DIRS = ['standards', 'the-tam-book/standards']
NOISE = ['上一篇', '下一篇', '当前位置', '打印本页', '扫一扫', '分享到', '责任编辑',
         '浏览次数', '网站地图', '主办单位', 'ICP备', '版权所有', '关注我们',
         '微信扫一扫', '手机版', '无障碍', '简体', '繁體']
TRUNC = ['（以下无正文）', '以下无正文', '……', '略', 'TODO', '待补', '未完待续']

out = []
for d in DIRS:
    out.append('#' * 25 + ' ' + d)
    for f in sorted(glob.glob(d + '/*.md')):
        if f.endswith('README.md'):
            continue
        t = open(f, encoding='utf-8', errors='replace').read()
        lines = t.splitlines()
        out.append('\n=== %s | bytes %d | lines %d' % (f, len(t.encode()), len(lines)))
        for l in lines[:16]:
            out.append('    ' + l[:130])
        # head chars
        out.append('    [tail] ' + ' / '.join(x[:60] for x in lines[-3:]))
open('.tmp/standards_heads.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written', len(out))
