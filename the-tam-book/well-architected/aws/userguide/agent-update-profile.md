<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-update-profile.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Updating an agent profile

AWS Well-Architected Agent is in preview release and is subject to change.


You can update a profile's display name, description, pillars, execution role, aggregation
 configuration, deletion protection, and business overview at any time.

## Console

###### To update a profile

1. Choose **Agent profiles** in the left-hand navigation.
2. Choose **Actions** on the profile, then **Edit
 profile**.
3. Update the fields you want to change.
4. Choose **Save**.

## CLI

###### Important

When you update a profile using the API or CLI (`UpdateAgentProfile`), you
 must specify all fields in the request, not only the fields you want to change. Any field
 omitted from the update request is reset to its default value or cleared. The update
 operation uses full replacement semantics (PUT), not partial update semantics (PATCH). The
 console handles this automatically by pre-populating all current values.

To avoid unintentionally clearing fields, retrieve the current profile configuration
 first, modify the values you want to change, then pass the full object back:

```
# 1. Get the current profile configuration
aws wellarchitected get-agent-profile \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
"

# 2. Update the profile with all fields specified
aws wellarchitected update-agent-profile \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
" \
    --display-name "
My Profile
" \
    --description "
Profile description
" \
    --pillars COST_OPTIMIZATION SECURITY \
    --execution-role-arn "
arn:aws:iam::111122223333:role/MyExecutionRole
" \
    --aggregation-configuration '
[
{
"accountId":"111122223333","regions":["us-east-1"],"accessRoleArn":"arn:aws:iam::111122223333:role/MyRole"}]
' \
    --deletion-protection \
    --business-overview "
Overview of the business context
"
```

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-update-profile.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
