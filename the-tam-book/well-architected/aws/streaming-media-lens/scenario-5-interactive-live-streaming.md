<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/scenario-5-interactive-live-streaming.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Interactive live streaming

Some content is particularly well-suited to interactive delivery, where the audience is providing direct textual feedback or other interaction as the program is happening (livestreamed gaming, for example). In these cases, not only is delivery latency a concern, but also a low-latency mechanism for delivery of feedback in a many-to-one model. Some use cases also call for the ability to have multiple video participants, perhaps in a host and guest or multi-party chat configuration.

The technology used for interactive streaming will have implications on scalability, as technologies used for real-time delivery (e.g. WebRTC) don't usually scale to large audiences. For some workflows, a two-tier participant setup where a subset of users is actively participating while a larger group is watching passively can bridge the gap between a fully-interactive experience and supporting a large audience. Interactive text chat can also be included for an interactive component that can scale higher than real-time streaming.

## Reference architecture

![Interactive live streaming architecture with a studio containing source devices, a gaming table, and a dealer module. Video is sent via RTMP(S) or WHIP through an encoder to Amazon IVS for real-time video processing in the AWS Cloud, with WebRTC delivery to players running the Amazon IVS Broadcast SDK. The dealer module sends REST or WebSocket data through AWS Direct Connect to Amazon EKS, which handles data processing, lobby or chat API, and game metadata through a dealer module. A Network Load Balancer connects to Amazon CloudFront for API delivery, protected by AWS WAF, with WebSocket connections to client devices.](/images/wellarchitected/latest/streaming-media-lens/images/image5.png)

1. Live video is captured from mobile or desktop source devices integrated with the Amazon Interactive Video Service (Amazon IVS) Real-Time Streaming broadcast SDK. It is then encoded and sent as an input to an Amazon IVS stage. An encoder device or an application like OBS Studio can also send video.
2. Amazon IVS receives the encoded video through Real Time Messaging Protocol (RTMP) over a TLS/SSL connection (RTMPS), WebRTC-HTTP ingestion protocol (WHIP), or WebRTC.
3. Relevant metadata is sent to a REST API layer for additional storage and processing and to a player. Direct Connect uses a dedicated connection for a secure and low-latency data (REST or WebSocket) transfer between your on-premises studio and AWS.
4. Amazon Elastic Kubernetes Service (Amazon EKS) processes REST APIs and WebSockets for content metadata, lobby or chat, and API functionality. It handles players' API calls and maintains WebSocket connections to players for dealer module messages.
5. Network Load Balancer offers ultralow latencies for latency-sensitive applications to process API communication between players and the application. The timed metadata is sent to the Amazon IVS endpoint.
6. Amazon CloudFront acts as an endpoint for inbound data flow and customer API requests during the video stream.
7. AWS WAF helps protect the endpoints and APIs from distributed denial of service (DDoS) attacks.
8. Players maintain WebSocket connections to the backend API for lobby or chat and game action calls.
9. The Amazon IVS player on the client device receives the video stream and metadata. The video and metadata are sent to client applications running the Amazon IVS broadcast SDK through WebRTC. Your viewers can watch live streams globally through the Amazon IVS content delivery network. The Amazon IVS broadcast SDK optimizes performance, reducing the impact on your app and on user devices.

## Configuration notes

- Visit [ivs.rocks](https://ivs.rocks/) to see a variety of use cases, demos, and partners that can provide turnkey solutions and enhancements for IVS workflows.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/scenario-5-interactive-live-streaming.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
