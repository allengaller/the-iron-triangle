import re, os, glob

FILES = [
    'standards/数据安全法.md',
    'standards/证券基金经营机构信息技术管理办法.md',
    'standards/银行保险机构数据安全管理办法.md',
    'the-tam-book/standards/law-cybersecurity-2016.md',
    'the-tam-book/standards/law-data-security-2021.md',
    'the-tam-book/standards/law-pipl-2021.md',
    'the-tam-book/standards/reg-bank-insurance-data-security-2024.md',
    'the-tam-book/standards/reg-bank-insurance-it-outsourcing-2021-141.md',
    'the-tam-book/standards/reg-commercial-bank-it-risk-2009-19.md',
    'the-tam-book/standards/reg-computer-info-system-protection.md',
    'the-tam-book/standards/reg-critical-info-infrastructure-2021.md',
    'the-tam-book/standards/reg-important-system-go-live-2009-83.md',
    'the-tam-book/standards/reg-securities-fund-it-management.md',
]

CN = '一二三四五六七八九十百零〇两'
ART = re.compile(r'第([' + CN + r'\d]{1,6})条')

def cn2int(s):
    if s.isdigit():
        return int(s)
    d = {'零':0,'〇':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}
    if s == '十':
        return 10
    total, section, num = 0, 0, 0
    # handle 百/十 units
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in d:
            num = d[ch]
        elif ch == '十':
            section += (num if num else 1) * 10
            num = 0
        elif ch == '百':
            section += (num if num else 1) * 100
            num = 0
        i += 1
    return section + num

os.makedirs('.tmp/condensed', exist_ok=True)
report = []
for f in FILES:
    raw = open(f, encoding='utf-8').read()
    lines = [l.strip() for l in raw.splitlines()]
    # drop front-matter up to first '---' after title block
    body = []
    started = False
    for l in lines:
        if not started:
            if l == '---':
                started = True
            continue
        if l:
            body.append(l)
    text = '\n'.join(body)
    arts = [(m.start(), cn2int(m.group(1)), m.group(0)) for m in ART.finditer(text)]
    nums = [a[1] for a in arts]
    # longest increasing run and gaps
    gaps = []
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1 and nums[i] != nums[i-1]:
            gaps.append('%d->%d' % (nums[i-1], nums[i]))
    # unique article numbers in order
    seen = []
    for n in nums:
        if n not in seen:
            seen.append(n)
    missing = [n for n in range(1, (max(seen) if seen else 0) + 1) if n not in seen]
    report.append('=== %s | chars %d | 条命中 %d | 唯一条号 %d | max %s' % (
        f, len(text), len(arts), len(seen), max(seen) if seen else '-'))
    report.append('    首条: %s' % (arts[0][2] if arts else '-'))
    report.append('    末条: %s' % (arts[-1][2] if arts else '-'))
    report.append('    缺号: %s' % (missing[:40] if missing else '无'))
    report.append('    跳号: %s' % (gaps[:20] if gaps else '无'))
    # duplicates (same number appearing far apart)
    from collections import Counter
    c = Counter(nums)
    report.append('    重复条号: %s' % ([k for k, v in c.items() if v > 1][:30] or '无'))
    open('.tmp/condensed/' + os.path.basename(f), 'w', encoding='utf-8').write(text)
    # first/last 200 chars
    report.append('    开头: ' + text[:160].replace('\n', ' / '))
    report.append('    结尾: ' + text[-160:].replace('\n', ' / '))

open('.tmp/articles_report.txt', 'w', encoding='utf-8').write('\n'.join(report))
print('\n'.join(report))
