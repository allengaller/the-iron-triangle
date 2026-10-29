<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/change-management.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Change nanagement

Reliable rollback and recovery procedures verify that failed changes
 do not compromise the availability, continuity, or data integrity of
 life sciences research workloads. Rollbacks must be predictable,
 validated, and automated where possible so that operations can
 resume quickly. In GxP-regulated environments, these same procedures
 also support regulatory requirements by providing auditable recovery
 evidence. Effective change management must also assess risks of,
 validate, and document changes so the system remains in a controlled
 and compliant state throughout its lifecycle.

Reliability testing for life sciences workloads must validate both
 technical resilience (availability, fault tolerance, performance
 under stress) and regulatory adherence (GxP, data integrity). A
 structured testing strategy verifies that workloads perform
 predictably under normal and adverse conditions, failures are
 anticipated and contained, and evidence is generated as part of
 system validation.

###### Best practices

- [LSREL09-BP01 Create and verify rollback plans](./lsrel09-bp01.html)
- [LSREL09-BP02 Implement safe deployment strategies (like blue/green or canary)](./lsrel09-bp02.html)
- [LSREL09-BP03 Verify data integrity and point-in-time recovery](./lsrel09-bp03.html)
- [LSREL09-BP04 Maintain auditable rollback and recovery records](./lsrel09-bp04.html)
- [LSREL09-BP05 Implement risk-based change control for validated systems](./lsrel09-bp05.html)
- [LSREL09-BP06 Automate validation testing for changes](./lsrel09-bp06.html)
- [LSREL10-BP01 Implement comprehensive reliability testing](./lsrel10-bp01.html)
- [LSREL10-BP02 Validate end-to-end reliability of regulated workloads](./lsrel10-bp02.html)
- [LSREL10-BP03 Test data integrity under failure conditions](./lsrel10-bp03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/change-management.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
