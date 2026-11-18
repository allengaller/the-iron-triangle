<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC02-BP04 Limit access to networking APIs

Implement strict controls over network management interfaces and
 APIs to prevent unauthorized access and changes to critical network
 infrastructure. This includes limiting access based on identity,
 role, and network location while maintaining comprehensive audit
 trails of all management actions.

**Desired outcome:** Prevent
 unauthorized access and modification of sensitive networking
 resources by restricting API access to approved personnel and secure
 locations.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Minimizes risk of accidental or malicious changes to critical
 network resources
- Supports enforcement of least privilege and security boundaries
- Reduces attack surface and potential for misconfiguration
- Enables better auditability and compliance

## Implementation guidance

- Grant access to networking APIs only to authorized networking
 teams or accounts. For example, you can achieve this using AWS
 IAM policies and resource-based policies.
- Monitor and audit API call to sensitive networking services,
 using services such as AWS CloudTrail.
- Regularly review permissions and restrict access on a
 least-privilege basis.

## Resources

- [Controlling
 Access to AWS Resources Using Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [IAM
 Policy Conditions for Source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html#AvailableKeys)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Best
 Practices for IAM Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
