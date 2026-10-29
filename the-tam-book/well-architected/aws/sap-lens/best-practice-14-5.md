<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-14-5.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best Practice 14.5 – Choose appropriate backup solutions and schedule

Depending on the backup method, there is the potential to dramatically increase both
 read and write operations on your storage, which can negatively impact the performance of
 your application. This is particularly true for database level backups which might be
 large in volume and lengthy in duration.

**Suggestion 14.5.1 – Determine a suitable backup window**

Define what is the most appropriate window for the running of backup operations
 aligned to your business requirements. Consider key dependencies such as the overnight
 batch schedule and the acceptable runtime.

**Suggestion 14.5.2 – Consider options to minimize the performance
 impact of backups**

Analyze any storage or network constraints and evaluate options to minimize the
 impact of the backup. This may include reducing the duration by using delta change backups
 either at a database or storage level. Refer to the Reliability Pillar to ensure this does
 not negatively impact the consistency of backups or the overall restoration time.

- SAP Lens [Reliability]: [Best Practice 12.1 -
 Establish a method for consistent recovery of business data](./best-practice-12-1.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-14-5.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
