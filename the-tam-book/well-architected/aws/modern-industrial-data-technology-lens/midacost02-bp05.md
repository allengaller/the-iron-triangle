<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST02-BP05 Develop cloud resource policies aligned with manufacturing operations

Create well-defined policies for cloud resource provisioning, usage, and management that
 reflect specific manufacturing processes, compliance requirements, and cost optimization
 goals. These policies should consider both IT and OT needs while maintaining operational
 efficiency.

**Desired outcome:** Well-defined policies for cloud resource
 provisioning, usage, and management that reflect specific manufacturing processes, compliance
 requirements, and cost optimization goals.

**Common anti-patterns:**

- Creating generic cloud policies without considering manufacturing-specific needs
- Implementing policies that hinder rapid scaling during production spikes
- Overlooking OT or IT integration in policy development
- Failing to involve key stakeholders (for example, production managers and quality
 control) in policy creation
- Not accounting for different policy needs across various manufacturing stages
 (design, production, and maintenance)
- Implementing strict cost-saving policies that compromise manufacturing system
 reliability

**Benefits of establishing this best practice:**

- Standardized resource management
- Clear governance framework
- Aligned business and IT objectives
- Improved cost control

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Develop and implement comprehensive policies that reflect your organization's specific
 manufacturing requirements while improving cost optimization.

### Implementation steps

1. Document organizational requirements:
Manufacturing process needsCompliance requirementsCost optimization targets
2. Create policy frameworks for:
Resource provisioningAccess controlCost allocationData management
3. Establish review and approval processes.
4. Implement policy enforcement mechanisms.

## Key AWS services

- AWS Organizations
- AWS Control Tower
- Service Catalog
- AWS IAM
- AWS Config
- AWS CloudFormation

## Resources

**Related documents:**

- [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
