<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/amazon-api-gateway-2.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Amazon API Gateway

Amazon API Gateway and
 AWS AppSync caching can be enabled to improve performance for applicable operations. DAX can
 improve read responses significantly as well as Global and Local Secondary Indexes to prevent
 DynamoDB full table scan operations. These details and resources were described in the Mobile
 Backend scenario.

API Gateway content encoding allows API clients to request the payload to be compressed
 before being sent back in the response to an API request. This reduces the number of bytes
 that are sent from API Gateway to API clients and decreases the time it takes to transfer the
 data. You can enable content encoding in the API definition, and you can also set the
 minimum response size that triggers compression. By default, APIs do not have content
 encoding support enabled.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/amazon-api-gateway-2.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
