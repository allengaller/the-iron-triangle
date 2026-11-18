<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops07-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCOPS07-BP01 Use AWS services and tools for automation and infrastructure as code (IaC) across hybrid and edge environments

Automation helps you provide consistent deployment, configuration,
 and monitoring processes, even for applications and data that need
 to reside in specific locations due to data residency
 requirements. This approach improves operational efficiency,
 reduces errors, and facilitates governance and compliance across
 your hybrid and edge infrastructure.

**Desired outcome:** Adopt AWS
 services and tools for automation and infrastructure as code (IaC)
 to consistently provision, manage, and maintain hybrid and edge
 environments, including AWS Outposts and Local Zones.

**Benefits of establishing this best
 practice:** Using AWS automation across hybrid and edge
 deployments enables consistent configuration management,
 streamlined deployments, and efficient scaling of resources. It
 reduces manual effort, minimizes human errors, and promotes
 standardization.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Use AWS services like AWS CloudFormation, AWS Outposts installer
 for servers, and AWS Serverless Application Model (AWS SAM) to
 automate infrastructure provisioning and application deployments
 across edge and cloud environments. Implement infrastructure as
 code (IaC) principles, which produces consistent and repeatable
 processes for deploying, configuring, and managing resources,
 even in locations with data residency requirements.

Additionally, tools like Terraform and Ansible can be used for
 automation and deployment on AWS Outposts, which are AWS-managed
 infrastructure and services deployed at your on-premises
 facilities.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops07-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
