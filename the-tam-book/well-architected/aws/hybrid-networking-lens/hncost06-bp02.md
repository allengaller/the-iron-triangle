<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST06-BP02 Separate traffic classes for dedicated connections

Create multiple dedicated connections for distinct traffic classes
 such as production versus backups. Assign guaranteed bandwidth to
 critical dedicated connections and use best-effort routing for
 dedicated connections.

**Desired outcome:** Cost-effective
 traffic segregation with guaranteed SLAs for priority workloads.

**Level of risk exposed if this best
 practice is not established:** Low

**Benefits of establishing this best
 practice:**

- Simplifies cost allocation by traffic type
- Enables independent scaling of traffic classes
- Complies with network isolation requirements

## Implementation guidance

- Configure separate BGP communities for dedicated connection.
 For example, you can achieve this using AWS Direct Connection
 VIFs on dedicated connections.

### Resources

- [Direct
 Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
