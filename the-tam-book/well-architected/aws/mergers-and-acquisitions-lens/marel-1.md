<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/marel-1.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MAREL 1: How do you plan to manage application robustness and availability during mergers and acquisitions?

Establish service-level agreements (SLAs) and appropriate
 mechanisms for ensuring high availability. Capture the
 applicable SLAs and operational-level agreements (OLAs) that are
 relevant for the scope of the integration. Check for impact or
 changes required due to mergers and acquisitions. Are the SLAs
 and OLAs related to any third parties involved, like managed
 service providers?

## MAREL01-BP01 Incorporate fault tolerance to achieve high availability as required for your industry vertical and customer expectations

These are two important concepts in the concept of availability. *Fault tolerance* is the ability to withstand subsystem failure and maintain availability (working properly within an established SLA). To implement fault tolerance, workloads use spare (or redundant) subsystems. *Fault isolation* minimizes the scope of impact when a failure does occur. This is typically implemented with modularization. Workloads are broken down into small subsystems that fail independently and can be repaired in isolation.

## MAREL01-BP02 Establish SLAs, including DR RTO and RPO for the combined organization

Critical platforms require high availability. It is advised to achieve the maximum required availability at a reasonable cost that meets customer and business needs.

## MAREL01-BP03 Establish a deployment strategy for combined company

AWS provides a number of tools to simplify and automate the provisioning of infrastructure and deployment of applications. Each deployment service offers different capabilities for managing applications. To build a successful deployment architecture, evaluate the available features of each service against the needs your application and organization.

## MAREL01-BP04 Establish an SRE team and process for the combined organization.

Site reliability engineering (SRE) is the practice of using software tools to automate IT infrastructure tasks such as system management and application monitoring. Organizations use SRE to keep their software applications reliable amidst frequent updates from development teams.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/marel-1.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
