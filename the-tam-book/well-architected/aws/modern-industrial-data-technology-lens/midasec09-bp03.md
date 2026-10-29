<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASEC09-BP03 Automate patch management for ICS and connected data infrastructure

Patch known vulnerabilities in a timely manner across industrial control systems (ICS),
 gateways, and cloud services by automating patch management processes.

**Desired outcome:** Patches are deployed consistently and
 timely, minimizing exposure to known exploits.

**Benefits of establishing this best practice:** Reduces manual
 overhead, enhances system stability, and supports compliance with vulnerability remediation
 SLAs.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely
 with OT vendors for ICS-specific patch cycles.

### Implementation steps

- Inventory all patchable assets across OT and IT systems.
- Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed
 nodes.
- Align maintenance windows with production downtime cycles.
- Monitor patch compliance using AWS Config and AWS Systems Manager reports.

## Resources

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
- [Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
