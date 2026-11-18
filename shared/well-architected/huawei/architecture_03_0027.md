<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0027.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC03-04 安全共享资源

大企业的不同组织、部门、团队之间需要安全共享资源。

- **风险等级** 中
- **关键策略** 大企业往往涉及多个组织单元、多个账号，需要对多账号之间进行共享资源。安全共享资源需遵循以下实践： 使用资源标签。通过标签对资源进行分类和标记，以便于管理和应用策略。 仅与可信实体共享资源。通过使用服务控制策略（SCP）限制权限，您可以限制组织内账户的权限，确保资源仅在组织内部共享。 创建专门的服务账号用于共享资源的访问。
- **相关云服务和工具** 组织 Organizations 资源访问管理 RAM：使用RAM为用户提供安全的跨账号共享资源的能力。如果您有多个华为云账号，您可以创建一次资源，并使用RAM服务将该资源共享给其他账号使用，这样您就不需要在每个账号中创建重复的资源。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0027.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
