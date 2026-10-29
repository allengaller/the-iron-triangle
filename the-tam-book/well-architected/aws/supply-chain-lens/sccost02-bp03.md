<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCCOST02-BP03 Only store useful data and discard the rest

A well-designed supply chain data management architecture
 incorporates a data lake to store processed and normalized useful
 data, while raw data is either discarded or archived in
 cost-effective storage for potential future needs.

**Desired outcome:** Data lifecycle
 is well defined as per business and regulatory requirements.

**Benefits of establishing this best
 practice:** Reduced cost, optimized performance, and
 better customer satisfaction

**Level of risk exposed if this best
 practice is not established:** Medium

## Implementation guidance

Implement data sanitization to identify, clean, and validate
 critical information before cloud transfer, while pre-processing
 data to improve bandwidth efficiency, reduce storage costs, and
 support high-quality, secure cloud data.

Use edge computing for local analytics and decision-making,
 prioritizing critical data for immediate cloud transmission.

### Implementation steps

1. Establish data classification and retention policies that
 define what data should be kept, archived, or discarded
 based on business and regulatory requirements.
2. Implement automated data sanitization processes to clean
 and validate data before storage, removing unnecessary or
 redundant information.
3. Deploy edge computing solutions for local data processing
 and filtering, transmitting only essential data to the
 cloud.
4. Configure automated data lifecycle management to archive
 or delete data according to established retention
 policies.
5. Implement data quality monitoring to make sure only
 valuable, accurate data is retained in storage systems.
6. Regularly review and optimize data retention policies
 based on changing business needs and regulatory
 requirements.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost02-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
