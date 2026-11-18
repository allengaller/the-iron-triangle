<!-- 本文件由 fetch_well_architected.py 生成，请勿手工编辑正文结构 -->
# Well-Architected 官方文档本地归档

六家云厂商 Well-Architected 框架官方文档的离线副本。腾讯云另含官方开发者社区的三份卓越架构白皮书（`tencent/article-*.md`）。用途：附录 Z 的事实核对底稿、断网写作与季度复核对照。**引用以原页面为准**，本目录只保证「当时页面写了什么」。

## 目录结构

`aws/` 根下是框架正文，`aws/<doc-set>/` 是延伸文档集（支柱详解、DevOps 与治理指引、运营就绪评审、用户指南）与 30 份 Lens（行业与技术两类）；`aliyun/` 按官方目录树分层，其余厂商平铺。

## 归档范围

| 厂商 | 文件数 | 抓取源 | 说明 |
| --- | --- | --- | --- |
| AWS | 4799 | <https://docs.aws.amazon.com/wellarchitected/latest/framework/> | 框架指南全量（六支柱设计原则与逐条最佳实践）＋延伸文档集与 30 份 Lens |
| Azure | 155 | <https://learn.microsoft.com/en-us/azure/well-architected/> | Well-Architected 目录全量（支柱、设计原则、工作负载、评审） |
| Google Cloud | 58 | <https://docs.cloud.google.com/architecture/framework> | architecture/framework 全量（支柱、Perspective、部署原型） |
| 阿里云 | 274 | <https://help.aliyun.com/zh/well-architected/> | 卓越架构文档集全量（官方 menupath/document_detail 接口树，含 AI 卓越架构） |
| 腾讯云 | 61 | <https://cloud.tencent.com/document/product/1264> | 产品 1264（智能顾问·卓越架构）全量 + 官方社区三份卓越架构白皮书 |
| 华为云 | 394 | <https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/> | usermanual-architecture 卓越架构技术框架全量（按左侧导航全量抓取） |

合计 **5741 个文件**、约 **26975 千字符**，抓取日 2026-10-25、2026-10-26。

抓取分两批：首轮全量落盘后，后续只补新出现在官方索引里的 doc set（当前为 AWS 23 份 Lens）；批内跨零点统一标注批次日，故文件头的 `captured` 只有批次日、没有具体时刻。

## 文件约定

每个文件头部三行注释记录 `source`（原始 URL）、`captured`（抓取日期）、`vendor`；文末回链原页面。正文为 HTML 自动转 Markdown，标题层级、列表、表格、代码块已规整，**语义未改写**。

## 复跑与维护（对接附录 Z.9.2）

```bash
python3 fetch_well_architected.py            # 全量重抓，覆盖同名文件并刷新 captured
python3 fetch_well_architected.py --limit 2  # 抽样验证解析是否失效
```

季度复核时先看本文件底部的失败清单：解析规则失效（页面改版）会表现为某厂商份数骤降或正文变短，此时修选择器而不是删条目。
