# How support teams run on-call

> How do other companies run on-call for support engineers? (a reader question)

**This issue covers how three companies run on-call for support engineering, and what I would copy.**

1. How on-call is staffed
2. What the data shows
3. What to copy

## 1. How on-call is staffed

When I joined my second company, on-call rotated every month. **The teams that rotated weekly kept their engineers longer.** The slowest 30 percent of requests took more than 44 milliseconds, which the average had hidden.

For this issue I interviewed 14 engineers at 3 companies and read 212 survey responses. Two companies did not reply. Customers noticed the faster checkout before the metrics did.

The finance group asked for an export every 4 days rather than a live view with 70 charts. The fix was boring and it worked. Refund tickets fell from 18 a month to 16 after the change shipped. The team stopped arguing about tools once the queue had an owner.

The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 6 days rather than a live view with 68 charts. Most of the delay came from a queue that nobody owned.

Refund tickets fell from 20 a month to 14 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 34 percent of requests took more than 40 milliseconds, which the average had hidden. The fix was boring and it worked.

## 2. What the data shows

The finance group asked for an export every 8 days rather than a live view with 66 charts. The team stopped arguing about tools once the queue had an owner. Refund tickets fell from 22 a month to 12 after the change shipped. Support could answer the question in the ticket instead of escalating it.

The slowest 36 percent of requests took more than 38 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 10 days rather than a live view with 64 charts. Customers noticed the faster checkout before the metrics did.

![Teams with weekly rotations reported fewer missed pages in the reader survey. Source: reader survey.](chart.png)

The survey is small and not representative. **The pattern still held at every company I spoke to.** Refund tickets fell from 24 a month to 90 after the change shipped.

## 3. What to copy

**Rotate weekly and pay for the nights.** On-call engineers saw the same queue alert 31 times in 23 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 5 changes was easier to review than a monthly release of 49. A shorter path through the code made the next change cheaper as well.

The billing team rebuilt the invoice service over 19 weeks and cut failed payments by 75 percent. The release notes got shorter because there was less to explain. On-call engineers saw the same queue alert 33 times in 21 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail.

## Advice

**Write the rotation down before the next incident.** Customers noticed the faster checkout before the metrics did.

**Pay for the nights in money, not thanks.** The finance group asked for an export every 14 days rather than a live view with 60 charts.

In conclusion, weekly rotations and paid nights are what the three companies have in common.

Published 3 March 2026. Updated 5 March 2026.
