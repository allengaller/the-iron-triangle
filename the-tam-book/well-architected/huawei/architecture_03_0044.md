<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0044.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC06-04 应用安全配置

对应用运行时的各项配置进行加固，以避免因安全配置错误而产生的安全漏洞和风险。

- **风险等级** 高
- **关键策略** 根据安全配置规范，对您工作负载中的应用，如Nginx、Tomcat、Apache、Jetty、JBoss、PHP、Redis等完成安全配置加固和Web攻击防护。 系统越权，例如系统是否存在capability提权、suid文件提权、定时任务提权、sudo文件配置提权等系统提权问题。 服务运行用户，例如服务运行的用户是否为最低权限用户，禁止使用root用户运行服务。 Web攻击，例如Web应用是否存在SQL注入、XSS跨站脚本、文件包含、目录遍历、敏感文件访问、命令、代码注入、网页木马上传、第三方漏洞攻击等常见Web威胁问题。
- **相关云服务和工具** 企业主机安全 HSS Web应用防火墙 WAF

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0044.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
