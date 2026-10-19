# The week in incidents

*The week in incidents is a series about outages and what they teach.*

This issue covers four topics.

1. **The payments outage.** Nobody had written down who could approve a refund, so every refund waited for the same two people.
2. **A new on-call rule.** The fix was boring and it worked.
3. **Cuts at a vendor.** Reviewers started reading the smaller changes properly instead of skimming them.
4. **A tool worth trying.** The team stopped arguing about tools once the queue had an owner.

## 1. The payments outage

At 09:14 the first alert fired. At 09:31 the status page still showed green. The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 6 days rather than a live view with 68 charts.

![](status.png)
***At 09:31 the status page still showed green. Source: [status page](https://example.org/status).***

## 2. A new on-call rule

The billing team rebuilt the invoice service over 13 weeks and cut failed payments by 81 percent. The old dashboard showed averages, and averages hide the slow requests at the tail. On-call engineers saw the same queue alert 27 times in 27 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people.

A weekly release of about 41 changes was easier to review than a monthly release of 53. Reviewers started reading the smaller changes properly instead of skimming them. The billing team rebuilt the invoice service over 15 weeks and cut failed payments by 79 percent. A shorter path through the code made the next change cheaper as well.

On-call engineers saw the same queue alert 29 times in 25 days before anyone traced the cause. The release notes got shorter because there was less to explain. A weekly release of about 3 changes was easier to review than a monthly release of 51. The old dashboard showed averages, and averages hide the slow requests at the tail.

The billing team rebuilt the invoice service over 17 weeks and cut failed payments by 77 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people. On-call engineers saw the same queue alert 31 times in 23 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them.

## 3. Cuts at a vendor

A weekly release of about 5 changes was easier to review than a monthly release of 49. A shorter path through the code made the next change cheaper as well. The billing team rebuilt the invoice service over 19 weeks and cut failed payments by 75 percent. The release notes got shorter because there was less to explain.

On-call engineers saw the same queue alert 33 times in 21 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail. A weekly release of about 7 changes was easier to review than a monthly release of 47. Nobody had written down who could approve a refund, so every refund waited for the same two people.

The billing team rebuilt the invoice service over 21 weeks and cut failed payments by 73 percent. Reviewers started reading the smaller changes properly instead of skimming them. On-call engineers saw the same queue alert 35 times in 19 days before anyone traced the cause. A shorter path through the code made the next change cheaper as well.

A weekly release of about 9 changes was easier to review than a monthly release of 45. The release notes got shorter because there was less to explain. The billing team rebuilt the invoice service over 23 weeks and cut failed payments by 71 percent. The old dashboard showed averages, and averages hide the slow requests at the tail.

## 4. A tool worth trying

On-call engineers saw the same queue alert 37 times in 17 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people. A weekly release of about 11 changes was easier to review than a monthly release of 43. Reviewers started reading the smaller changes properly instead of skimming them.

The billing team rebuilt the invoice service over 25 weeks and cut failed payments by 69 percent. A shorter path through the code made the next change cheaper as well. On-call engineers saw the same queue alert 39 times in 15 days before anyone traced the cause. The release notes got shorter because there was less to explain.

A weekly release of about 13 changes was easier to review than a monthly release of 41. The old dashboard showed averages, and averages hide the slow requests at the tail. The billing team rebuilt the invoice service over 27 weeks and cut failed payments by 67 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people.

On-call engineers saw the same queue alert 41 times in 13 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 15 changes was easier to review than a monthly release of 39. A shorter path through the code made the next change cheaper as well.

The status page has since been fixed, which is more than can be said for the vendor.
