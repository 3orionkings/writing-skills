# Patterns for support bots: what held up in production

> A model is only as good as the examples you check it against.

This post covers three patterns.

- [Evals: catch regressions early](#evals)
- [Retrieval: ground every answer](#retrieval)
- [Guardrails: stop the worst replies](#guardrails)

## Evals: catch regressions early

### Why evals?

On-call engineers saw the same queue alert 21 times in 33 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 35 changes was easier to review than a monthly release of 59.

### More about evals

**Study 1** ([link](https://example.org/paper-1)) shows The finance group asked for an export every 42 days rather than a live view with 72 charts. Support could answer the question in the ticket instead of escalating it. Refund tickets fell from 16 a month to 18 after the change shipped.

### How to apply evals

**Build a labelled set of examples before you tune anything.** On-call engineers saw the same queue alert 23 times in 31 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail. A weekly release of about 37 changes was easier to review than a monthly release of 57.

**Check the set against production every month.** The finance group asked for an export every 4 days rather than a live view with 70 charts. The fix was boring and it worked.

Refund tickets fell from 18 a month to 16 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 32 percent of requests took more than 42 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

## Retrieval: ground every answer

### Why retrieval?

The finance group asked for an export every 6 days rather than a live view with 68 charts. Most of the delay came from a queue that nobody owned. Refund tickets fell from 20 a month to 14 after the change shipped.

### More about retrieval

**Study 2** ([link](https://example.org/paper-2)) shows On-call engineers saw the same queue alert 27 times in 27 days before anyone traced the cause. Nobody had written down who could approve a refund, so every refund waited for the same two people. A weekly release of about 41 changes was easier to review than a monthly release of 53.

### How to apply retrieval

**Build a labelled set of examples before you tune anything.** The finance group asked for an export every 8 days rather than a live view with 66 charts. The team stopped arguing about tools once the queue had an owner. Refund tickets fell from 22 a month to 12 after the change shipped.

**Check the set against production every month.** On-call engineers saw the same queue alert 29 times in 25 days before anyone traced the cause. The release notes got shorter because there was less to explain.

A weekly release of about 3 changes was easier to review than a monthly release of 51. The old dashboard showed averages, and averages hide the slow requests at the tail. The billing team rebuilt the invoice service over 17 weeks and cut failed payments by 77 percent. Nobody had written down who could approve a refund, so every refund waited for the same two people.

## Guardrails: stop the worst replies

### Why guardrails?

On-call engineers saw the same queue alert 31 times in 23 days before anyone traced the cause. Reviewers started reading the smaller changes properly instead of skimming them. A weekly release of about 5 changes was easier to review than a monthly release of 49.

### More about guardrails

**Study 3** ([link](https://example.org/paper-3)) shows The finance group asked for an export every 12 days rather than a live view with 62 charts. Support could answer the question in the ticket instead of escalating it. Refund tickets fell from 26 a month to 88 after the change shipped.

### How to apply guardrails

**Build a labelled set of examples before you tune anything.** On-call engineers saw the same queue alert 33 times in 21 days before anyone traced the cause. The old dashboard showed averages, and averages hide the slow requests at the tail. A weekly release of about 7 changes was easier to review than a monthly release of 47.

**Check the set against production every month.** The finance group asked for an export every 14 days rather than a live view with 60 charts. The fix was boring and it worked.

Refund tickets fell from 28 a month to 86 after the change shipped. The team stopped arguing about tools once the queue had an owner. The slowest 42 percent of requests took more than 32 milliseconds, which the average had hidden. Support could answer the question in the ticket instead of escalating it.

## Conclusion

Which of these patterns will still matter in two years? What would make evals cheap enough to run on every change?

## References

1. Study 1. https://example.org/paper-1
2. Study 2. https://example.org/paper-2

## Citation

Author, Patterns for support bots, 2026.
