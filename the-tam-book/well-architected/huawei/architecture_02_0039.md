<!-- source: https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0039.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: huawei -->

# RES05-01 网络连接高可用

应用系统对外提供服务时，需要确保对外网络连接的高可用，避免单个网络连接中断而导致业务不可用。

- **风险等级** 高

- **关键策略** 网络链路冗余：网络连接需要支持多路径，以实现高可用能力，以避免在一条网络路径中断的情况下，业务能切换到其他路径继续通信。 网络链路快速倒换：需要定期检查网络链路的连通性，但检测到失败时需要尽快切换到正常路径。 公有云组网场景可通过多EIP 弹性IP及DNS域名解析实现网络连接的高可用；对可用性要求较高的场景，需要支持智能DNS功能，能对EIP进行异常监控和自动切换；此外DNS自身也需要冗余容错，避免由于DNS故障而导致域名解析失败，业务中断。 混合云组网场景链路冗余与倒换方案： 双DC专线冗余：用户数据中心与华为云VPC之间采用两条DC专线互通；其中两条物理专线接入同区域的两个华为云专线接入点，并通过BGP路由协议接入同一个VPC，用户可设置虚拟接口的优先级以决定业务的主备链路。 具体的方案参见“[用户通过虚拟网关负载冗余方式访问VPC](https://support.huaweicloud.com/intl/zh-cn/bestpractice-dc/dc_05_0003.html)”。 双VPN冗余：用户数据中心与华为云VPC之间采用两条VPN连接保证可靠性；当其中一条VPN连接故障时，系统可以切换到另一条VPN连接，保证网络不中断。两条VPN连接可以是双活或主备部署。 具体的方案参见“[通过VPN实现云上云下网络互通（双活模式）](https://support.huaweicloud.com/intl/zh-cn/bestpractice-vpn/vpn_best_00019.html)”与“[通过VPN实现云上云下网络互通（主备模式）](https://support.huaweicloud.com/intl/zh-cn/bestpractice-vpn/vpn_best_00028.html)”。 DC专线/VPN主备：用户数据中心与华为云VPC之间同时部署DC专线和VPN两条网络链路，互为主备，并通过企业路由器，可以实现DC和VPN主备链路的自动切换，不需要手工切换双链路，不仅避免业务受损，同时降低维护成本。 具体的方案参见“[通过企业路由器构建DC/VPN双联路主备混合云组网](https://support.huaweicloud.com/intl/zh-cn/bestpractice-vpn/er_03_0081.html)”。
- **相关云服务和工具** 云专线 DC 虚拟专用网络 VPN

---

> 原页面：https://support.huaweicloud.com/intl/zh-cn/usermanual-architecture/architecture_02_0039.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
