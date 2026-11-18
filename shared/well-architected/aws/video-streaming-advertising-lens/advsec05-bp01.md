<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC05-BP01 Validate and sanitize content before running a campaign

Content validation is essential to mitigate ad fraud and block
 unwanted content from reaching ad audience.

## Implementation guidance

Consider using
 Amazon S3 which can serve as a secure, scalable storage
 solution for advertising content. It allows for simple
 management and distribution of assets. S3 can be configured
 with strict access controls and encryption to maintain the
 security of the advertisement files. Additionally, Amazon
 Rekognition can be utilized to analyze images and videos in
 advertisements, verifying they meet solution standards and
 don't contain inappropriate content. This AI-powered service
 can detect objects, scenes, and activities in visual content.
 For additional monitoring and auditing, consider using AWS
 CloudTrail to provide a record of actions taken by users,
 roles, or AWS services in the ad serving solution, which is
 essential for security analysis and compliance audits.

## Key AWS services

- Amazon S3
- Amazon Rekognition
- AWS CloudTrail

## Resources

- [Checking object integrity in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
