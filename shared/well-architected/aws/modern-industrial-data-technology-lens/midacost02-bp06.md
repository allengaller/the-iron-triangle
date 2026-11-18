<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp06.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST02-BP06 Implement manufacturing-aware cost controls

Establish effective guardrails that help prevent unnecessary spending while maintaining
 operational efficiency and flexibility for production demands. This includes implementing
 approval workflows that don't hinder urgent production needs and differentiating between cost
 controls for different environments (production, development, testing).

**Desired outcome:** Effective guardrails that help prevent
 unnecessary spending while maintaining operational efficiency and flexibility for production
 demands.

**Common anti-patterns:**

- Applying blanket cost controls without considering critical manufacturing systems
- Implementing rigid resource limits that don't account for production variability
- Neglecting to create separate cost control policies for research and development, production, and
 quality assurance environments
- Failing to align cost control measures with manufacturing cycles and seasonal demands
- Implementing approval workflows that cause delays in scaling resources for urgent
 production needs
- Not differentiating between cost controls for operational data and long-term
 compliance data storage
- Implementing strict policies that hinder engineering research and development or applying overly
 permissive policies that lead to over provisioning
- Not training employees on best practices of deploying right-sized
 infrastructure/services that balance cost and performance

**Benefits of establishing this Best Practice:**

- Avoided cost overruns
- Controlled resource provisioning
- Enhanced budget compliance
- Improved cost predictability

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Establish mechanisms to monitor, control, and optimize cloud spending for manufacturing
 workloads while verifying that critical operational systems maintain necessary resources.

### Implementation steps

1. Define cost control mechanisms:
Budget thresholdsResource limitsApproval workflows
2. Implement automated enforcement.
3. Create exception processes.
4. Monitor control effectiveness.
5. Regular review and adjustment.

## Key AWS services

- AWS Budgets
- AWS Cost Explorer
- AWS Service Quotas
- AWS Organizations
- AWS CloudFormation
- AWS Control Tower

## Resources

**Related documents:**

- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-cost-categories.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp06.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
