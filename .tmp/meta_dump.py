import os, re, json

def dump(d, tag):
    rows = []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.md') or fn == 'README.md':
            continue
        p = os.path.join(d, fn)
        raw = open(p, encoding='utf-8', errors='replace').read()
        lines = raw.split('\n')
        # front matter block or leading key: value lines
        head = lines[:40]
        fields = []
        for ln in head:
            m = re.match(r'^\s*(?:[-*]\s*)?(?:\|\s*)?\**([^|:*]{2,20})\**\s*[:：]\s*(.+?)\s*\|?\s*$', ln)
            if m and not m.group(2).startswith('---'):
                k, v = m.group(1).strip(), m.group(2).strip()
                if k in ('标准号','标准名称','文件名称','名称','文号','发布机构','发布日期','实施日期','实施时间','发布状态','状态','标准类别','来源','链接','官方链接','归口单位','代替标准','被代替','备注','版本','页数','全文页数','文档页数','来源网站','获取日期','施行日期','公布日期','效力','效力状态','适用','正文'):
                    fields.append(f'{k}={v}')
        # title
        title = ''
        for ln in lines:
            if ln.startswith('# '):
                title = ln[2:].strip(); break
        body = raw
        # strip front matter
        if body.startswith('---'):
            i = body.find('\n---', 3)
            if i > 0:
                body = body[i+4:]
        body_chars = len(re.sub(r'\s', '', body))
        arts = len(set(re.findall(r'第[一二三四五六七八九十百零〇\d]{1,6}条', body)))
        rows.append({'file': fn, 'title': title, 'bytes': len(raw.encode()), 'body_chars': body_chars,
                     'unique_artifacts': arts, 'fields': fields})
    print('=== %s ===' % tag)
    for r in rows:
        print(f"### {r['file']} | {r['bytes']}B | 正文{r['body_chars']}字 | 条号{r['unique_artifacts']} | 标题: {r['title']}")
        if r['fields']:
            print('    ' + ' ; '.join(r['fields']))
    print()

dump('/Users/allengaller/Documents/GitHub/allengaller/the-tam-book/standards', 'ROOT standards/')
dump('/Users/allengaller/Documents/GitHub/allengaller/the-tam-book/the-tam-book/standards', 'NESTED the-tam-book/standards/')
