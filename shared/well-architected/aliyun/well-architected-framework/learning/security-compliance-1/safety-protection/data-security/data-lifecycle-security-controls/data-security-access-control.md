<!-- source: https://help.aliyun.com/zh/well-architected/data-security-access-control -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aliyun -->
<!-- node-id: 2573807 -->

# 数据安全访问控制

为企业数据的访问执行严格的访问控制，是比较有效的事前、事中的安全控制措施，安全访问控制建议遵循如下原则：

1. 最小化访问权限原则：尽可能细化到表、库级别的访问授权；
2. 暴露面最小原则：尽可能对存储数据或敏感信息的数据库、OSSbucket 设置私有访问，并集中到堡垒机或统一认证后进行访问，缩小数据暴露面；
3. 多因素认证：在访问云平台和关键数据时，需要进行多因素认证；
4. 敏感数据访问：对于敏感数据的访问需要有记录，或执行敏感数据访问申请等审批流程，但这往往会使数据的访问和使用增加额外的沟通和流程成本。

---

> 原页面：https://help.aliyun.com/zh/well-architected/data-security-access-control（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
