<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-data-testing.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Anti-patterns for data testing

- **Testing data drift:** Testing data in environments that
 do not mirror production datasets can result in testing outdated data schemas, different
 configurations, or testing data not representative of real-world conditions. Tests that
 pass in a non-representative environment might fail in production, leading to undetected
 data issues. Ensure that testing environments mirror production as closely as possible,
 both in terms of configuration and the nature of the data. Regularly update testing
 environment datasets to reflect changes in production.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-data-testing.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
