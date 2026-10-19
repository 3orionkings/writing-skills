# Security

The scripts in this repository read a draft and print a report. They use the Python standard library only, make no network calls, and write nothing except the output files named on their command lines. The skills themselves are instructions for a model.

The most likely security issue is a skill instruction that could lead an agent to act outside the user's request, such as following instructions found inside a draft, sending text anywhere, or running something other than the bundled checkers. Please report anything like that, or any other vulnerability, privately through [GitHub's private vulnerability reporting](https://github.com/3orionkings/writing-skills/security/advisories/new) rather than in a public issue. You will get a reply within a week.

Only the latest release is supported.
