<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_personnel_capability.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# OPS07-BP01 Ensure personnel capability

Have a mechanism to validate that you have the appropriate number of trained personnel to support the workload. They must be trained on the platform and services that make up your workload. Provide them with the knowledge necessary to operate the workload. You must have enough trained personnel to support the normal operation of the workload and troubleshoot any incidents that occur. Have enough personnel so that you can rotate during on-call and vacations to avoid burnout.

**Desired outcome:**

- There are enough trained personnel to support the workload at times when the workload is available.
- You provide training for your personnel on the software and services that make up your workload.

**Common anti-patterns:**

- Deploying a workload without team members trained to operate the platform and services in use.
- Not having enough personnel to support on-call rotations or personnel taking time off.

**Benefits of establishing this best
 practice:**

- Having skilled team members helps effective support of your workload.
- With enough team members, you can support the workload and on-call rotations while decreasing the risk of burnout.

**Level of risk exposed if this best practice
 is not established:** High

## Implementation guidance

Validate that there are sufficient trained personnel to support the workload. Verify that you have enough team members to cover normal operational activities, including on-call rotations.

**Customer example**

AnyCompany Retail makes sure that teams supporting the workload are properly staffed and trained. They have enough engineers to support an on-call rotation. Personnel get training on the software and platform that the workload is built on and are encouraged to earn certifications. There are enough personnel so that people can take time off while still supporting the workload and the on-call rotation.

### Implementation steps

1. Assign an adequate number of personnel to operate and support your workload, including on-call duties, security issues, and lifecycle events, such as end of support and certificate rotation tasks.
2. Train your personnel on the software and platforms that compose your workload.
[AWS Training and Certification](https://aws.amazon.com/training/) has a library of courses about AWS. They provide free and paid courses, online and in-person.[AWS hosts events and webinars](https://aws.amazon.com/events/) where you learn from AWS experts.
3. Perform the following on a regular basis:
Evaluate team size and skills as operating conditions and the workload change.Adjust team size and skills to match operational requirements.Verify ability and capacity to [address planned lifecycle events](https://docs.aws.amazon.com/health/latest/ug/aws-health-planned-lifecycle-events.html), unplanned security, and operational notifications through AWS Health.

**Level of effort for the implementation plan:** High. Hiring and training a team to support a workload can take significant effort but has substantial long-term benefits.

## Resources

**Related best practices:**

- [OPS11-BP04 Perform knowledge management](./ops_evolve_ops_knowledge_management.html) - Team members must have the information necessary to operate and support the workload. Knowledge management is the key to providing that.

**Related documents:**

- [AWS Events and Webinars](https://aws.amazon.com/events/)
- [AWS Training and Certification](https://aws.amazon.com/training/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_personnel_capability.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
