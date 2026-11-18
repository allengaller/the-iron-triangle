<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec09-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC09-BP01 Verify that your instances are configured as expected

Unexpected configuration changes to end user systems can help
 you identify possible threat actors. Users should not need to
 reconfigure applications or operating systems for the daily use
 of their application portfolio.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Automate configuration management tools to verify compliance.
 Use centralized control and enforcement of configuration
 settings applied to Amazon WorkSpaces and WorkSpaces Applications
 instances to verify that configuration settings align with the
 desired configuration of instances.

- For Active Directory domain-joined Windows instances, use
 Group Policy Objects (GPOs) to apply a known configuration
 to instances.
- For Amazon WorkSpaces Linux instances, consider
 configuration management tools such as Ansible, Chef, and
 Puppet to apply a known configuration.
- For Amazon WorkSpaces Applications On-Demand and Always-On fleets,
 apply desired configuration settings to the instance used
 to create the Image for the associated fleet.

After deployment, you can audit Amazon WorkSpaces Personal
 instances to determine if the expected and desired
 configuration of instances is in effect or whether this has
 been overridden or tampered with. Configuration management
 tools such as Ansible, Chef, and Puppet can help with this, as
 can PowerShell Desired State Configuration.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec09-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
