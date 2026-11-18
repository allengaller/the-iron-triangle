<!-- source: https://help.aliyun.com/zh/well-architected/sec01-bp07-periodic-review-of-the-reasonableness-and-necessity-of-the -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2706141 -->

# 定期审查人员身份合理性和必要性

随着企业员工的变动，比如：员工入职、离职、转岗等，其云上身份及其权限也随之不断调整。在这个过程中，企业需要定期扫描审查云上人员身份，及时识别并处理因人员变动带来的身份闲置、过度授权等问题，并确保诸如开启MFA等相关安全管控策略的持续落地。

## 优先级

中

## 不推荐做法

- 从不审查云上人员身份的合理性和必要性。
- 依赖人工审查，导致过高的操作成本，同时无法保证一致的审核标准。

## 实施指南

建议您使用云治理中心治理检测的功能，通过产品化的手段，定期审查并治理人员身份。

1. 在您第一次使用云治理中心时，需要[开通云治理中心](https://help.aliyun.com/zh/cgc/getting-started/activate-cloud-governance-center)，开通后既可免费使用。云治理中心每天会进行一次云上的治理成熟度状况的检测，建议您定期查看检测数据，并根据修复指引治理风险项。对于人员身份，您可以重点关注人员身份管理、使用细粒度授权等场景下的检测项。更多检测项，请参加云治理中心[支持的检测项（2.0模型）](https://help.aliyun.com/zh/cgc/user-guide/supported-detections-2-0-model)。
2. 订阅治理检测报告，定时获取最新的治理检测结果，方便您及时查看和处理风险事项。具体操作，请参见[订阅治理报告](https://help.aliyun.com/zh/cgc/user-guide/set-check-items#bcf88aa4211vb)。

---

> 原页面：https://help.aliyun.com/zh/well-architected/sec01-bp07-periodic-review-of-the-reasonableness-and-necessity-of-the（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
