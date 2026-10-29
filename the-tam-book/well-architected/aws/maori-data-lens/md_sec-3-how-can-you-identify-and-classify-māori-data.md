<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-3-how-can-you-identify-and-classify-māori-data.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MD_SEC 3: How can you identify and classify Māori data?

Organisations may wish to understand what Māori data they hold and have a method to
 classify Māori data to protect it with security controls and practices. Once the data has been
 classified and appropriate metadata is captured, you can govern and use that data in
 appropriate ways.

- **MD_SEC03-BP01: Develop an understanding of what Māori data
 is**. Create an easy-to-understand definition of Māori data for your
 organisation. Having a definition of Māori data can help determine what additional
 considerations are relevant to your organisation or application. Piloting this and testing
 this with your customers facilitates a mutually-agreed upon definition, which is
 implementable for your organisation.
- **MD_SEC03-BP02: Incorporate Māori data classification into your data
 governance framework**. If you already have a data classification framework
 within your organisation, you may wish to expand this to include a Māori data
 classification approach. A classification framework can help you determine what is Māori
 data, outline where and how the classification should be recorded, and define the security
 and access controls that are required for that data classification. For example, what
 additional data access controls may be required if the data is classified as tapu or noa?
- **MD_SEC03-BP03: Record Māori data classifications as metadata and
 make it easily discoverable**. Use approaches such as metadata tagging and data
 cataloguing to store and manage your classification metadata. Tools such as business data
 catalogues should make it easier for your organisation to search for and discover datasets
 that contain Māori data in your organisation. In addition, you can add tags which record
 the purpose for which consent of that data was given. This may allow for easier review of
 consent and data access policies and up-to-date consent practices.
- **MD_SEC03-BP04: Leverage technologies and techniques to help identify
 and classify existing Māori data**. Your organisation may already capture and
 store Māori data. Consider using available tools and techniques to review and classify
 your existing data. Once identified and classified, update your metadata and business data
 catalogues. This may involve assessing data across databases, object stores, file servers,
 document management systems, communication systems (like email), and analytics platforms.
 For example, search your AWS Glue Data Catalog table columns for terms like *iwi*
 or *hapū* or Māori organisation.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-3-how-can-you-identify-and-classify-māori-data.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
