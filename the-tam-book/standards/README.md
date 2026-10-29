# standards/　金融运维法规标准全文库（附录 W 配套）

> 本目录是附录 W《中国金融行业运维相关标准与监管要求汇编》（`manuscript/appx-w-financial-ops-standards.md`）的本地全文配套。
> 全部文件采集/登记时点为 **2026-10-25**。全文类文件头部均标注来源链接；**转载文本不替代官方标准文本**，正式引用须回到官方渠道核对。

## A. 法律法规与监管规章（全文已拉取）

| 文件 | 本地文件 | 来源 | 状态 |
| --- | --- | --- | --- |
| 中华人民共和国网络安全法（2025 修正版全文） | [law-cybersecurity-2016](law-cybersecurity-2016.md) | 国家互联网信息办公室 cac.gov.cn | 现行（修正版 2026-01-01 施行） |
| 中华人民共和国数据安全法 | [law-data-security-2021](law-data-security-2021.md) | 国家互联网信息办公室 cac.gov.cn | 现行 |
| 中华人民共和国个人信息保护法 | [law-pipl-2021](law-pipl-2021.md) | 国家互联网信息办公室 cac.gov.cn | 现行 |
| 关键信息基础设施安全保护条例（国务院令第 745 号） | [reg-critical-info-infrastructure-2021](reg-critical-info-infrastructure-2021.md) | 中国政府网 | 现行 |
| 计算机信息系统安全保护条例（2011 修订） | [reg-computer-info-system-protection](reg-computer-info-system-protection.md) | 中国政府网/国务院公报 | 现行 |
| 商业银行信息科技风险管理指引（银监发〔2009〕19 号） | [reg-commercial-bank-it-risk-2009-19](reg-commercial-bank-it-risk-2009-19.md) | 上海市发改委网站转载 | 现行 |
| 银行业金融机构重要信息系统投产及变更管理办法（银监办发〔2009〕83 号） | [reg-important-system-go-live-2009-83](reg-important-system-go-live-2009-83.md) | 华律网公开转载 | 现行 |
| 商业银行数据中心监管指引（银监办发〔2010〕114 号） | [reg-commercial-bank-data-center-2010-114](reg-commercial-bank-data-center-2010-114.md) | 公开全文未程序化获取，文件内附渠道 | 现行（待补全文） |
| 银行业金融机构信息科技外包风险监管指引（银监发〔2013〕5 号） | [reg-it-outsourcing-risk-2013-5](reg-it-outsourcing-risk-2013-5.md) | 公开全文未程序化获取，文件内附渠道 | **已废止**（141 号第四十六条） |
| 银行保险机构信息科技外包风险监管办法（银保监办发〔2021〕141 号） | [reg-bank-insurance-it-outsourcing-2021-141](reg-bank-insurance-it-outsourcing-2021-141.md) | 中国政府网 | 现行 |
| 银行保险机构数据安全管理办法（金规〔2024〕24 号） | [reg-bank-insurance-data-security-2024](reg-bank-insurance-data-security-2024.md) | 金融监管总局官网（API 原文） | 现行（废止 2022 年 118 号办法） |
| 证券基金经营机构信息技术管理办法（证监会令第 152 号） | [reg-securities-fund-it-management](reg-securities-fund-it-management.md) | 中国政府网 PDF（pypdf 提取，32 页） | 现行 |
| 人民银行关于银行业金融机构信息系统安全等级保护定级的指导意见（银发〔2012〕163 号） | [pbc-grading-opinion-2012-163](pbc-grading-opinion-2012-163.md) | 公开全文未程序化获取，文件内附渠道 | 现行（待补全文） |

## B. 国家标准 GB/GB/T（元数据 + 官方渠道）

等保 2.0 系列（GB/T 22239 / 22240 / 25070 / 28448 / 25058 / 39786）、运维服务系列（GB/T 28827.1/.2/.3/.4/.6）、数据中心系列（GB/T 33136-2024、GB 51314、GB 50174、GB/T 42581、GB/T 34982、GB/T 32910.3）、容灾与事件（GB/T 20988-2007、GB/Z 20986）、金融专项（GB/T 36618）。共 20 份，见各 `GB-*.md` 文件。

- 全文官方渠道：[国家标准全文公开系统](https://openstd.samr.gov.cn/bzgk/gb/index)（在线阅读）、[全国标准信息公共服务平台](https://std.samr.gov.cn/)（状态核验）

## C. 金融行业标准 JR/T（元数据 + 官方渠道）

JR/T 0265-2023、JR/T 0361-2026、JR/T 0044-2008、JR/T 0071.1–.6—2020、JR/T 0072-2020、JR/T 0073-2012、JR/T 0131-2015、JR/T 0197-2020、JR/T 0171-2020、JR/T 0166/0167/0168-2018、JR/T 0068-2020、JR/T 0060-2021、JR/T 0074-2012。共 15 份，见各 `JR-T-*.md` 文件。

- 全文官方渠道：[金融标准全文公开系统](https://cfstc.pbc.gov.cn/bzgk/)（人民银行，多数可下载 PDF）

## 维护规则

1. 每年随附录 W 复核一次；重点：GB/T 20988-2025 与 GB/T 33136-2024 的实施日期、JR/T 新标准发布；
2. 全文文件只修正来源错误，不静默改动原文；新版发布后新增文件而非覆盖；
3. 补全文渠道：114 号（法律图书馆/百度百科词条有全文，反爬）、163 号（人民银行文告 PDF）、2013-5 号（已废止，北大法宝）——欢迎人工补齐后替换占位文件。
