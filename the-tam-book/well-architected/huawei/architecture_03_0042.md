<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0042.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# SEC06-02 建立安全编码规范

应用安全涉及需求、设计、实现、部署多个环节，实现的安全是应用安全的重要一环。建立安全编码规范有助于团队编写更安全、更高质量的代码，减少甚至规避由于编码错误引入的安全风险。

- **风险等级** 高
- **关键策略** 发布团队常用编程语言的安全编码规范。通用的安全编码规范应包含程序输入校验、程序输出编码、身份验证、访问控制、安全加解密算法、异常处理、IO操作、文件上传、序列化、输出格式化等。 对于在Web应用场景使用的语言如Java、Python，还要考虑安全会话管理、防SQL注入、防跨站脚本攻击XSS、防跨站请求伪造CSRF等编码规范。 对于C/C++语言，要考虑缓冲区溢出漏洞、命令注入、危险函数、内存泄露、指针越界、数组读写越界等安全风险。 对于JavaScript语言，要考虑容易受到XSS攻击的安全风险。

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_03_0042.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
