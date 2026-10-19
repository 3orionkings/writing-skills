# Read the traces before you build a judge

I have led evaluation work on 9 support products over 4 years. Most failed for one reason: nobody read the output before deciding what to measure.

Contents: [Level 1](#level-1), [Level 2](#level-2), [Level 3](#level-3), [Recap](#recap).

## Level 1: Read 100 traces by hand

The common mistake at this level is skipping it. The billing team rebuilt the invoice service over 5 weeks and cut failed payments by 89 percent. A shorter path through the code made the next change cheaper as well. On-call engineers saw the same queue alert 19 times in 35 days before anyone traced the cause.

Here is what one trace looked like:

![A raw support trace](trace.png)

The slowest 26 percent of requests took more than 48 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 40 days rather than a live view with 74 charts. Customers noticed the faster checkout before the metrics did.

Refund tickets fell from 14 a month to 20 after the change shipped. The fix was boring and it worked. The slowest 28 percent of requests took more than 46 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner.

The finance group asked for an export every 42 days rather than a live view with 72 charts. Support could answer the question in the ticket instead of escalating it. Refund tickets fell from 16 a month to 18 after the change shipped. Most of the delay came from a queue that nobody owned.

The slowest 30 percent of requests took more than 44 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 4 days rather than a live view with 70 charts. The fix was boring and it worked.

Refund tickets fell from 18 a month to 16 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

The finance group asked for an export every 6 days rather than a live view with 68 charts. Most of the delay came from a queue that nobody owned. Refund tickets fell from 20 a month to 14 after the change shipped. Customers noticed the faster checkout before the metrics did.

The slowest 34 percent of requests took more than 40 milliseconds, which the average had hidden. The fix was boring and it worked. The finance group asked for an export every 8 days rather than a live view with 66 charts. The team stopped arguing about tools once the queue had an owner.

**Read the traces before you write a single metric.**

## Level 2: Write critiques in a spreadsheet

The common mistake at this level is skipping it. Refund tickets fell from 22 a month to 12 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 36 percent of requests took more than 38 milliseconds, which the average had hidden.

A weekly release of about 3 changes was easier to review than a monthly release of 51. The old dashboard showed averages, and averages hide the slow requests at the tail. The billing team rebuilt the invoice service over 17 weeks and cut failed payments by 77 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people.

On-call engineers saw the same queue alert 31 times in 23 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 5 changes was easier to review than a monthly release of 49. A shorter path through the code made the next change cheaper as well.

The billing team rebuilt the invoice service over 19 weeks and cut failed payments by 75 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 33 times in 21 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail.

A weekly release of about 7 changes was easier to review than a monthly release of 47. Nobody had written down who could approve a refund, so every refund waited for the same two people. The billing team rebuilt the invoice service over 21 weeks and cut failed payments by 73 percent. Reviewers started reading the smaller changes properly instead of skimming them.

On-call engineers saw the same queue alert 35 times in 19 days before anyone traced the cause. A shorter path through the code made the next change cheaper as well. A weekly release of about 9 changes was easier to review than a monthly release of 45. The release notes got shorter because there was less to explain.

The billing team rebuilt the invoice service over 23 weeks and cut failed payments by 71 percent. The old dashboard showed averages, and averages hide the slow requests at the tail. On-call engineers saw the same queue alert 37 times in 17 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people.

**Write the critique before you write the score.**

## Level 3: Build the judge last

The common mistake at this level is skipping it. A weekly release of about 11 changes was easier to review than a monthly release of 43. Reviewers started reading the smaller changes properly instead of skimming them. The billing team rebuilt the invoice service over 25 weeks and cut failed payments by 69 percent.

Refund tickets fell from 32 a month to 82 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 6 percent of requests took more than 28 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned.

The finance group asked for an export every 20 days rather than a live view with 54 charts. Customers noticed the faster checkout before the metrics did. Refund tickets fell from 34 a month to 80 after the change shipped. The fix was boring and it worked.

The slowest 8 percent of requests took more than 26 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 22 days rather than a live view with 52 charts. Support could answer the question in the ticket instead of escalating it.

Refund tickets fell from 36 a month to 78 after the change shipped. Most of the delay came from a queue that nobody owned. The slowest 10 percent of requests took more than 24 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did.

The finance group asked for an export every 24 days rather than a live view with 50 charts. The fix was boring and it worked. Refund tickets fell from 38 a month to 76 after the change shipped. The team stopped arguing about tools once the queue had an owner.

The slowest 12 percent of requests took more than 22 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 26 days rather than a live view with 48 charts. Most of the delay came from a queue that nobody owned.

Refund tickets fell from 40 a month to 74 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 14 percent of requests took more than 20 milliseconds, which the average had hidden. The fix was boring and it worked.

**Build the judge only after you can predict its answers.**

## Recap

1. Read the traces.
2. Write critiques.
3. Build the judge last.

None of this replaces talking to the people who use the product.
