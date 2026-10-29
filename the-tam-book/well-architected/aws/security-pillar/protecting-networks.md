<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-networks.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Protecting networks

Users, both in your workforce and your customers, can be located anywhere. You need
 to pivot from traditional models of trusting anyone and anything that has access to your
 network. When you follow the principle of applying security at all layers, you employ a
 [Zero Trust](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/) approach. Zero Trust security is a model where application components
 or microservices are considered discrete from each other and no component or microservice
 trusts any other.

The careful planning and management of your network design forms the
 foundation of how you provide isolation and boundaries for resources within your workload.
 Because many resources in your workload operate in a VPC and inherit the security properties,
 it’s critical that the design is supported with inspection and protection mechanisms backed by
 automation. Likewise, for workloads that operate outside a VPC, using purely edge services
 and/or serverless, the best practices apply in a more simplified approach. Refer to the [AWS
 Well-Architected Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) for specific guidance on serverless
 security.

###### Best practices

- [SEC05-BP01 Create network layers](./sec_network_protection_create_layers.html)
- [SEC05-BP02 Control traffic flow within your network layers](./sec_network_protection_layered.html)
- [SEC05-BP03 Implement inspection-based protection](./sec_network_protection_inspection.html)
- [SEC05-BP04 Automate network protection](./sec_network_auto_protect.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-networks.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
