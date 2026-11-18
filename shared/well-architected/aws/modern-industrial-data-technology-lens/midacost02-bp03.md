<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDACOST02-BP03 Automate production-aware resource decommissioning

Implement automated identification and removal of unused resources synchronized with
 production schedules, product lifecycles, and manufacturing compliance requirements. This
 automation includes safety checks, rollback procedures, and consideration of maintenance
 windows to help prevent disruption to manufacturing operations.

**Desired outcome:** Automated identification and removal of
 unused resources synchronized with production schedules, product lifecycles, and manufacturing
 compliance requirements.

**Common anti-patterns:**

- Implementing automated removal without considering production schedules
- Using the same automation rules for both IT and OT resources
- Not incorporating manufacturing compliance checks in automation
- Failing to account for interdependencies with MES, SCADA, or other manufacturing
 systems
- Automated decommissioning during production hours
- Not maintaining audit trails for regulated manufacturing processes
- Bypassing quality management system validations

**Benefits of establishing this best practice:**

- Reduced manual intervention
- Consistent application of decommissioning policies
- Immediate cost savings from unused resource removal
- Reduced human error

**Level of risk exposed if this best practice is not
 established:** High

## Implementation guidance

Create automated systems that can safely identify, tag, notify relevant stakeholders,
 and finally remove resources that are no longer needed, with appropriate safeguards to help
 prevent disruption to manufacturing operations.

### Implementation steps

1. Define automation rules for resource identification.
2. Create automated workflows for:
Resource taggingNotification of stakeholdersBackup creationResource termination
3. Implement safety checks and rollback procedures.
4. Monitor automation effectiveness.
5. Include manufacturing-specific automation rules:
Production schedule-aware decommissioningProduct lifecycle milestonesEquipment maintenance windowsShift pattern considerations

## Key AWS services

- AWS Lambda
- Amazon EventBridge
- AWS Config Rules
- AWS Systems Manager Automation
- AWS Step Functions
- Amazon SNS

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduler.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
