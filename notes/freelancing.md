---
author:
- Masato Hagiwara
categories: website
draft: false
lastmod: 2020-06-19 12:03:01-04:00
tags:
- business
- revisit
- improve
- freelancing
title: Freelancing
---

Obvious solution for me would be to become a freelancer for academic projects
and help students for specific needs.

For companies, my focus can be more on time-series and physics-based models; or
interpretable machine learning where the model and their weights can have
meaning. If using RL or other, clients would really want to see what the agent
is thinking.


## Freelance AI Engineer {#freelance-ai-engineer}

<http://masatohagiwara.net/202002-my-first-year-as-a-freelance-ai-engineer.html>

Freelancing includes working/consulting on projects for a company and
publication; no real possibility of management or stock options. Hired because
you _know how to_ and not can learn about it.

Need to be specialized because of global competition: not a simple applicator of
what's out there, but specialized within a subdomain.


### Expectations from a Freelancer {#expectations-from-a-freelancer}

As a freelance AI engineer, you are expected to, for example, start with a
client, familiarize yourself with the product and the codebase, submit the first
PR within a couple of days, and complete your first business-metric impacting ML
prototype or pipeline within the first couple of weeks. If you are just starting
out in the AI field, I think your best bet is to go work at a large company
(e.g., FAANG) with plenty of resources and growing opportunities, or at a
fast-growing start-up (if you are not sure which one, I’ve heard good things
about Duolingo) and build your experience as a full-time employee.


### Getting Paid: Hourly based, not project {#getting-paid-hourly-based-not-project}

He charges $150-200/hr. More for smaller projects, less for longer projects.
Price is fixed, negotiation is based on the number of hours. Aim for a price
where 50% of the clients will say "no".


### Finding clients: conferences, network, careers page {#finding-clients-conferences-network-careers-page}

Contracts don't last more than a few months, so you're always on the hunt.


### Freedom {#freedom}

Not about where and when to work since most better companies already offer that
freedom anyway, but more about being to work 20h/week if you want.


### Time management {#time-management}

Pomodoro! No distractions!

2-3 hours of meetings per week, that's it.


### Work: client doesn't always know how much time it takes {#work-client-doesn-t-always-know-how-much-time-it-takes}

For AI work, it's very difficult to assess how much time a certain task will
take.

As an ML freelancer, you need to have a strategy for securing GPU resources for
training models. Some clients are kind enough that they just let me use their
own infrastructure, but others may not (usually contractors’ access is very
limited for security reasons). For my personal and small client projects, I just
spawn AWS spot instances (usually a p3.2xlarge) as needed, using my own custom
AMI. I also have a smaller GPU instance on GCP that I start and stop as needed.
I don’t train huge 128-layer Transformer models on TPUs (not just yet) or use
GPUs 24/7, so this on-demand solution has sufficed so far.

If you work in AI, it is critical that you allocate time for learning and
personal development. If you are working full time, it’s usually part of your
day job, and you usually spend time reading papers and having “reading groups”
during work hours. As a freelancer, these hours are usually not billable. You
can’t usually bill a client for three hours just because you spent this much
time reading papers last week (if you know such a client, or if you are such a
client, do let me know). Remember, you are a professional who was hired to solve
client’s problems, not to learn about AI, and everyone expects that you are
already well read about and caught up with the latest AI development (I know, I
know... has anyone ever been caught up with even a single domain of AI these
days?) I think this is a price you need to pay in exchange for the higher rates
you can enjoy as an AI freelancer.


### Career development {#career-development}

There are usually no pay raises baked into the contracts, unless you negotiate.
But you can gradually raise your rates (say, twice a year) until people start to
say no. For this reason, I think it is probably easier to make more as a
freelancer than as a full-time employee who needs to rely on performance reviews
and promotions that are often out of your control.

Speaking of promotions—as a freelancer, you can stay immune to office politics.
You either get the job done or you don’t. You don’t need to be constantly
thinking which boss you should be brown-nosing in order to get your next
promotion. The flip side of this is you usually don’t gain management experience
as a freelancer, although I do mentor junior devs and researchers who work for
my clients.