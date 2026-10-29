<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF08-BP04 Monitor operating system metrics

Operating systems can add significant variations in performance to your Workload
 depending on the compute, storage, and memory resources required. Test with all operating
 systems that are intended to be supported by your deployment.

**Level of risk exposed if this best practice is not
 established:** Low

## Implementation guidance

Monitor the performance of instances delivering end user services.

- Use operating system metrics such as Windows Performance Counters for detailed
 insight into instance performance.
- [Use
 the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).
- For ongoing monitoring and analysis, consider using the [Amazon Kinesis Agent for Windows](https://docs.aws.amazon.com/kinesis-agent-windows/latest/userguide/what-is-kinesis-agent-windows.html) to monitor Windows Performance Counters for
 performance trend analysis of key system metrics.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
