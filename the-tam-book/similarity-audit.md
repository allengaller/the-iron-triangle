# 跨文件同构审计

> `python3 scripts/similarity_audit.py --report`（可复跑，勿手改）
> 口径见 `QUALITY-GATE.md`。

样本 83 个文件｜比较 3403 对｜骨架完全相同 84 对｜同构簇 5 个

## 一、同构簇：骨架完全相同

骨架相同不等于缺陷。本书内涵篇本就统一“定义→分级→训练→自检”四段，那是设计选择。真正要判的是两件事：文字是不是抄的（文本重合），以及是不是同一个模板批量填出来的（成员数 + 字数跨度）。

| 文件数 | 字数区间 | 文本重合中位 | 判定 | 成员 |
|---|---|---|---|---|
| 13 | 1360–1744（跨度 22%） | 0.04 | 批量填充 | b-tam-process-system-howto、i-on-duty-standard-howto、j-enablement-training-howto、k-incident-emergency-howto、l-project-onboarding-howto、m-product-introduction-howto、n-tam-onsite-certification-howto、o-tam-onsite-promotion-howto、r-problem-retrospective-howto、s-overtime-compoff-howto、t-online-change-howto、u-ticket-management-howto、v-tam-bte-sa-triangle-howto |
| 3 | 4542–5048（跨度 10%） | 0.00 | 统一体例 | ch09-risk-compliance、ch12-escalation-crisis、ch13-internal-collaboration |
| 2 | 2532–3092（跨度 18%） | 0.18 | 复刻 | p-tam-service-quality-standard-public-cloud、q-tam-service-quality-standard-dedicated-cloud |
| 2 | 3766–3835（跨度 2%） | 0.00 | 统一体例 | ch17-financial-availability、ch19-financial-incident |
| 2 | 2306–3790（跨度 39%） | 0.02 | 统一体例 | ch24-ai-risk-governance-howto、ch26-measurement-system-howto |

## 二、文本重合 ≥ 0.12 的文件对（非同构簇）

这一栏抓的是“换个标题重发”的情形：骨架不同，但文字大量重合。

| 文本重合 | 骨架同构 | A | B |
|---|---|---|---|
| 0.18 | 1.00 | appx-p-tam-service-quality-standard-public-cloud.md | appx-q-tam-service-quality-standard-dedicated-cloud.md |

## 三、口径与盲区

- 文本重合：12 字片段的包含率（A 的片段有多少出现在 B 中）。用包含率而非 Jaccard，因为长短文件对比时 Jaccard 系统性偏低。
- 骨架同构：二级标题去掉编号与冒号后取 Jaccard。文本可以改写，骨架很难改。
- 测不到同义改写：换词复述、调换小节顺序、重写标题都会拉低分数。
- 不判断质量：两份同构文件可能都很好，也可能都很差，需人工看。
- 不同体裁不该同构。若两个不同 Diátaxis 类型的文件骨架相同，优先怀疑标注有误。

