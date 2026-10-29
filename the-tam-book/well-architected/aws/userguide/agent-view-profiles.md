<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-view-profiles.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Viewing your agent profiles

AWS Well-Architected Agent is in preview release and is subject to change.


## Console

To view a list of your profiles, choose **Agent profiles** in the
 left-hand navigation.

This view lists all of your configured AWS WA Agent profiles, along with action required
 notices for misconfigured profiles. From this page, you can:

- Choose **Go to Dashboard** to view recommendations for a
 profile.
- Choose **See profile details** to view the profile details
 page.
- Choose **Actions** to edit the profile, copy the profile ARN, or
 delete the profile.

The profile details page displays:

- **Profile summary:** Host account, goals, accounts in
 the profile, AWS Regions, optimization pillars, applications, termination protection
 status, and a copiable **Execution role ARN** for the profile.
- **Next steps (optional):** Provides optional next steps
 for the profile when the particular actions haven't been taken. You can choose
 **Provide profile access to team members** to share a profile with
 team members, or choose **Create applications with context** to define
 application context in the profile.

The profile details page has multiple tabs:

- **Accounts in profile:** Lists accounts configured for
 the profile. You can edit accounts and filter by Region.
- **Profile Access:** Shows AWS accounts with access to
 this profile and their access level (read or read/write). You can provide access to
 additional accounts or remove access.
- **Applications:** Lists application contexts defined for
 the profile. You can add, edit, or delete application contexts, and search or filter by
 Region.

## CLI

To list all agent profiles in your account:

```
aws wellarchitected list-agent-profiles
```

To view details for a specific profile:

```
aws wellarchitected get-agent-profile \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
"
```

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-view-profiles.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
