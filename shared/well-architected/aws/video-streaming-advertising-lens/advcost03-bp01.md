<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVCOST03-BP01 Consider private communication channels between SSP and DSP

Private communication channels can help keep traffic secure while also reducing
 internet egress charges.

## Implementation guidance

With [AWS PrivateLink](https://aws.amazon.com/privatelink/), you can
 establish secure, private communication channels between your SSPs, DSPs, and other AWS
 services or on-premises resources. This approach enhances security, reduces data exposure
 risks, and can improve performance for your programmatic advertising workloads, while
 simplifying your network architecture and reducing operational overhead. In cases where
 PrivateLink cannot be used, then Amazon VPC Peering, AWS Direct Connect, and AWS Global Accelerator can be
 considered.

## Resources

- [AWS lowers data processing charges for AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2021/07/aws-lowers-data-processing-charges-aws-privatelink/)
- [Get
 started with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
