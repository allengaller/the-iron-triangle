<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-incresp.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Incident response

Even with extremely mature preventive and detective controls, your
 organization should still put processes in place to respond to and
 mitigate the potential impact of security incidents. The
 architecture of your workload strongly affects the ability of your
 teams to operate effectively during an incident, to isolate or
 contain systems, and to restore operations to a known good state.
 Putting in place the tools and access ahead of a security
 incident, then routinely practicing incident response through game
 days, will help you verify that your architecture can accommodate
 timely investigation and recovery.

In AWS, the following practices facilitate effective incident
 response:

- Detailed logging is available that contains important content,
 such as file access and changes.
- Events can be automatically processed and launch tools that
 automate responses through the use of AWS APIs.
- You can pre-provision tooling and a “clean room” using AWS CloudFormation. This allows you to carry out forensics in a
 safe, isolated environment.

The following question focuses on these considerations for
 security.

Verify that you have a way to quickly grant access for your
 security team, and automate the isolation of instances as well
 as the capturing of data and state for forensics.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-incresp.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
