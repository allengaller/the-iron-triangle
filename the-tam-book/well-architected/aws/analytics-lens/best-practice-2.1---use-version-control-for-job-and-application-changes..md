<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.1---use-version-control-for-job-and-application-changes..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 2.1 – Use version control for job and application changes

Version control systems support tracking changes and the
 ability to revert to previous versions of an analytics
 system should changes cause unintended consequences. Your
 team should version control code repositories for both
 analytics infrastructure as code (IaC) and analytics
 applications logic.

## Suggestion 2.1.1 – Use infrastructure as code and version control systems so that a failed deployment can be rolled back to a previous good state

Follow software development best practices when building
 analytics systems. For example, deploy resources using
 code templates, such as AWS CloudFormation or Hashicorp
 Terraform, so that all deployments occur exactly as
 intended. Use version control systems (for example, code
 repositories such as GitHub) to hold
 current and previous versions of your code templates.
 Using these tools, if a new change results in unwanted
 outcomes, you can easily roll back to the previous code
 template.

For more details, refer to the following information:

- AWS Whitepaper:
 [Introduction
 to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- AWS Blog:
 [Automate
 building an integrated analytics solution with AWS
 Analytics Automation Toolkit](https://aws.amazon.com/blogs/big-data/automate-building-an-integrated-analytics-solution-with-aws-analytics-automation-toolkit/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.1---use-version-control-for-job-and-application-changes..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
