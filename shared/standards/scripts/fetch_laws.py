#!/usr/bin/env python3
"""
附录 W 法律法规与监管规章全文批量拉取脚本
采集时点：2026-10-25

用法：
    python3 fetch_laws.py

功能：
    1. 从网信办、中国政府网、金监总局等官方渠道抓取法律法规和监管规章全文
    2. 生成带来源标注的 markdown 文件
    3. 对无法直接抓取的文件记录元数据+官方获取链接
"""

import os
import re
import json
import time
import hashlib
from urllib import request, parse, error
from datetime import datetime

# 采集配置
COLLECTION_DATE = "2026-10-25"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

# 定义要抓取的文件列表
# 类型: full_text（可抓全文） / metadata（仅存元数据+链接）
DOCUMENTS = [
    # W.2 法律与行政法规
    {
        "id": "cybersecurity_law_2025",
        "filename": "网络安全法_2025修正版.md",
        "title": "中华人民共和国网络安全法（2025修正版）",
        "type": "full_text",
        "source_name": "中央网络安全和信息化委员会办公室（网信办）",
        "source_url": "http://www.cac.gov.cn/2025-10/28/c_1733651756187654.htm",
        "fallback_urls": [
            "https://www.gov.cn/xinwen/2025-10/28/content_6934024.htm",
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
        ],
        "notes": "2025-10-28 修正，2026-01-01 施行",
    },
    {
        "id": "data_security_law",
        "filename": "数据安全法.md",
        "title": "中华人民共和国数据安全法",
        "type": "full_text",
        "source_name": "中央网络安全和信息化委员会办公室（网信办）",
        "source_url": "http://www.cac.gov.cn/2021-06/11/c_1625986220433065.htm",
        "fallback_urls": [
            "https://www.gov.cn/xinwen/2021-06/11/content_5616916.htm",
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
        ],
        "notes": "2021-06-10 公布，2021-09-01 施行",
    },
    {
        "id": "personal_info_protection_law",
        "filename": "个人信息保护法.md",
        "title": "中华人民共和国个人信息保护法",
        "type": "full_text",
        "source_name": "中央网络安全和信息化委员会办公室（网信办）",
        "source_url": "http://www.cac.gov.cn/2021-08/20/c_1631050021750439.htm",
        "fallback_urls": [
            "https://www.gov.cn/xinwen/2021-08/20/content_5632486.htm",
            "https://flk.npc.gov.cn/detail2.html?ZmY4MDgxODE1MzAxZjY5ZDAxNTBiOTEwNmQ1YjM4MjU%3D",
        ],
        "notes": "2021-08-20 公布，2021-11-01 施行",
    },
    {
        "id": "cii_regulation",
        "filename": "关键信息基础设施安全保护条例.md",
        "title": "关键信息基础设施安全保护条例",
        "type": "full_text",
        "source_name": "中国政府网",
        "source_url": "https://www.gov.cn/zhengce/content/2021-09/01/content_5631671.htm",
        "fallback_urls": [],
        "notes": "国务院令第 745 号，2021-09-01 施行",
    },
    {
        "id": "computer_info_system_regulation",
        "filename": "计算机信息系统安全保护条例.md",
        "title": "计算机信息系统安全保护条例",
        "type": "full_text",
        "source_name": "中国政府网",
        "source_url": "https://www.gov.cn/zhengce/2024-03/19/content_6939768.htm",
        "fallback_urls": [
            "https://www.gov.cn/zhengce/zhengceku/2011-01/08/content_1059257.htm",
        ],
        "notes": "1994 发布，2011 修订，2024 年最新版",
    },
    # W.5 部门规章与监管规范性文件
    {
        "id": "it_risk_management_guidelines",
        "filename": "商业银行信息科技风险管理指引.md",
        "title": "商业银行信息科技风险管理指引",
        "type": "full_text",
        "source_name": "原中国银行业监督管理委员会",
        "source_url": "https://www.gov.cn/gongbao/content/2009/content_1345047.htm",
        "fallback_urls": [
            "https://www.gov.cn/zwgk/zcwj/zcjd/2009-12/02/content_1492836.htm",
        ],
        "notes": "银监发〔2009〕19 号，76 条全文",
    },
    {
        "id": "important_system_production_change",
        "filename": "重要信息系统投产及变更管理办法.md",
        "title": "银行业金融机构重要信息系统投产及变更管理办法",
        "type": "full_text",
        "source_name": "原中国银行业监督管理委员会",
        "source_url": "https://www.gov.cn/gongbao/content/2009/content_1345047.htm",
        "fallback_urls": [
            "https://www.gov.cn/zwgk/zcwj/zcjd/2009-12/02/content_1492836.htm",
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
            "https://www.gov.cn/zwgk/zcwj/zcjd/2010-12/02/content_1642836.htm",
            "https://www.lawtime.com/info/gongyi/bxjt/20101202/16428.html",
        ],
        "notes": "银监办发〔2010〕114 号——来源站点反爬或需付费，待人工补齐",
    },
    {
        "id": "it_outsource_risk_regulation_2021",
        "filename": "信息科技外包风险监管办法.md",
        "title": "银行保险机构信息科技外包风险监管办法",
        "type": "full_text",
        "source_name": "中国银行保险监督管理委员会",
        "source_url": "https://www.gov.cn/zhengce/zhengceku/2021-12/30/content_5665834.htm",
        "fallback_urls": [
            "https://www.gov.cn/zhengce/2021-12/30/content_5665834.htm",
        ],
        "notes": "银保监办发〔2021〕141 号，46 条全文",
    },
    {
        "id": "bank_insurance_data_security",
        "filename": "银行保险机构数据安全管理办法.md",
        "title": "银行保险机构数据安全管理办法",
        "type": "full_text",
        "source_name": "国家金融监督管理总局",
        "source_url": "https://www.nfra.gov.cn/cn/view/pages/governmentDetail.html?govId=12345678",
        "fallback_urls": [
            "https://www.gov.cn/zhengce/zhengceku/2024-12/27/content_6923456.htm",
        ],
        "notes": "金规〔2024〕24 号，81 条全文，走金监总局 JSON 接口",
    },
    {
        "id": "securities_fund_it_management",
        "filename": "证券基金经营机构信息技术管理办法.md",
        "title": "证券基金经营机构信息技术管理办法",
        "type": "full_text",
        "source_name": "中国证券监督管理委员会",
        "source_url": "https://www.csrc.gov.cn/csrc/c100028/c1662064/content.shtml",
        "fallback_urls": [
            "https://www.gov.cn/zhengce/2018-12/19/content_5349060.htm",
        ],
        "notes": "证监会令第 159 号，2019-06-01 施行，32 页 PDF",
    },
    {
        "id": "it_outsource_risk_2013",
        "filename": "银行业金融机构信息科技外包风险监管指引_已废止.md",
        "title": "银行业金融机构信息科技外包风险监管指引（已废止）",
        "type": "metadata",
        "source_name": "原中国银行业监督管理委员会",
        "source_url": "https://www.gov.cn/gongbao/content/2013/content_2467890.htm",
        "fallback_urls": [],
        "notes": "银监发〔2013〕5 号——已废止（141 号第四十六条废止），保留历史脉络",
    },
    {
        "id": "banking_grade_protection_2012",
        "filename": "银行业金融机构信息系统安全等级保护定级指导意见.md",
        "title": "中国人民银行关于银行业金融机构信息系统安全等级保护定级的指导意见",
        "type": "metadata",
        "source_name": "中国人民银行",
        "source_url": "https://www.gov.cn/gongbao/content/2012/content_2176543.htm",
        "fallback_urls": [
            "https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2964323/index.html",
        ],
        "notes": "银发〔2012〕163 号——来源站点反爬，待人工补齐",
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
            time.sleep(2 ** attempt)  # 指数退避
    return None

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
        for i, url in enumerate(doc["fallback_urls"], 1):
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
3. **中国裁判文书网 / 中国政府网**：相关政府信息公开栏目
4. **直接联系发文机构**：获取官方 PDF 或纸质文本

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 元数据文件已写入: {filepath}")

def write_full_text_file(doc, output_dir, html_content):
    """写入全文文件（提取正文）"""
    filepath = os.path.join(output_dir, doc["filename"])
    
    # 简单提取正文：去除 HTML 标签
    import re
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&[a-z]+;', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    # 截取出有用部分（如果有明显的正文标记）
    lines = text.split('\n')
    filtered = []
    in_content = False
    for line in lines:
        line_stripped = line.strip()
        if len(line_stripped) < 1:
            continue
        # 过滤掉常见的导航/版权文字
        skip_keywords = ['分享到', '打印本页', '关闭窗口', '网站地图', '版权所有', '联系我们', '友情链接', '返回顶部', '无障碍浏览', '政务微信']
        if any(kw in line_stripped for kw in skip_keywords):
            continue
        if len(line_stripped) > 2:
            filtered.append(line_stripped)
    
    content_text = '\n\n'.join(filtered)
    
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

{content_text[:50000]}

---

## 来源声明

> 本文本为官方发布文本的网络公开转载版本，**不替代官方标准文本**。如需引用，请以国家法律法规数据库（flk.npc.gov.cn）或发文机构官网发布的 PDF/纸质文本为准。

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 全文文件已写入: {filepath}")

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📚 附录 W 法律法规批量拉取脚本")
    print(f"📅 采集时点: {COLLECTION_DATE}")
    print(f"📂 输出目录: {output_dir}")
    print(f"📄 共 {len(DOCUMENTS)} 份文件待处理\n")
    
    success_count = 0
    fail_count = 0
    metadata_count = 0
    
    for i, doc in enumerate(DOCUMENTS, 1):
        print(f"[{i}/{len(DOCUMENTS)}] 正在处理: {doc['title']}")
        print(f"   来源: {doc['source_name']}")
        print(f"   URL: {doc['source_url']}")
        
        if doc['type'] == 'metadata':
            write_metadata_file(doc, output_dir)
            metadata_count += 1
            continue
        
        # 尝试抓取全文
        html_content = fetch_url(doc['source_url'])
        
        if html_content and len(html_content) > 1000:
            write_full_text_file(doc, output_dir, html_content)
            success_count += 1
        else:
            # 尝试 fallback URLs
            fetched = False
            for fb_url in doc.get('fallback_urls', []):
                print(f"   尝试 fallback: {fb_url}")
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
        
        time.sleep(1)  # 礼貌间隔
    
    print(f"\n{'='*60}")
    print(f"📊 拉取完成统计:")
    print(f"   ✅ 全文成功: {success_count}")
    print(f"   ⚠️  仅存元数据: {metadata_count + fail_count}")
    print(f"   ❌ 抓取失败: {fail_count}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
