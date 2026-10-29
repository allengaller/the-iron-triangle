<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-test-environment-management.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Metrics for test environment management

- **Test bed provisioning time:** The duration spent
 provisioning a test environment including all supporting infrastructure and data
 saturation. This metric indicates inefficiencies in the overall test bed provisioning
 process. Measure the time difference between the start of provisioning to when the
 environment is confirmed as ready to run a test case.
- **Test case execution time:** The duration taken to run a
 test case or a suite of test cases. Faster test execution speeds indicate efficient test
 environment and execution management which allows for rapid iterations and feedback.
 Improve this metric by optimizing test bed provisioning, ensuring efficient resource
 allocation, and parallelizing test runs. Measure the timestamp difference between the
 start and end of test case execution.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-test-environment-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
