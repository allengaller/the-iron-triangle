<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0024.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# OPS04-01 有效落地持续集成

- **风险等级** 高
- **关键策略** 持续集成是一种软件开发实践，开发人员使用它定期将软件更新集成到源代码控制系统中。当工程师向代码仓提交代码时，持续集成过程就开始了。理想情况下，集成过程会根据多个基线和测试来验证代码。然后，它向提交者提供有关这些测试状态的反馈。如果基线检查和测试进展顺利，集成过程将生成并暂存部署更新软件的资产。这些资产包括编译的代码和容器映像。 持续集成可以通过执行以下操作更快地交付高质量的软件： 针对代码运行自动化测试，以便尽早检测到重大更改。 运行代码分析以确保代码标准、质量和配置。 运行合规性和安全检查以确保软件不存在已知漏洞。 运行验收或功能测试以确保软件按预期运行。 对检测到的问题提供快速反馈。 在适用的情况下，生成包含更新代码的可部署资产或包。
- **相关云服务和工具** [CodeArts Pipeline](https://www.huaweicloud.com/intl/zh-cn/product/cloudpipeline.html)

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_06_0024.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
