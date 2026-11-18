<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-architecture-reviews.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Conducting architecture reviews

AWS Well-Architected Agent is in preview release and is subject to change.


Architecture reviews analyze your infrastructure as code (IaC) templates against the AWS
 Well-Architected Framework and return deployment-ready updated templates with best-practice fixes
 applied. Unlike resource and application recommendations, architecture reviews target templates
 before deployment, enabling you to identify and resolve issues before they reach
 production.

Unlike Resource and Application recommendations, AWS WA Agent, Architecture type recommendations are not automatically
 generated. You must manually conduct an architecture review to generate them.

## Supported input formats

You provide an Amazon S3 URI containing your infrastructure as code (IaC) templates for an
 architecture review. AWS CDK and Terraform projects are supported. The following input types
 are accepted:

- **.zip file:** A compressed archive of
 your IaC project files. The .zip file cannot exceed 25 MB.
- **Amazon S3 folder:** A folder in Amazon S3
 containing your IaC project files. The total folder size cannot exceed 100 MB, and no
 individual file can exceed 1 MB.

AWS WA Agent validates submitted files and rejects requests that contain malicious content or
 files that exceed these size limits. Binary and media files are excluded from the
 review.

## Conducting a review

### Console

###### To conduct an architecture review

1. In the AWS WA Agent dashboard, choose **Architecture
 review**.
2. In Review details, enter a name for your architecture review. The name must
 contain only letters, numbers, hyphens (-), and underscores (_). Spaces and special
 characters are not permitted.
3. Upload your file using an S3 URI. Then, choose an **Object version**. You can also choose **Browse S3** to explore files in your S3 buckets.
NoteAWS WA Agent expects that your S3 buckets are in the same AWS Region as your agent profile. If you cannot find your IaC files, verify that they're in an S3 bucket in the same Region as your profile.
4. Select the consent checkbox to allow AWS WA Agent to access the contents of the file. Without selecting this checkbox, you cannot run an architecture review.
5. Select the **Well-Architected Framework** lens. This is the
 only lens available for architecture reviews at this time.
6. Select which pillars you want to review.
7. Choose **Start review**.

### CLI

Use the `StartAgentRecommendationGeneration` API to start an architecture
 review. Only the `ARCHITECTURE` recommendation type is supported for on-demand
 generation. Resource and application recommendations are generated exclusively through the
 scheduled refresh cycle and cannot be triggered on demand.

The following parameters control the review request:

The name of the architecture review. The name can be 1 to 128
 characters and must contain only letters, numbers, hyphens (-), and underscores (_).
 Spaces and special characters are not permitted.

The recommendation types to generate. Specify
 `ARCHITECTURE`.

A JSON object that defines what the review covers. Required for architecture
 reviews.

A list of Well-Architected pillars to review. Valid values:
 `COST_OPTIMIZATION`, `SECURITY`,
 `RESILIENCE`, `PERFORMANCE`.

A list of up to 10 optimization goal IDs to prioritize the review
 against. You can retrieve goal IDs using
 `ListAgentGoals`. For information about creating goals, see
 [Editing goals](./agent-edit-goals.html).

A per-pillar filter that narrows the review to specific items.
 Each object has two required members: `pillar` (a single pillar
 value) and `ids` (a list of item IDs to process for that pillar,
 such as best practice IDs like `SEC02-BP02`, AWS service names,
 or resource ARNs). When `items` is omitted, all items are processed
 for the selected pillars.

A JSON object specifying the IaC template location and lens selection. An
 architecture review analyzes an IaC template, so you provide the template location
 through this parameter.

The Amazon S3 URI of the IaC template, .zip archive, or folder to
 review.

The object version ID of the Amazon S3 object.

A list of lens ARNs to review against. Only the Well-Architected
 Framework lens (`arn:aws:wellarchitected::aws:lens/wellarchitected`)
 is supported for architecture reviews at this time.

```
aws wellarchitected start-agent-recommendation-generation \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
" \
    --types ARCHITECTURE \
    --name "
my-architecture-review
" \
    --scope '
{

  "pillars": ["COST_OPTIMIZATION", "SECURITY"]
}' \
    --additional-context '
{

  "s3Uri": "s3://
your-bucket
/
your-template.yaml
",
  "s3VersionId": "
optional-version-id
",
  "lensArns": ["arn:aws:wellarchitected::aws:lens/wellarchitected"]
}'
```

To monitor the status of an architecture review, use
 `GetAgentRecommendationGeneration` or
 `ListAgentRecommendationGenerations`:

```
aws wellarchitected list-agent-recommendation-generations \
    --profile-arn "
arn:aws:wellarchitected:us-east-1:111122223333:agent-profile/my-profile
"
```

## Architecture review limits

Architecture reviews are limited to 5 reviews per day per profile. You can run reviews
 consecutively while daily quota remains. Architecture reviews are not subject to the weekly
 scheduled recommendation generation cycle.

## Viewing review results

You can monitor the status of the review as it progresses or return to the AWS WA Agent
 dashboard by choosing **Go to dashboard**. The Reviews tab on the dashboard
 shows all your in-progress and completed reviews.

The generated recommendations include code in the same language as your source template.
 For example, if you upload a Terraform file, the updated template is returned as
 Terraform.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-architecture-reviews.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
