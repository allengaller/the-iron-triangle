<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec02-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS

Protect data in transit by using encrypted communication channel
 at the network communication level.

## Implementation guidance

Protecting data that is transmitted from network to network
 remains a top security priority. Data confidentiality,
 integrity, and authenticity of the supported workloads are
 crucial for securing sensitive information, preventing
 unauthorized access, and enabling reliable operations within the
 workload.

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish connectivity between Amazon VPCs
 and other services without exposing the data to the public
 internet. If you have on-premises resources, consider using
 [AWS Direct Connect](https://aws.amazon.com/directconnect/). Direct Connect can make it easy to
 establish private connectivity between an AWS datacenter and
 your internal network. Implementing MACsec security on your
 Direct Connect connection provides point-to-point encryption for
 your traffic.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec02-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
