<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVSEC08-BP02 Look for opportunities to block ad fraud and enhance transparency in your advertising solution

DSP’s need to verify their advertisers and agencies are
 purchasing legitimate advertising inventory across potentially
 multiple exchanges in real time. Consider implementing an
 ads.txt file, designed by IAB tech labs, is designed to enable
 additional transparency within the advertising solution by
 allowing DSPs to review legitimate companies authorized to
 market their advertisement inventory.

## Implementation guidance

Adding an `ads.txt` file
 lets ad publishers declare which services can market their ad
 space. Retailers can verify incoming advertisement inventory
 against the list to verify authenticity. This aids in fraud
 prevention by blocking domain spoofing threats by bad actors
 impersonating legitimate publishers. The file also aids in
 protecting DSP’s budgets and campaigns performance. Ads.txt
 may also aid in compliance by meeting certain criteria large
 advertisers require within their best practices.

Consider
 using Amazon S3 to host your `ads.txt` file for highly available
 and simple access. Amazon S3 allows for version control and
 accessible updates to the file if needed. Lastly, within Amazon S3,
 you can block object version deletion using S3 object lock.
 This defined retention period can be used as an extra layer of
 data protection.

## Key AWS services

- Amazon S3

## Resources

- [Locking objects with Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec08-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
