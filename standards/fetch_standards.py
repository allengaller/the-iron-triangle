#!/usr/bin/env python3
"""
附录 W GB/T 国标与 JR/T 行标元数据批量生成脚本
采集时点：2026-10-25
"""

import os
from datetime import datetime

COLLECTION_DATE = "2026-10-25"

# GB/T 国家标准（20份）
GB_T_STANDARDS = [
    {"number": "GB/T 22239-2019", "name": "信息安全技术 网络安全等级保护基本要求", "status": "现行", "notes": "等保 2.0 核心标准，第三级及以上对金融机构普遍适用"},
    {"number": "GB/T 22240-2020", "name": "信息安全技术 网络安全等级保护定级指南", "status": "现行", "notes": "系统定级方法"},
    {"number": "GB/T 25070-2019", "name": "信息安全技术 网络安全等级保护安全设计技术要求", "status": "现行", "notes": "安全建设设计"},
    {"number": "GB/T 28448-2019", "name": "信息安全技术 网络安全等级保护测评要求", "status": "现行", "notes": "测评依据"},
    {"number": "GB/T 25058-2019", "name": "信息安全技术 网络安全等级保护实施指南", "status": "现行", "notes": "实施流程"},
    {"number": "GB/T 39786-2021", "name": "信息安全技术 信息系统密码应用基本要求", "status": "现行", "notes": "密评（商用密码应用安全性评估）依据"},
    {"number": "GB/T 28827.1-2022", "name": "信息技术服务 运行维护 第 1 部分：通用要求", "status": "现行", "notes": "运维服务供方能力模型（人员/过程/技术/资源四要素），ITSS 符合性评估基础"},
    {"number": "GB/T 28827.2-2012", "name": "信息技术服务 运行维护 第 2 部分：交付规范", "status": "现行", "notes": "交付过程管理"},
    {"number": "GB/T 28827.3-2012", "name": "信息技术服务 运行维护 第 3 部分：应急响应规范", "status": "现行", "notes": "应急响应分级与流程，附录 K 的对照基准之一"},
    {"number": "GB/T 28827.4-2019", "name": "信息技术服务 运行维护 第 4 部分：数据中心服务要求", "status": "现行", "notes": "数据中心运维服务专项要求"},
    {"number": "GB/T 28827.6-2019", "name": "信息技术服务 运行维护 第 6 部分：应用系统服务要求", "status": "现行", "notes": "应用运维专项要求"},
    {"number": "GB/T 33136-2016", "name": "信息技术服务 数据中心服务能力成熟度模型", "status": "现行（2024 修订版已发布）", "notes": "数据中心成熟度五级模型，金融数据中心自我评估常用"},
    {"number": "GB/T 51314-2018", "name": "数据中心基础设施运行维护标准", "status": "现行", "notes": "机房基础设施运维的国家标准（住建部体系）"},
    {"number": "GB 50174-2017", "name": "数据中心设计规范", "status": "现行", "notes": "机房分级（A/B/C 级）设计依据"},
    {"number": "GB/T 42581-2023", "name": "信息技术服务 数据中心业务连续性等级评价准则", "status": "现行", "notes": "数据中心业务连续性等级评价"},
    {"number": "GB/T 34982-2017", "name": "云计算数据中心基本要求", "status": "现行", "notes": "云数据中心基本要求"},
    {"number": "GB/T 32910.3-2016", "name": "数据中心资源利用 第 3 部分：电能能效要求", "status": "现行", "notes": "PUE 能效要求"},
    {"number": "GB/T 20988-2007", "name": "信息安全技术 信息系统灾难恢复规范", "status": "现行（2025 修订版已发布）", "notes": "灾难恢复 0–6 七级能力划分与七要素，灾备建设国标基准"},
    {"number": "GB/Z 20986-2007", "name": "信息安全技术 信息安全事件分类分级指南", "status": "现行", "notes": "安全事件定级参照"},
    {"number": "GB/T 36618-2018", "name": "信息安全技术 金融信息服务安全规范", "status": "现行", "notes": "金融信息服务安全"},
]

# JR/T 金融行业标准（15份）
JR_T_STANDARDS = [
    {"number": "JR/T 0265-2023", "name": "金融数据中心能力建设指引", "status": "现行", "notes": "金融数据中心治理/场地/网络/运行管理/风险管控五部分能力要求，基本要求＋增强要求两档"},
    {"number": "JR/T 0361-2026", "name": "金融数据中心智能运维规范", "status": "现行（2026-09 发布）", "notes": "金融数据中心 AIOps/智能运维的建设依据"},
    {"number": "JR/T 0044-2008", "name": "银行业信息系统灾难恢复管理规范", "status": "现行", "notes": "银行灾备管理行业规范，与 GB/T 20988 配套使用"},
    {"number": "JR/T 0071.1-2020", "name": "金融行业网络安全等级保护实施指引 第1部分：基础和术语", "status": "现行", "notes": "等保 2.0 金融行业落地细则（替代 JR/T 0071-2012）"},
    {"number": "JR/T 0072-2020", "name": "金融行业网络安全等级保护测评指南", "status": "现行", "notes": "金融等保测评依据"},
    {"number": "JR/T 0073-2012", "name": "金融行业信息安全等级保护测评服务安全指引", "status": "现行", "notes": "测评服务过程安全"},
    {"number": "银发〔2012〕163 号", "name": "中国人民银行关于银行业金融机构信息系统安全等级保护定级的指导意见", "status": "现行", "notes": "银行系统定级监管口径"},
    {"number": "JR/T 0131-2015", "name": "金融业信息系统机房动力系统规范", "status": "现行", "notes": "机房动力（供配电、UPS 等）专项"},
    {"number": "JR/T 0197-2020", "name": "金融数据安全 数据安全分级指南", "status": "现行", "notes": "金融数据五级分类分级，容灾备份与传输策略按级配置"},
    {"number": "JR/T 0171-2020", "name": "个人金融信息保护技术规范", "status": "现行", "notes": "个人金融信息全生命周期技术要求"},
    {"number": "JR/T 0166-2018", "name": "云计算技术金融应用规范 技术架构", "status": "现行", "notes": "金融上云三件套之一，专有云项目必查"},
    {"number": "JR/T 0167-2018", "name": "云计算技术金融应用规范 安全技术要求", "status": "现行", "notes": "金融上云三件套之一"},
    {"number": "JR/T 0168-2018", "name": "云计算技术金融应用规范 容灾", "status": "现行", "notes": "金融上云三件套之一"},
    {"number": "JR/T 0068-2020", "name": "网上银行系统信息安全通用规范", "status": "现行", "notes": "网银系统安全"},
    {"number": "JR/T 0060-2021", "name": "证券期货业网络安全等级保护基本要求", "status": "现行", "notes": "证券期货业等保落地细则"},
    {"number": "JR/T 0074-2012", "name": "保险业 IT 服务管理基本规范", "status": "现行", "notes": "保险业 ITSM 基线"},
]

def sanitize_filename(name):
    """清理文件名中的非法字符"""
    import re
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = name.replace(' ', '_')
    return name

def generate_gb_t_file(std, output_dir):
    """生成 GB/T 标准元数据文件"""
    filename = f"GB_T_{sanitize_filename(std['number'])}.md"
    filepath = os.path.join(output_dir, filename)
    
    content = f"""# {std['number']} {std['name']}

> **来源**: 国家标准全文公开系统（openstd.samr.gov.cn）  
> **采集时点**: {COLLECTION_DATE}  
> **状态**: 📄 官方平台仅提供在线阅读或受控下载，以下为元数据与官方获取渠道

## 标准信息

| 项目 | 内容 |
|------|------|
| **标准号** | {std['number']} |
| **标准名称** | {std['name']} |
| **发布状态** | {std['status']} |
| **标准类别** | 国家标准（GB/T） |
| **主管部门** | 国家市场监督管理总局（国家标准化管理委员会） |

## 运维要点

{std['notes']}

## 官方获取渠道

- **国家标准全文公开系统**：https://openstd.samr.gov.cn
- **全国标准信息公共服务平台**：https://std.samr.gov.cn

> 提示：国标全文公开系统支持在线阅读和 PDF 下载（部分标准可能仅限在线阅读）。

## 说明

该标准为国家标准（GB/GB/T），官方平台仅提供在线阅读或受控下载，无法通过自动化脚本抓取全文。如需引用，请通过国家标准全文公开系统获取正式版本。

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def generate_jr_t_file(std, output_dir):
    """生成 JR/T 标准元数据文件"""
    filename = f"JR_T_{sanitize_filename(std['number'])}.md"
    filepath = os.path.join(output_dir, filename)
    
    content = f"""# {std['number']} {std['name']}

> **来源**: 金融标准全文公开系统（cfstc.pbc.gov.cn）  
> **采集时点**: {COLLECTION_DATE}  
> **状态**: 📄 官方平台仅提供在线阅读或受控下载，以下为元数据与官方获取渠道

## 标准信息

| 项目 | 内容 |
|------|------|
| **标准号** | {std['number']} |
| **标准名称** | {std['name']} |
| **发布状态** | {std['status']} |
| **标准类别** | 金融行业标准（JR/T） |
| **归口单位** | 全国金融标准化技术委员会（金标委） |
| **主管部门** | 中国人民银行 |

## 运维要点

{std['notes']}

## 官方获取渠道

- **金融标准全文公开系统**：https://cfstc.pbc.gov.cn/bzgk/
- **中国人民银行官网**：https://www.pbc.gov.cn

> 提示：金融标准全文公开系统支持在线阅读和 PDF 下载（部分标准可能仅限在线阅读）。

## 说明

该标准为金融行业标准（JR/T），由全国金融标准化技术委员会（金标委）归口管理。官方平台仅提供在线阅读或受控下载，无法通过自动化脚本抓取全文。如需引用，请通过金融标准全文公开系统获取正式版本。

---
*本文件由批量采集脚本自动生成，采集时间：{COLLECTION_DATE}*
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename

def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📚 GB/T 国标与 JR/T 行标元数据批量生成脚本")
    print(f"📅 采集时点: {COLLECTION_DATE}")
    print(f"📂 输出目录: {output_dir}\n")
    
    # 生成 GB/T 文件
    print(f"📄 正在生成 GB/T 国家标准元数据文件（共 {len(GB_T_STANDARDS)} 份）...")
    for i, std in enumerate(GB_T_STANDARDS, 1):
        filename = generate_gb_t_file(std, output_dir)
        print(f"   [{i}/{len(GB_T_STANDARDS)}] ✅ {filename}")
    
    # 生成 JR/T 文件
    print(f"\n📄 正在生成 JR/T 金融行业标准元数据文件（共 {len(JR_T_STANDARDS)} 份）...")
    for i, std in enumerate(JR_T_STANDARDS, 1):
        filename = generate_jr_t_file(std, output_dir)
        print(f"   [{i}/{len(JR_T_STANDARDS)}] ✅ {filename}")
    
    print(f"\n{'='*60}")
    print(f"📊 生成完成统计:")
    print(f"   GB/T 国家标准: {len(GB_T_STANDARDS)} 份")
    print(f"   JR/T 金融行业标准: {len(JR_T_STANDARDS)} 份")
    print(f"   总计: {len(GB_T_STANDARDS) + len(JR_T_STANDARDS)} 份")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
