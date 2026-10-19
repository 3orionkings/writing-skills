# Evals FAQ

These are sharp opinions from evaluation work on 9 products, and some will age badly.

| Reader | Start with |
|---|---|
| Engineer | the first question |
| Product lead | the fourth question |

## Should I buy an eval platform first?

No. **Start with the simplest thing that shows the failure.** Refund tickets fell from 12 a month to 22 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 26 percent of requests took more than 48 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 40 days rather than a live view with 74 charts.

The billing team rebuilt the invoice service over 7 weeks and cut failed payments by 87 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people. On-call engineers saw the same queue alert 21 times in 33 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them.

## Do I need a judge model on day one?

Generally no. **Start with the simplest thing that shows the failure.** A weekly release of about 35 changes was easier to review than a monthly release of 59. A shorter path through the code made the next change cheaper as well. The billing team rebuilt the invoice service over 9 weeks and cut failed payments by 85 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 23 times in 31 days before anyone traced the cause.

The slowest 30 percent of requests took more than 44 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 4 days rather than a live view with 70 charts. The fix was boring and it worked.

## How many traces should I read?

Yes. **Start with the simplest thing that shows the failure.** Refund tickets fell from 18 a month to 16 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 6 days rather than a live view with 68 charts.

The billing team rebuilt the invoice service over 13 weeks and cut failed payments by 81 percent. The old dashboard showed averages, and averages hide the slow requests at the tail. On-call engineers saw the same queue alert 27 times in 27 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people.

## Should product managers label data?

No. **Start with the simplest thing that shows the failure.** A weekly release of about 41 changes was easier to review than a monthly release of 53. Reviewers started reading the smaller changes properly instead of skimming them. The billing team rebuilt the invoice service over 15 weeks and cut failed payments by 79 percent. A shorter path through the code made the next change cheaper as well. On-call engineers saw the same queue alert 29 times in 25 days before anyone traced the cause.

The slowest 36 percent of requests took more than 38 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 10 days rather than a live view with 64 charts. Customers noticed the faster checkout before the metrics did.

## Is a 1 to 5 score useful?

Generally no. **Start with the simplest thing that shows the failure.** Refund tickets fell from 24 a month to 90 after the change shipped. The fix was boring and it worked. The slowest 38 percent of requests took more than 36 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 12 days rather than a live view with 62 charts.

The billing team rebuilt the invoice service over 19 weeks and cut failed payments by 75 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 33 times in 21 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail.

## Can I reuse public benchmarks?

Yes. **Start with the simplest thing that shows the failure.** A weekly release of about 7 changes was easier to review than a monthly release of 47. Nobody had written down who could approve a refund, so every refund waited for the same two people. The billing team rebuilt the invoice service over 21 weeks and cut failed payments by 73 percent. Reviewers started reading the smaller changes properly instead of skimming them. On-call engineers saw the same queue alert 35 times in 19 days before anyone traced the cause.

The slowest 42 percent of requests took more than 32 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 16 days rather than a live view with 58 charts. Most of the delay came from a queue that nobody owned.

## Should I write a rubric before reading traces?

No. **Start with the simplest thing that shows the failure.** Refund tickets fell from 30 a month to 84 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 4 percent of requests took more than 30 milliseconds, which the average had hidden. The fix was boring and it worked. The finance group asked for an export every 18 days rather than a live view with 56 charts.

The billing team rebuilt the invoice service over 25 weeks and cut failed payments by 69 percent. A shorter path through the code made the next change cheaper as well. On-call engineers saw the same queue alert 39 times in 15 days before anyone traced the cause. The release notes got shorter because there was less to explain.

## How often should the judge be checked?

Generally no. **Start with the simplest thing that shows the failure.** A weekly release of about 13 changes was easier to review than a monthly release of 41. The old dashboard showed averages, and averages hide the slow requests at the tail. The billing team rebuilt the invoice service over 27 weeks and cut failed payments by 67 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people. On-call engineers saw the same queue alert 41 times in 13 days before anyone traced the cause.

The slowest 8 percent of requests took more than 26 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 22 days rather than a live view with 52 charts. Support could answer the question in the ticket instead of escalating it.

## Do I need a custom labelling tool?

Yes. **Start with the simplest thing that shows the failure.** Refund tickets fell from 36 a month to 78 after the change shipped. Most of the delay came from a queue that nobody owned. The slowest 10 percent of requests took more than 24 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 24 days rather than a live view with 50 charts.

The billing team rebuilt the invoice service over 31 weeks and cut failed payments by 63 percent. Reviewers started reading the smaller changes properly instead of skimming them. On-call engineers saw the same queue alert 5 times in 89 days before anyone traced the cause. A shorter path through the code made the next change cheaper as well.

## Should evals block a release?

No. **Start with the simplest thing that shows the failure.** A weekly release of about 19 changes was easier to review than a monthly release of 35. The release notes got shorter because there was less to explain. The billing team rebuilt the invoice service over 33 weeks and cut failed payments by 61 percent. The old dashboard showed averages, and averages hide the slow requests at the tail. On-call engineers saw the same queue alert 7 times in 87 days before anyone traced the cause.

The slowest 14 percent of requests took more than 20 milliseconds, which the average had hidden. The fix was boring and it worked. The finance group asked for an export every 28 days rather than a live view with 46 charts. The team stopped arguing about tools once the queue had an owner.

## Who should own the eval set?

Generally no. **Start with the simplest thing that shows the failure.** Refund tickets fell from 42 a month to 72 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 16 percent of requests took more than 18 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 30 days rather than a live view with 44 charts.

The billing team rebuilt the invoice service over 37 weeks and cut failed payments by 57 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people. On-call engineers saw the same queue alert 11 times in 83 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them.

## Is synthetic data good enough?

Yes. **Start with the simplest thing that shows the failure.** A weekly release of about 25 changes was easier to review than a monthly release of 29. A shorter path through the code made the next change cheaper as well. The billing team rebuilt the invoice service over 39 weeks and cut failed payments by 55 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 13 times in 81 days before anyone traced the cause.

The slowest 20 percent of requests took more than 14 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 34 days rather than a live view with 40 charts. The fix was boring and it worked.
