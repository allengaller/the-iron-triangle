<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience

Edge services can accelerate requests for static content as well
 as improve the response time for dynamic requests. By using the
 advantages of the cloud backbone network, it can maximize the
 efficiency and stability of access after requests enter the cloud.

## Implementation guidance

If your advertising workload involves serving static content,
 such as images or videos, use
 [Amazon CloudFront](https://aws.amazon.com/cloudfront/) to cache and deliver your content from edge
 locations around the world. Amazon CloudFront reduces latency
 and improves user experience for your global audience by serving
 content from the nearest edge location.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Regional Edge Caches (RECs)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Points of Presence (POPs)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)

## Resources

- [Use
 an Amazon CloudFront distribution to serve a static website](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/getting-started-cloudfront-overview.html)
- [Ways
 to use CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html)
- [CloudFront
 configuration best practices](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html)
- [Speeding
 up your website with Amazon CloudFront](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html)
- [Customize
 at the edge with Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
