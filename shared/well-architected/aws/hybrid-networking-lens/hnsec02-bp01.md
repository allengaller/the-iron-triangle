<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC02-BP01 Implement a landing zone

Implementing a landing zone establishes a standardized, secure
 foundation for hybrid networking infrastructure. A landing zone
 provides centralized identity and access management, standardized
 security controls, governance mechanisms, network architecture, and
 account structures that enable scalable growth while maintaining
 compliance. By automating resource provisioning and implementing
 guardrails from the start, organizations can avoid costly rework
 later while accelerating their cloud adoption journey with
 confidence, knowing they have established proper security boundaries
 and operational efficiency from day one.

**Desired outcome:** Establish a
 secure foundation for your hybrid networking environment with
 consistent architecture and configuration controls.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Ensures consistent security and compliance across all accounts
- Automates account provisioning and governance
- Reduces operational overhead and human error
- Enables scalable and secure hybrid networking environment

## Implementation guidance

- Deploy a landing zone using services such as AWS Control Tower.
- Apply preventive and detective guardrails for governance and
 compliance.
- Standardize account creation and management through Account
 Factory.
- Monitor the landing zone using services such as AWS Control Tower dashboard and Security Hub CSPM.

## Resources

- [AWS Control Tower Landing Zone](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-aws-control-tower.html)
- [AWS Control Tower Guardrails](https://docs.aws.amazon.com/audit-manager/latest/userguide/controltower.html)
- [Provision
 and manage accounts with Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [AWS Control Tower Dashboard](https://docs.aws.amazon.com/controltower/latest/userguide/control-tower-dashboard.html)
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
