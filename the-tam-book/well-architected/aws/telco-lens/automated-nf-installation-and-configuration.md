<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/automated-nf-installation-and-configuration.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Automated NF installation and configuration

AWS TNB performs the installation and configuration of the 5G NFs (for example, CU,
 AMF, UPF, and SMF) on the provisioned infrastructure.

**Recommendations:** Verify the NF packages and Helm charts
 are properly designed to use the capabilities of Kubernetes and the underlying cloud
 infrastructure. Implement automated testing and canary deployments to validate the NF
 installations.

**Practical advice:** Monitor the NF deployments for errors
 or issues and leverage the AWS TNB APIs to programmatically retrieve logs and metrics for
 troubleshooting. Establish automated rollback and recovery procedures in case of deployment
 failures.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/automated-nf-installation-and-configuration.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
