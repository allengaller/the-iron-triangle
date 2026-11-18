<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-edit-goals.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Editing goals

AWS Well-Architected Agent is in preview release and is subject to change.


###### Important

Each profile requires at least one goal. If you delete all goals from a profile,
 scheduled recommendations are not generated until you add a new goal.

## Console

Goals can be added either in **Agent profiles** or in the
 **Dashboard** for the profile.

###### To add goals from the profile

1. Choose **Agent profiles** in the left-hand navigation.
2. Choose **Actions**, then **Edit profile**.
3. In **Optimization pillars**, enter a free text goal statement for
 each optimization pillar you are reviewing.
NoteConcrete, specific goals help AWS WA Agent prioritize and recommend actions. For example,
 "optimize costs" is vague, while "optimize cost of X and Y AWS service by 15%" is
 specific and measurable.
4. After entering goals, choose **Save**.

###### To add goals from the dashboard

1. Choose **Dashboard** in the left-hand navigation.
2. Verify that you have the correct profile selected under
 **Profile**.
3. On the right side of the screen, choose the **pencil icon** in
 **Your goals**.
4. Enter, update, or remove **Optimization pillars** and
 **Goal statements**.
5. Choose **Save**.

## CLI

To create a new goal:

```
aws wellarchitected create-agent-goal \
    --profile-arn "
profile-arn
" \
    --title "
Reduce EC2 spend by 20%
" \
    --pillars COST_OPTIMIZATION
```

To update an existing goal:

```
aws wellarchitected update-agent-goal \
    --profile-arn "
profile-arn
" \
    --goal-id "
goal-id
" \
    --title "
Updated goal statement
"
```

To delete a goal:

```
aws wellarchitected delete-agent-goal \
    --profile-arn "
profile-arn
" \
    --goal-id "
goal-id
"
```

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-edit-goals.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
