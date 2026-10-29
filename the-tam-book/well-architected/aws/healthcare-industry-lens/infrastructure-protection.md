<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/infrastructure-protection.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Infrastructure protection

Follow Well-Architected best practices for
 [infrastructure
 protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) when designing and managing your
 transactional systems of record.

**Implement security
 controls necessary to protect the infrastructure within the
 AWS account**

Migrated healthcare workloads may have dependencies on
 technologies, older software applications, and host operating
 systems. For such systems, limit network access to sensitive
 hosts, apply the latest available security patches, and the
 employ monitoring practices described above.

Enable [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) in accounts that
 host and process PHI to add intelligent threat detection to
 your environment. GuardDuty continuously monitors
 your AWS accounts and workloads for malicious activity and
 provides detailed security findings. You can also create
 custom, automated [responses
 to GuardDuty findings using Amazon CloudWatch Events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html).

For details on workload protection, see the [security
 pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/infrastructure-protection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
