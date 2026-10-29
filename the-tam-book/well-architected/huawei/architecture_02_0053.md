<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0053.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES07-03 监控到异常后发送消息通知

当对应用系统监控发现应用异常后，需要向相应的人员和系统发送实时通知消息和告警，以便及时处理。

- **风险等级** 中
- **关键策略** 采用实时快捷的消息通知方式，以便相关人员能及时得到消息。 消息发送人员需要涵盖运维人员，以便及时恢复。 运维人员需要有备份，避免单点风险。 SMN消息通知服务可依据用户需求主动推送通知消息，方式可为短信、电子邮件等。CES、AOM、CTS、APM、LTS等服务均已经对接SMN消息通知服务，在阈值规则发生变化时，可以以邮件或短信等方式通知，以便您在第一时间发现异常并进行处理。
- **相关云服务和工具** 消息通知服务 SMN 云运维中心 COC：支持人员管理、排班管理和通知管理，可以根据通知规则自动将消息发送给要通知的人员。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0053.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
