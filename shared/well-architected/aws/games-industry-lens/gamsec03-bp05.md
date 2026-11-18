<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec03-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# GAMESEC03-BP05 Provide an option for players to set up multi-factor authentication (MFA) on their accounts

Player accounts can be an asset to bad actors, particularly in
 games that support in-game currency and purchases. Due to the
 pervasiveness of player account hacking and social engineering
 attacks, provide players with the option to enhance the security
 of their accounts by configuring multi-factor authentication
 (MFA).

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

When a player attempts to access their account by using MFA, a
 temporary code is sent to their email address, phone number, or a
 purpose-built multi-factor authentication mobile app. To
 successfully authenticate, the player must then enter the code
 into the login system within a limited time frame.

MFA can also be used to help protect accounts that are attempting
 to authenticate from a new geo-location, accounts that have been
 flagged by player support for potential malicious activity, and
 even for accounts that have not logged into the game for an
 extended period.

For example, Amazon Cognito user pools can
 [configure multi-factor
 authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) on user directories.

### Implementation steps

- Enable multi-factor authentication (MFA) to enhance player
 account security.
- Use temporary codes sent via email, phone, or MFA apps to
 verify account access.
- Apply MFA for new geo-locations, flagged accounts, or
 accounts with extended inactivity.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec03-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
