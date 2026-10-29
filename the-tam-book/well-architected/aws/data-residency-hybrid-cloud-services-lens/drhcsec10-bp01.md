<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec10-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCSEC10-BP01 Update your threat models to cover the accidental or malicious storage of data in unauthorized locations

Threat models should include specific
 scenarios where the threat is data stored in unauthorized
 locations due to accidental storage as well as maliciously
 intent.

**Desired outcome:** Threat models
 cover all risks to data residency compliance.

**Common anti-patterns:**

- Threat models do not include specific location of data as a
 risk

**Benefits of establishing this best
 practice:** Up to date threat models help prepare people
 to respond to incidents.

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

- Review existing threat models, and remediate if they don't
 already address exfiltration to unauthorized internal
 accounts, unauthorized external accounts, or locations
 outside of AWS.
- Add threat scenarios where data is stored in an unauthorized
 location, such as in any or specific Regions, due to data
 residency policies within the same account.

## Resources

**Related documentation:**

- [How
 to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcsec10-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
