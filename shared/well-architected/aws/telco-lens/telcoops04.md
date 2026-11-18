<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# IP verification

Telco's own large CIDR blocks of IP addresses and wish to have them represented with
 their ownership even when advertised by AWS. The IP address CIDR block are assigned to telco
 resources in the cloud and should be propagated through AWS to the Internet where both the
 CIDR block and the ASN associated with the prefixes are represented as owned by the telco.
 This improves the reputation of the address prefix propagated across the Internet for telco
 subscribers and gives CSPs responsibility and accountability of the address space.

###### Best practices

- [TELCOOPS04-BP01 Implement the Bring Your Own IP (BYOIP) address processes and associate the prefixes with the IPAM solution](./telcoops04-bp01.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
