<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-delete-profile.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Deleting an agent profile

AWS Well-Architected Agent is in preview release and is subject to change.


###### Important

Deleting an agent profile also deletes all goals, application contexts, and
 recommendations in the profile. Before deleting, verify that you have saved any information
 you may need from the profile.

## Console

###### To delete a profile

1. Choose **Agent profiles** in the left-hand navigation.
2. Choose **Actions** on the profile, then **Delete
 profile**.
3. Confirm the deletion.

If the **Delete profile** option is unavailable (grayed out),
 termination protection is enabled on the profile. Disable it first:

###### To disable termination protection

1. Choose **Agent profiles** in the left-hand navigation.
2. Choose **Actions** on the profile, then **Edit
 profile**.
3. In **Permissions and Integrations**, disable the
 **Termination protection** toggle.
4. Choose **Save**.

After disabling termination protection, return to **Agent profiles**
 and delete the profile using **Actions**, **Delete
 profile**.

## CLI

To delete a profile:

```
aws wellarchitected delete-agent-profile \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
"
```

###### Note

If deletion protection is enabled, you must first disable it using
 `UpdateAgentProfile` with `--deletion-protection false` before
 deleting the profile.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-delete-profile.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
