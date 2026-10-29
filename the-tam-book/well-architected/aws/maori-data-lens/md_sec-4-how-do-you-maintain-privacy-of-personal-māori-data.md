<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-4-how-do-you-maintain-privacy-of-personal-māori-data.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MD_SEC 4: How do you maintain privacy of personal Māori data?

It is important that personal data is collected and processed lawfully, fairly, and
 transparently in relation to a person. When designing, building, and operating workloads that
 may capture, store, and process Māori personal data, privacy should be taken into account
 throughout the entire process. The application of privacy principles should align with your
 organisation's privacy framework and be guided by applicable privacy regulation such as the
 New Zealand Privacy Act 2020. For further information on how you are applying AWS services
 in conjunction with the New Zealand Privacy Act 2020, see [Using AWS in the Context of the New Zealand Privacy Considerations](https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_New_Zealand_Privacy_Considerations.pdf).

- **MD_SEC04-BP01: Use tools and techniques to adequately de-identify
 data.** This helps protect individual's privacy when producing data sets that
 may be shared or published. There are many techniques within data and analytics domains to
 help de-identify data. These include obfuscation (obscuring sensitive data), tokenisation
 (where a sensitive piece of data is replaced by a non-sensitive token where the token can
 map back to the original data), and anonymisation (such as removing sensitive data
 completely).
- **MD_SEC04-BP02: Honour the consent you've received when using data
 for internal analytics**. If your organisation asked for consent when
 collecting data, that data should be used only for the purposes that you have received
 consent for. If your organisation asked for consent and did not receive it, exclude this
 data from analytics and AI/ML uses.
- **MD_SEC04-BP03: Honour the consent you've received when sharing
 data**. Only share data with third parties if you have obtained requisite
 consent in accordance with applicable laws such as the New Zealand Privacy Act. Consider
 creating mechanisms to exclude that data from any data sharing processes if you have not
 obtained the required consents.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-4-how-do-you-maintain-privacy-of-personal-māori-data.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
