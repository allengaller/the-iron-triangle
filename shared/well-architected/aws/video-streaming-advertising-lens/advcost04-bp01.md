<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVCOST04-BP01 Consider lower cost storage for older User Profile data

As the 30 most recent days are most relevant, using DynamoDB can prioritize high
 performance for the most relevant data (typically within the last 30 days), and archiving to
 Amazon S3 can reduce costs for less relevant data.

**For S3 profile data:**

- Enable S3 Intelligent-Tiering on your bucket
- Configure lifecycle policies to transition older data
- Set up monitoring to track access patterns

1. **For DynamoDB:**
Implement TTL for old profile recordsCreate export jobs to move historical data to S3Use S3 Lifecycle policies for long-term archival

**Cost optimization best practices**

- Regularly analyze data access patterns
- Use AWS Cost Explorer to track storage expenses
- Consider object size and retrieval frequency
- Implement tagging for better cost tracking

## Key AWS services

- DynamoDB
- S3
- Intelligent Tiering

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
