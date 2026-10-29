<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-filter-rec.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Filter recommendations in AWS Well-Architected Agent

AWS Well-Architected Agent is in preview release and is subject to change.


Use filters to narrow down recommendations based on specific criteria to focus on the most
 relevant optimizations for your environment and priorities.

## Console

The Filters panel on the left side of the dashboard allows you to refine recommendations
 by:

- **Type:** Application, Architecture, or Resource-level
 recommendations
- **Pillars:** Cost Optimization, Security, Resilience, or
 Performance
- **Effort:** Small, Medium, or Large effort to fix
- **Impact:** High, Medium, or Low impact fixes
- **Services:** Select services from the list

You can select multiple filter criteria simultaneously. The **Clear
 filters** button removes all applied filters to return to the full
 recommendations view.

You can use the search bar to find a specific recommendation using keywords or
 recommendation names.

## CLI

To filter recommendations by state (open or closed):

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
" \
    --state OPEN
```

To filter by pillar:

```
aws wellarchitected list-agent-recommendations \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
" \
    --pillar COST_OPTIMIZATION
```

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-filter-rec.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
