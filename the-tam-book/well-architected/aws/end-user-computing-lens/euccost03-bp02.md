<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCCOST03-BP02 Use a self-service portal to request your ITSM

Instead of enabling self-service capabilities for your users, use a self-service portal to allow users to request resources, or enable workflow-based request for EUC resources with your ITSM. This gives you better control and limits the exposure to unforeseen cost increases.

**Level of risk exposed if this best
 practice is not established:** Low

## Implementation guidance

Consider implementing a self-service portal to request
 WorkSpaces or changes to your existing WorkSpaces, like
 running mode, bundle, or storage. A self-service portal can
 allow your users to provision and terminate their EUC services
 as required. For an example for Amazon WorkSpaces, see
 [Creating
 a self-service portal for Amazon WorkSpaces end users](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-a-self-service-portal-for-amazon-workspaces-end-users/).

Additionally, consider using your ITSM solution to enable
 workflow-based requests for new WorkSpaces or changes to
 existing WorkSpaces, like running mode, bundle, or storage.
 For examples of integrating with ServiceNow, see
 [How
 to enable self-service Amazon WorkSpaces by using Service Catalog Connector for ServiceNow](https://aws.amazon.com/blogs/mt/how-to-enable-self-service-amazon-workspaces-by-using-aws-service-catalog-connector-for-servicenow/) and
 
 
 [Managing
 Amazon WorkSpaces by integrating Service Catalog with ServiceNow](https://aws.amazon.com/blogs/mt/managing-amazon-workspaces-by-integrating-aws-service-catalog-with-servicenow/).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost03-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
