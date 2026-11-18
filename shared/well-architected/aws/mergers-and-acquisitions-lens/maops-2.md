<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MAOPS 2: How do you plan to set up and govern a secure, multi-account, or multicloud AWS environment?

Businesses that are expanding their footprint on AWS due to mergers and acquisitions,
 or are planning to enhance an established AWS environment, need have a foundation on AWS
 for their cloud environment. Establishing a cloud foundation on AWS requires guidance
 tailored to your business needs. Using a capability-based approach, you can create an
 environment to deploy, operate, and govern your workloads. A capability includes a
 definition, scenarios, opinionated guidance, and supporting automation to establish and
 operate a specific part of a cloud environment. Capabilities are components that can help
 you plan, implement, and operate your cloud environment, and include people, process, and
 technology considerations. Capabilities are designed to integrate into your overall
 technology environment.

## MAOPS02-BP01 Each company has identified their primary Region

For many services, you can choose an AWS Region that specifies where your resources
 are managed. Regions are sets of AWS resources located in the same geographical area. You
 don't need to choose a Region for the AWS Management Console or for some services, such as AWS Identity and Access Management.

## MAOPS02-BP02 Configure AWS Control Tower, AWS Config, and AWS CloudFormation

AWS Control Tower offers the easiest way to set up and govern a secure, multi-account AWS
 environment. It establishes a landing zone that is based on best-practices blueprints, and
 it enables governance using guardrails you can choose from a pre-packaged list.

## MAOPS02-BP03 Automate infrastructure as code (IaC) using Cloud Formation or Terraform

AWS CloudFormation helps you model, provision, and manage AWS and third-party resources by
 treating infrastructure as code.

## MAOPS02-BP04 Automate resource compliance using tools like AWS Config

AWS Config is a config tool that helps you assess, audit, and evaluate the configurations
 and relationships of your resources.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
