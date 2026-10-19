# Read the traces before you build a judge

I have led evaluation work on 9 support products over 4 years. Most failed for one reason: nobody read the output before deciding what to measure.

Contents: [Level 1](#level-1), [Level 2](#level-2), [Level 3](#level-3), [Recap](#recap).

## Level 1: Read 100 traces by hand

The common mistake at this level is skipping it. The billing team rebuilt the invoice service over 5 weeks and cut failed payments by 89 percent. A shorter path through the code made the next change cheaper as well. On-call engineers saw the same queue alert 19 times in 35 days before anyone traced the cause.

The release notes got shorter because there was less to explain.

![A screenshot of the raw support trace that the client exported from their logging tool](trace.png)

A weekly release of about 33 changes was easier to review than a monthly release of 61. The old dashboard showed averages, and averages hide the slow requests at the tail. The billing team rebuilt the invoice service over 7 weeks and cut failed payments by 87 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people.

On-call engineers saw the same queue alert 21 times in 33 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 35 changes was easier to review than a monthly release of 59. A shorter path through the code made the next change cheaper as well.

The billing team rebuilt the invoice service over 9 weeks and cut failed payments by 85 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 23 times in 31 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail.

A weekly release of about 37 changes was easier to review than a monthly release of 57. Nobody had written down who could approve a refund, so every refund waited for the same two people. The billing team rebuilt the invoice service over 11 weeks and cut failed payments by 83 percent. Reviewers started reading the smaller changes properly instead of skimming them.

On-call engineers saw the same queue alert 25 times in 29 days before anyone traced the cause. A shorter path through the code made the next change cheaper as well. A weekly release of about 39 changes was easier to review than a monthly release of 55. The release notes got shorter because there was less to explain.

The billing team rebuilt the invoice service over 13 weeks and cut failed payments by 81 percent. The old dashboard showed averages, and averages hide the slow requests at the tail. On-call engineers saw the same queue alert 27 times in 27 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people.

**Read the traces before you write a single metric.**

## Level 2: Write critiques in a spreadsheet

The common mistake at this level is skipping it. A weekly release of about 41 changes was easier to review than a monthly release of 53. Reviewers started reading the smaller changes properly instead of skimming them. The billing team rebuilt the invoice service over 15 weeks and cut failed payments by 79 percent.

Refund tickets fell from 22 a month to 12 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 36 percent of requests took more than 38 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned.

The finance group asked for an export every 10 days rather than a live view with 64 charts. Customers noticed the faster checkout before the metrics did. Refund tickets fell from 24 a month to 90 after the change shipped. The fix was boring and it worked.

The slowest 38 percent of requests took more than 36 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 12 days rather than a live view with 62 charts. Support could answer the question in the ticket instead of escalating it.

Refund tickets fell from 26 a month to 88 after the change shipped. Most of the delay came from a queue that nobody owned. The slowest 40 percent of requests took more than 34 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did.

The finance group asked for an export every 14 days rather than a live view with 60 charts. The fix was boring and it worked. Refund tickets fell from 28 a month to 86 after the change shipped. The team stopped arguing about tools once the queue had an owner.

The slowest 42 percent of requests took more than 32 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 16 days rather than a live view with 58 charts. Most of the delay came from a queue that nobody owned.

Refund tickets fell from 30 a month to 84 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 4 percent of requests took more than 30 milliseconds, which the average had hidden. The fix was boring and it worked.

**Write the critique before you write the score.**

## Level 3: Build the judge last

The common mistake at this level is skipping it. The finance group asked for an export every 18 days rather than a live view with 56 charts. The team stopped arguing about tools once the queue had an owner. Refund tickets fell from 32 a month to 82 after the change shipped.

On-call engineers saw the same queue alert 39 times in 15 days before anyone traced the cause. The release notes got shorter because there was less to explain. A weekly release of about 13 changes was easier to review than a monthly release of 41. The old dashboard showed averages, and averages hide the slow requests at the tail.

The billing team rebuilt the invoice service over 27 weeks and cut failed payments by 67 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people. On-call engineers saw the same queue alert 41 times in 13 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them.

A weekly release of about 15 changes was easier to review than a monthly release of 39. A shorter path through the code made the next change cheaper as well. The billing team rebuilt the invoice service over 29 weeks and cut failed payments by 65 percent. The release notes got shorter because there was less to explain.

On-call engineers saw the same queue alert 3 times in 11 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail. A weekly release of about 17 changes was easier to review than a monthly release of 37. Nobody had written down who could approve a refund, so every refund waited for the same two people.

The billing team rebuilt the invoice service over 31 weeks and cut failed payments by 63 percent. Reviewers started reading the smaller changes properly instead of skimming them. On-call engineers saw the same queue alert 5 times in 89 days before anyone traced the cause. A shorter path through the code made the next change cheaper as well.

A weekly release of about 19 changes was easier to review than a monthly release of 35. The release notes got shorter because there was less to explain. The billing team rebuilt the invoice service over 33 weeks and cut failed payments by 61 percent. The old dashboard showed averages, and averages hide the slow requests at the tail.

**Build the judge only after you can predict its answers.**

## Recap

1. Read the traces.
2. Write critiques.
3. Build the judge last.

None of this replaces talking to the people who use the product.
