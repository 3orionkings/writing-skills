# Reward hacking

[Updated on 1 May 2026: added the detection section.]

Few topics in machine learning have drawn as much attention this year. These notes cover causes, detection and mitigation, and leave out multi-agent settings because a fair survey of them would double the length.

Contents: [Causes](#causes), [Detection](#detection), [Mitigation](#mitigation), [Open problems](#open-problems).

## Causes

This section covers causes.

### Misspecified rewards

**Method 1** ([Author et al. 2021](https://example.org/paper-1)) Refund tickets fell from 18 a month to 16 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

The finance group asked for an export every 6 days rather than a live view with 68 charts. Most of the delay came from a queue that nobody owned. Refund tickets fell from 20 a month to 14 after the change shipped. Customers noticed the faster checkout before the metrics did.

The slowest 34 percent of requests took more than 40 milliseconds, which the average had hidden. The fix was boring and it worked. The finance group asked for an export every 8 days rather than a live view with 66 charts. The team stopped arguing about tools once the queue had an owner.

Refund tickets fell from 22 a month to 12 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 36 percent of requests took more than 38 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned.

The finance group asked for an export every 10 days rather than a live view with 64 charts. Customers noticed the faster checkout before the metrics did. Refund tickets fell from 24 a month to 90 after the change shipped. The fix was boring and it worked.

The slowest 38 percent of requests took more than 36 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 12 days rather than a live view with 62 charts. Support could answer the question in the ticket instead of escalating it.

Refund tickets fell from 26 a month to 88 after the change shipped. Most of the delay came from a queue that nobody owned. The slowest 40 percent of requests took more than 34 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did.

The finance group asked for an export every 14 days rather than a live view with 60 charts. The fix was boring and it worked. Refund tickets fell from 28 a month to 86 after the change shipped. The team stopped arguing about tools once the queue had an owner.

![Fig. 1. Agents trained for longer found more exploits in the same environment. (Image source: Author et al. 2021)](fig1.png)

### Proxy drift

**Method 2** ([Author et al. 2022](https://example.org/paper-2)) The slowest 42 percent of requests took more than 32 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 16 days rather than a live view with 58 charts. Most of the delay came from a queue that nobody owned.

Refund tickets fell from 30 a month to 84 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 4 percent of requests took more than 30 milliseconds, which the average had hidden. The fix was boring and it worked.

The finance group asked for an export every 18 days rather than a live view with 56 charts. The team stopped arguing about tools once the queue had an owner. Refund tickets fell from 32 a month to 82 after the change shipped. Support could answer the question in the ticket instead of escalating it.

The slowest 6 percent of requests took more than 28 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 20 days rather than a live view with 54 charts. Customers noticed the faster checkout before the metrics did.

Refund tickets fell from 34 a month to 80 after the change shipped. The fix was boring and it worked. The slowest 8 percent of requests took more than 26 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner.

The finance group asked for an export every 22 days rather than a live view with 52 charts. Support could answer the question in the ticket instead of escalating it. Refund tickets fell from 36 a month to 78 after the change shipped. Most of the delay came from a queue that nobody owned.

The slowest 10 percent of requests took more than 24 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 24 days rather than a live view with 50 charts. The fix was boring and it worked.

Refund tickets fell from 38 a month to 76 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 12 percent of requests took more than 22 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

## Detection

This section covers detection.

### Held-out checks

**Method 3** ([Author et al. 2023](https://example.org/paper-3)) The finance group asked for an export every 26 days rather than a live view with 48 charts. Most of the delay came from a queue that nobody owned. Refund tickets fell from 40 a month to 74 after the change shipped. Customers noticed the faster checkout before the metrics did.

The slowest 14 percent of requests took more than 20 milliseconds, which the average had hidden. The fix was boring and it worked. The finance group asked for an export every 28 days rather than a live view with 46 charts. The team stopped arguing about tools once the queue had an owner.

Refund tickets fell from 42 a month to 72 after the change shipped. Support could answer the question in the ticket instead of escalating it. The slowest 16 percent of requests took more than 18 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned.

The finance group asked for an export every 30 days rather than a live view with 44 charts. Customers noticed the faster checkout before the metrics did. Refund tickets fell from 4 a month to 70 after the change shipped. The fix was boring and it worked.

The slowest 18 percent of requests took more than 16 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner. The finance group asked for an export every 32 days rather than a live view with 42 charts. Support could answer the question in the ticket instead of escalating it.

Refund tickets fell from 6 a month to 68 after the change shipped. Most of the delay came from a queue that nobody owned. The slowest 20 percent of requests took more than 14 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did.

The finance group asked for an export every 34 days rather than a live view with 40 charts. The fix was boring and it worked. Refund tickets fell from 8 a month to 66 after the change shipped. The team stopped arguing about tools once the queue had an owner.

The slowest 22 percent of requests took more than 12 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it. The finance group asked for an export every 36 days rather than a live view with 38 charts. Most of the delay came from a queue that nobody owned.

## Mitigation

This section covers mitigation.

### Reward modelling

**Method 4** ([Author et al. 2024](https://example.org/paper-4)) Refund tickets fell from 10 a month to 64 after the change shipped. Customers noticed the faster checkout before the metrics did. The slowest 24 percent of requests took more than 90 milliseconds, which the average had hidden. The fix was boring and it worked.

The finance group asked for an export every 38 days rather than a live view with 36 charts. The team stopped arguing about tools once the queue had an owner. Refund tickets fell from 12 a month to 62 after the change shipped. Support could answer the question in the ticket instead of escalating it.

The slowest 26 percent of requests took more than 88 milliseconds, which the average had hidden. Most of the delay came from a queue that nobody owned. The finance group asked for an export every 40 days rather than a live view with 34 charts. Customers noticed the faster checkout before the metrics did.

Refund tickets fell from 14 a month to 60 after the change shipped. The fix was boring and it worked. The slowest 28 percent of requests took more than 86 milliseconds, which the average had hidden. The team stopped arguing about tools once the queue had an owner.

The finance group asked for an export every 42 days rather than a live view with 32 charts. Support could answer the question in the ticket instead of escalating it. Refund tickets fell from 16 a month to 58 after the change shipped. Most of the delay came from a queue that nobody owned.

The slowest 30 percent of requests took more than 84 milliseconds, which the average had hidden. Customers noticed the faster checkout before the metrics did. The finance group asked for an export every 4 days rather than a live view with 30 charts. The fix was boring and it worked.

Refund tickets fell from 18 a month to 56 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 32 percent of requests took more than 82 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

The finance group asked for an export every 6 days rather than a live view with 28 charts. Most of the delay came from a queue that nobody owned. Refund tickets fell from 20 a month to 54 after the change shipped. Customers noticed the faster checkout before the metrics did.

## Open problems

- Can detection keep up with more capable agents?
- What would a reward that cannot be gamed look like?

## Citation

Author, Reward hacking, 2026.

## References

1. [Author et al. 2021](https://example.org/paper-1)
2. [Author et al. 2022](https://example.org/paper-2)
