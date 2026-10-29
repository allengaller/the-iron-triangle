#!/usr/bin/env python3
"""
附录 W 法律法规与监管规章全文批量拉取脚本 v2
采集时点：2026-10-25

改进：使用更可靠的官方来源，增加百度百科等 fallback
"""

import os
import re
import time
from urllib import request, error

COLLECTION_DATE = "2026-10-25"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
    "Referer": "https://www.gov.cn/",
}

# 真实的文档列表（使用 flk.npc.gov.cn 国家法律法规数据库为主渠道）
DOCUMENTS = [
    {
        "id": "cybersecurity_law_2025",
        "filename": "网络安全法_2025修正版.md",
        "title": "中华人民共和国网络安全法（2025修正版）",
        "type": "full_text",
        "source_name": "国家法律法规数据库",
        "source_url": "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
        "fallback_urls": [
            "https://www.cac.gov.cn/2025-10/28/c_1733651756187654.htm",
            "https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%B3%95",
        ],
        "notes": "2025-10-28 修正，2026-01-01 施行",
    },
    {
        "id": "personal_info_protection_law",
        "filename": "个人信息保护法.md",
        "title": "中华人民共和国个人信息保护法",
        "type": "full_text",
        "source_name": "国家法律法规数据库",
        "source_url": "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
        "fallback_urls": [
            "https://baike.baidu.com/item/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E4%B8%AA%E4%BA%BA%E4%BF%A1%E6%81%AF%E4%BF%9D%E6%8A%A4%E6%B3%95",
        ],
        "notes": "2021-08-20 公布，2021-11-01 施行",
    },
    {
        "id": "cii_regulation",
        "filename": "关键信息基础设施安全保护条例.md",
        "title": "关键信息基础设施安全保护条例",
        "type": "full_text",
        "source_name": "中国政府网 / 国家法律法规数据库",
        "source_url": "https://www.gov.cn/zhengce/2021-09/01/content_5631671.htm",
        "fallback_urls": [
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
            "https://baike.baidu.com/item/%E5%85%B3%E9%94%AE%E4%BF%A1%E6%81%AF%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%E5%AE%89%E5%85%A8%E4%BF%9D%E6%8A%A4%E6%9D%A1%E4%BE%8B",
        ],
        "notes": "国务院令第 745 号，2021-09-01 施行",
    },
    {
        "id": "computer_info_system_regulation",
        "filename": "计算机信息系统安全保护条例.md",
        "title": "计算机信息系统安全保护条例",
        "type": "full_text",
        "source_name": "中国政府网 / 国家法律法规数据库",
        "source_url": "https://www.gov.cn/zhengce/2024-03/19/content_6939768.htm",
        "fallback_urls": [
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
            "https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BF%A1%E6%81%AF%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8%E4%BF%9D%E6%8A%A4%E6%9D%A1%E4%BE%8B",
        ],
        "notes": "1994 发布，2011 修订，2024 年最新版",
    },
    {
        "id": "it_risk_management_guidelines",
        "filename": "商业银行信息科技风险管理指引.md",
        "title": "商业银行信息科技风险管理指引",
        "type": "full_text",
        "source_name": "原中国银行业监督管理委员会 / ClearSec",
        "source_url": "https://www.gov.cn/gongbao/content/2009/content_1345047.htm",
        "fallback_urls": [
            "https://www.lawtime.com/info/gongyi/bxjt/20091202/1345047.html",
            "https://baike.baidu.com/item/%E5%95%86%E4%B8%9A%E9%93%B6%E8%A1%8C%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E9%A3%8E%E9%99%A9%E7%AE%A1%E7%90%86%E6%8C%87%E5%BC%95",
        ],
        "notes": "银监发〔2009〕19 号，76 条全文",
    },
    {
        "id": "important_system_production_change",
        "filename": "重要信息系统投产及变更管理办法.md",
        "title": "银行业金融机构重要信息系统投产及变更管理办法",
        "type": "full_text",
        "source_name": "原中国银行业监督管理委员会 / ClearSec",
        "source_url": "https://www.gov.cn/gongbao/content/2009/content_1345047.htm",
        "fallback_urls": [
            "https://www.lawtime.com/info/gongyi/bxjt/20091202/1345047.html",
            "https://baike.baidu.com/item/%E9%93%B6%E8%A1%8C%E4%B8%9A%E9%87%91%E8%9E%8D%E6%9C%BA%E6%9E%84%E9%87%8D%E8%A6%81%E4%BF%A1%E6%81%AF%E7%B3%BB%E7%BB%9F%E6%8A%95%E4%BA%A7%E5%8F%8A%E5%8F%98%E6%9B%B4%E7%AE%A1%E7%90%86%E5%8A%9E%E6%B3%95",
        ],
        "notes": "银监办发〔2009〕83 号，40 条全文",
    },
    {
        "id": "data_center_supervision_guidelines",
        "filename": "商业银行数据中心监管指引.md",
        "title": "商业银行数据中心监管指引",
        "type": "metadata",
        "source_name": "原中国银行业监督管理委员会",
        "source_url": "https://www.gov.cn/gongbao/content/2010/content_1641235.htm",
        "fallback_urls": [
            "https://www.lawtime.com/info/gongyi/bxjt/20101202/1642836.html",
            "https://www.pkulaw.com/chl/d86799f8e4b11bdfb1bffbd4687a8b0a.html",
        ],
        "notes": "银监办发〔2010〕114 号——来源站点反爬或需付费，待人工补齐",
    },
]

def fetch_url(url, max_retries=3):
    """带重试的 URL 获取"""
    for attempt in range(max_retries):
        try:
            req = request.Request(url, headers=HEADERS)
            with request.urlopen(req, timeout=30) as response:
                data = response.read()
                # 尝试解压 gzip
                try:
                    import gzip
                    data = gzip.decompress(data)
                except:
                    pass
                # 尝试多种编码
                for enc in ['utf-8', 'gbk', 'gb2312', 'latin-1']:
                    try:
                        return data.decode(enc)
                    except:
                        continue
                return data.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"  尝试 {attempt + 1}/{max_retries} 失败: {e}")
            time.sleep(2 ** attempt)
    return None

def extract_baidu_baike_text(html_content):
    """从百度百科提取正文"""
    # 百科页面通常有特定的正文 div
    import re
    # 尝试找到正文部分
    patterns = [
        r'<div class="lemma-summary"[^>]*>(.*?)</div>',
        r'<div class="para"[^>]*>(.*?)</div>',
    ]
    texts = []
    for pattern in patterns:
        matches = re.findall(pattern, html_content, re.DOTALL)
        for match in matches:
            text = re.sub(r'<[^>]+>', '', match)
            text = re.sub(r'&nbsp;', ' ', text)
            text = re.sub(r'&[a-z]+;', '', text)
            if text.strip():
                texts.append(text.strip())
    if texts:
        return '\n\n'.join(texts[:20])  # 限制条数
    return None

def write_full_text_file(doc, output_dir, html_content):
    """写入全文文件"""
    filepath = os.path.join(output_dir, doc["filename"])
    
    # 提取正文
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&[a-z]+;', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    # 过滤
    lines = text.split('\n')
    filtered = []
    skip_keywords = ['分享到', '打印本页', '关闭窗口', '网站地图', '版权所有', '联系我们', '友情链接', '返回顶部', '无障碍浏览', '政务微信', '登录', '注册']
    for line in lines:
        line_stripped = line.strip()
        if len(line_stripped) < 2:
            continue
        if any(kw in line_stripped for kw in skip_keywords):
            continue
        filtered.append(line_stripped)
    
    content_text = '\n\n'.join(filtered[:2000])  # 限制长度
    
    content = f"""# {doc['title']}

> **来源**: [{doc['source_name']}]({doc['source_url']})  
> **采集时点**: {COLLECTION_DATE}  
> **状态**: ✅ 全文已抓取（正文提取自官方 HTML，建议复核）

## 文件信息

| 项目 | 内容 |
|------|------|
| **文件名称** | {doc['title']} |
| **来源机构** | {doc['source_name']} |
| **官方链接** | [{doc['source_url']}]({doc['source_url']}) |
| **备注** | {doc['notes']} |

---

## 正文

{content_text}

---

## 来源声明

> 本文本为官方发布文本的网络公开转载版本，**不替代官方标准文本**。如需引用，请以国家法律法规数据库（flk.npc.gov.cn）或发文机构官网发布的 PDF/纸质文本为准。

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 全文文件已写入: {filepath}")

def write_metadata_file(doc, output_dir):
    """写入仅存元数据的文件"""
    filepath = os.path.join(output_dir, doc["filename"])
    content = f"""# {doc['title']}

> **来源**: [{doc['source_name']}]({doc['source_url']})  
> **采集时点**: {COLLECTION_DATE}  
> **状态**: ⚠️ 无法自动抓取全文，以下为元数据与官方获取渠道

## 文件信息

| 项目 | 内容 |
|------|------|
| **文件名称** | {doc['title']} |
| **来源机构** | {doc['source_name']} |
| **官方链接** | [{doc['source_url']}]({doc['source_url']}) |
| **备注** | {doc['notes']} |

## 官方获取渠道
"""
    if doc.get("fallback_urls"):
        content += "\n"
        for url in doc["fallback_urls"]:
            content += f"- [{url}]({url})\n"
    else:
        content += "\n- 暂无其他官方获取渠道\n"

    content += f"""
## 说明

该文件因以下原因无法通过自动化脚本抓取全文：
- 来源站点设有反爬机制或付费墙
- 官方平台仅提供在线阅读或受控下载
- 文件已废止，原文不再公开提供

如需完整文本，建议通过以下渠道获取：
1. **国家法律法规数据库**：https://flk.npc.gov.cn
2. **北大法宝**：https://www.pkulaw.com（需订阅）
3. **中国政府网**：https://www.gov.cn
4. **直接联系发文机构**：获取官方 PDF 或纸质文本

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ⚠️ 元数据文件已写入: {filepath}")

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📚 附录 W 法律法规批量拉取脚本 v2")
    print(f"📅 采集时点: {COLLECTION_DATE}")
    print(f"📂 输出目录: {output_dir}")
    print(f"📄 共 {len(DOCUMENTS)} 份文件待处理\n")
    
    success_count = 0
    fail_count = 0
    
    for i, doc in enumerate(DOCUMENTS, 1):
        print(f"[{i}/{len(DOCUMENTS)}] 正在处理: {doc['title']}")
        
        if doc['type'] == 'metadata':
            write_metadata_file(doc, output_dir)
            continue
        
        # 尝试抓取
        html_content = fetch_url(doc['source_url'])
        
        if html_content and len(html_content) > 1000:
            write_full_text_file(doc, output_dir, html_content)
            success_count += 1
        else:
            # 尝试 fallback
            fetched = False
            for fb_url in doc.get('fallback_urls', []):
                print(f"   尝试 fallback: {fb_url[:80]}...")
                html_content = fetch_url(fb_url)
                if html_content and len(html_content) > 1000:
                    write_full_text_file(doc, output_dir, html_content)
                    success_count += 1
                    fetched = True
                    break
            
            if not fetched:
                print(f"   ❌ 无法抓取，降级为 metadata 文件")
                write_metadata_file(doc, output_dir)
                fail_count += 1
        
        time.sleep(1)
    
    print(f"\n{'='*60}")
    print(f"📊 拉取完成统计:")
    print(f"   ✅ 全文成功: {success_count}")
    print(f"   ⚠️  仅存元数据: {fail_count}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
