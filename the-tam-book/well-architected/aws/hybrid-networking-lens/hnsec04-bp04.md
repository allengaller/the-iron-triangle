<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC04-BP04 Implement DNS security controls

DNS security control protects against DNS threats such as data
 exfiltration. You can create blocklists and allowlists to manage
 which domains your resources can query through DNS.

**Desired outcome:** Prevent data
 exfiltration and block malicious domains at the DNS layer in hybrid
 networks.

**Level of risk exposed if this best practice
 is not established:** Medium

**Benefits of establishing this best
 practice:**

- Blocks DNS-based attacks and data exfiltration
- Provides centralized control over DNS traffic
- Enables logging and reporting for compliance

## Implementation guidance

- Define DNS firewall rule groups for blocklists and allowlists.
- Associate DNS firewall rules with relevant networks.
- Monitor DNS queries and refine rules based on findings.

## Resources

- [How
 Resolver DNS Firewall works](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/resolver-dns-firewall-overview.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
