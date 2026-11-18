<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/workload-and-scope.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Workload and scope

AWS Well-Architected Agent is in preview release and is subject to change.


According to the
 [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads.html):

A workload is more than cloud services or resources. It also
 includes people, teams, processes, and runbooks, along with the
 technology and infrastructure that deliver business value. Before
 running a WAFR, invest time to understand and document components of
 your workload. This can help you save time during the review phase.

## Choosing a workload for a WAFR

To prepare a workload for a WAFR, discuss the following questions
 with the team:

- Who owns the workload? Who is responsible if a disruption of
 the workload impacts the business?
- What is the purpose of the workload? Are there analytics for
 the business? Does it have a sandbox, training, and logging?
- Does this workload need to exist? What happens if you shut it
 down?
- Is the workload customer-facing or internal?
- Is the workload production or non-production?
- What phase is the workload in its lifecycle?
- What is the impact if the workload had a disruption?
- What are the boundaries of the workload?
- What dependencies does this workload have?

You should be able to clearly answer most of these questions when
 evaluating your workload before continuing with the WAFR.

## What is the scope of the review?

Although ultimately a WAFR spans
 [all
 pillars of the Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), we can identify trade-offs and
 understand the context before making decisions. A good way to
 start is to focus on prioritized pillars or a particular area of
 the workload.

Defining the larger review process, producing some actionable
 results, and iterating helps you produce more value for the
 workload and the business.

Consider a phased approach:

1. Identify two to three major pillars that are most relevant to
 the current business and technical context
2. Demonstrate the value of your workload within these pillars
3. After you get satisfactory results, repeat with more pillars

To reduce scope further, use lenses that are designed specifically
 for your workloads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/workload-and-scope.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
