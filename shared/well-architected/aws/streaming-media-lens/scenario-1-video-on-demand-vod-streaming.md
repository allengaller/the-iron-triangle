<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/scenario-1-video-on-demand-vod-streaming.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Video on demand (VOD) streaming

Video-on-Demand (VOD) or file-based streaming is the most common streaming scenario. VOD content is shared by millions of content creators across user-generated content sites, used in the enterprise for training, or used to deliver popular movies and television shows to the home.

There exists a wide range of file-based streaming architectures. If your content is already in an adaptive bit rate format, an Amazon S3 origin and a CDN is all that you need to serve viewers. However, if your content is in a high-bit rate format, you need a batch processing component to convert the media into a distribution format.

There are many ways to deploy a batch process on AWS for media processing. You can deploy transcoding software on Amazon EC2 instances directly, use Docker containers with Amazon ECS and AWS Batch, or use services from AWS or AWS Partners. If you're getting started with VOD, we recommend using AWS Elemental MediaConvert. MediaConvert helps you scale transcoding to meet demand, keep costs low, and retain video quality without the overhead of managing any infrastructure.

You might need additional logic or steps in your workflow to extract content metadata, register content with content management systems, make intelligent processing decisions, or to introduce quality control steps. A common approach is through a serverless design that uses AWS Step Functions to model your workflow, AWS Lambda to run logic, and services like AWS Elemental MediaConvert, AWS Batch, and Amazon ECS to scale compute-intensive media processing.

## Reference architecture

![VOD streaming architecture within an AWS Region showing file sources uploading to Amazon S3 for ingest, a processing stage with metadata extraction, MediaConvert transcoding, and quality control orchestrated by a workflow state machine, an origination stage with MediaPackage as the origin service connected to content management, and a delivery stage with CloudFront CDN serving player devices.](/images/wellarchitected/latest/streaming-media-lens/images/image1.png)

1. Content is uploaded through an application or file transfer tools.
2. Object Created event emitted by object storage invokes the media processing workflow.
3. Workflow progresses through batch processing stages like analysis, transcoding, and quality control.
4. Completed content is published to origin service and made available through content management APIs.
5. Players request content from origin service and begins viewing session.

## Configuration notes

- Communication within a serverless workflow is typically done by event publishers, messaging services, and subscribed functions. Operations triggered from events must be idempotent, as failures can occur and events can be delivered more than once.
- Consider using separate buckets for ingest and origination to reduce the risk of unintentional access to source assets.
- Media analysis tools and machine learning can be used to extract source characteristics and drive intelligent processing decisions.
- To reduce delivery and storage costs, explore compression technologies such as [AWS Quality-Defined Variable bit rate (QVBR)](https://docs.aws.amazon.com/mediaconvert/latest/ug/choosing-rate-control-mode.html) that provide streams at lower bitrates but equivalent video quality.
- Many sources only need to be read once for processing. Use aggressive lifecycle policies to optimize object storage costs for source material.
- Processing and storing media in multiple protocols or digital rights management (DRM) schemes can increase storage costs by orders of magnitude. Architectures that serve multiple formats or media endpoint customization should use a just-in-time packaging (JITP) origin.
- Use a content delivery network (CDN) to improve time-to-first-frame performance and offload origin request rate.
- Refer to the [Video on Demand on AWS solutions implementation](https://aws.amazon.com/solutions/implementations/video-on-demand-on-aws/) for a well-architected reference architecture for Video-on-Demand.
- Review the [Well-Architected Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) for best practices regarding serverless architectures.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/scenario-1-video-on-demand-vod-streaming.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
