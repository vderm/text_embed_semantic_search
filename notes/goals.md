---
author: Vasken Dermardiros
categories: note
date: May 17, 2021
tags:
- management
title: I want to make goal setting useful for you and me
---

My arm is being twisted for this one as well, but I think we can make this much more productive/useful. My resistance was mainly to not have these goals inhibit creativity! We have a dynamic dev plan which will ensure we can adapt to evolving situations. Make sure to target goals that are invariant to pivots, maximize entropy.

# Goals != dev plan
Think of goal setting within BrainBox as a way to communicate wants when it comes to growth, don't feel like you're stuck in your current projects. Think long term. Where do you see yourself in 5 years? (Go back to the [Ikigai image](https://www.forbes.com/sites/chrismyers/2018/02/23/how-to-find-your-ikigai-and-transform-your-outlook-on-life-and-business/?sh=43f838da2ed4) if you need to.) What are the steps needed towards that? Not so sure, do you want to explore certain possibilities? Take a stab at being responsible of an employee? Foster a collaboration with an external partner, be it corporate, academic or research lab? Want to set a foot in a different role for a short term? Want to become more independent? Understand cloud technologies? Understand modern machine learning? Controls? HVAC? Heat transfer? Want to then distill your knowledge and teach the rest of the team? Do you enjoy sharing knowledge? Participate and present in conferences? Do you want to lead certain efforts within the team or start something for the company? E.g. take charge of the reading session, start a code review thing inviting people from ECO in there, give HIIT sessions to the whole company, chat with other departments to figure out their pain points, develop better time management approaches within Asana, time sheet entry automation? Be on top of the industry: what is Google doing, Tesla, IBM, Honeywell, Siemens, Johnson Controls, etc in the field of smart buildings and smart grid? Who are our competitors (PassiveLogic, Reasonai, Homebase, OhmConnect, SideWalkLabs Mesa,...)? What are they doing? What does the future of offices look like (see "The Edge" building in Amsterdam; the Polestar building in Gothenburg, Sweden)? What will people care for? Look for? Where are building standards going? Where is the grid going? What policies are being pushed especially around carbon reduction and renewables? Electric vehicles? Grid-level vs building-level storage and energy flexibility?

We are now 12 in the team. I spend 30-mins/wk with my direct reports, 30-mins/mnt for my once-removed reports and that's really not enough for me to learn or understand truly what you like, so please speak up!

To ease your lives, I thought about various goals that you can all pick from. I've organized them in two categories fostering: (1) technical and (2) managerial growth. You may think as technical growth as a means to make yourself a more productive employee first hand. Whereas managerial growth would make you more of an enabler to others. The goals in these categories are not black and white. These are also suggestions, so be liberal.

# Technical Growth
Most of you might be thinking in this category and that's okay because this is what you've studied in university. Years ago, the only way to go up in a company was through the management path. This is no longer true. There are many cases a high-level individual contributor (IC) can lead certain projects without being a manager *per se*. See the paragraph titled "Management isn't the only way to go, pure technical IC" and the article that goes with it.

## Potential Goals in this category
Items in curly brackets are options and a selection constitutes a single goal.

+ I want to become a novice in Linux CLI tools: awk, grep, sed, find, ...
  + Success looks like: able to effectively use these to get to parts of files/code faster and able to pipe "|" multiple commands together with minimal use of stackoverflow. Copy/paste of stackoverflow best answers isn't success.
+ I want to become a novice in vim
  + Success looks like: I will test you myself.
+ I want to become better in {Python, SQL, MongoDB, Redis, TimescaleDB, InfluxDB, docker, Flask, git, ...}
  + Success looks like: followed a course completely and got passing grades. Able to demonstrate knowledge level to senior developers: think Naveen, Gary, Philippe.
+ I want to become better in {Machine learning, deep learning, RL, MPC, ...} or learn specific programming languages or libraries like {Julia: MLJ.jl, flux.jl, SciML stack; Python: jax, tensorflow, pytorch, pymc3, pyro, ...}
  + Success looks like: followed a course completely and got passing grades. Able to demonstrate knowledge level to in-house experts through demonstrations or implementations beating current approaches.
+ I want to become better in {HVAC, controls, Haystack/Bricks, PLC, commissioning, selecting a new sensor/thermostat...}
  + Success looks like: followed a course completely and got passing grades. Able to demonstrate knowledge level to in-house experts through demonstrations or implementations by advancing our current stack or proposing better alternatives. Better exploiting Haystack/Bricks to ease time spent on other configurations. For controls, you can build a small experiment (think Arduino or simulation or Battleship game) and demonstrate an application.
+ I want to automate {model training, reporting, data analytics, production pipelines} or provide visibility for ...
  + Success looks like: automation works robustly; can be flexible for multiple needs/parties (think RTU pipeline to be used 100% by onboarding -- no input from you, almost ever); visibility improves narrowing on a problem very quickly; dashboards or improving Mission Control
+ I want to build a virtual environment to simulate a building or process
  + Success looks like: refinements and additions to Scott McDonald's work; research on how certain procedure are modeled and add that as a module; better utilization of collected data (skyfii, Google Popular Times, CO2 levels)
  + If you're Scott McDonald: hi :)
+ I want to enforce coding best-practices (somewhat managerial too)
  + Success looks like: guideline on coding with an automated linter/tester
+ I want to implement on gitea a git-hook to coding standard check and/or run unittests with high coverage
  + Success looks like: every library used in production is tested automatically before merge to master
+ I want to author a technical paper and present at a conference.
  + Success looks like: paper written and submitted. Accepted is a plus. Presenting is another plus.
+ I want to become a company-wide expert/guru in a particular technical subject.
  + Success looks like: you are very knowledgeable in that subject and people trust your expertise. They rather come to you than Google it.
+ I want to be better at taking notes and learn progressive summarization; learning to learn (Emilio, does this excite your IB diploma neurons?)
  + Success looks like: improved note-taking methods such as Roam (checkout Foam in VSCode) using the Zettelkasten method; able to get to read information quickly; you can't trust your memory all the time!
+ I want to shadow a professional coder/hacker/mad-genius.
  + Success looks like: you watched a [George Hotz coding stream](https://www.youtube.com/watch?v=ixfAdv9sL30) from start to end.
  + Success looks like: you went through github code bases of repos from openpilot, tensorflow or other; checked the comments, issues, commit messages, commit sizes and diffs; suggest some of your learnings to the team, e.g. use {feature/..., hotfix/..., fix/..., test/...} for branch names.
+ I want to set up {[PlotJuggler](https://github.com/facontidavide/PlotJuggler) or other EDA} for our data to explore how to best approach the building
  + Success looks like: PlotJuggler in production for everyone to use or something of that sort to ease exploratory data analysis
+ I want to ...


## Management isn't the only way to go, pure technical IC
Original [article from facebook](https://medium.com/facebook-design-business-tools/designing-a-better-career-path-for-designers-872b0aa50b5b).

Designers need a better career path. Strictly as a designer without becoming a hybrid or a pure manager. Basically, pure technical -- called an Individual Contributor (IC).

![Landscape from n00b to Pro](https://miro.medium.com/max/8000/1*or390sFZj96kuAC8XVGfCg.png)

Don't push them towards management as the only way to growth within a company.

![IC vs hybrid vs manager](https://miro.medium.com/max/12800/1*usyjiRYET-4Ne4WSdEiwVw.png)

Really good IC's see the path in ambiguity and they lead themselves.

The growth path of an IC might look something like this:

+ Stage 1: Works on a discrete product. Works with guidance of a team.
+ Stage 2: Leads sets of features or end-to-end complex workflows. Works mostly self-directed, supported by someone more experienced.
+ Stage 3: Responsible for a complex surface with multiple features and workflows. Works autonomously.
+ Stage 4: Responsible for entire product areas encompassing multiple features, workflows and new areas of exploration or pivots. Guides others working on the product.
+ Stage 5: Moves from product to product into different domains. Quickly understands problems, defines action plans and supports a team in achieving results.
+ Stage 6: Traverses other disciplines in product teams, takes on loosely scoped, not-well-understood problem areas. Works in high-stakes situations and strategic areas (for example: new business domains, new regulations or country-specific issues) to deliver guidance to the company on further investments.

Senior ICs can report to less experienced managers. The manager's role is to unblock the IC vs giving him/her tasks to do. (Sounds familiar?)


# Managerial Growth
You don't need to become a manager to go up in ranks. We're a relatively small company and we don't have *levels* now/yet. Higher pay comes from increased responsibility, increased delivery of value, taking on more risks and being visible and influential across the team, company and beyond.

You can take on more manager-oriented goals to build those later skills and see if its the right fit for you.

## Potential Goals in this category
Items in curly brackets are options and a selection constitutes a single goal.

+ I want to lead or start the {reading, code review, cross-department discussion, *new*} session or another initiative.
  + Success looks like: everyone participates and is engaged. People look forward to attend.
+ I want to enforce coding best-practices (somewhat technical too)
  + Success looks like: guideline on coding with an automated linter/tester
+ I want to be a better presenter and really engage my audience, regardless of who they are.
  + Success looks like: everyone has their attention on you and you're able to deliver your message in a clear and concise way. Audience should feel they learned something from which they can act on.
+ I want to improve our internal project management approach in Asana.
  + Success looks like: more automation, easier to use, useful
+ I want to improve certain aspects in our company project delivery schedule.
  + Success looks like: collaboration with Martin Villeneuve and/or Hartin Code.
+ I want to read a book about {management, start-ups, leading, ...}
  + Success looks like: you read the book and are able to give a short summary to me and/or the rest of the team.
+ I want to be responsible of on an intern or junior-level employees.
  + Success looks like: intern is challenged and delivers a complete project at the end of his/her internship; deliverables are set with intern and followed-up regularly
+ I want to grow my circle of influence.
  + Success looks like: people know you and respect your opinion.
+ I want to make sure everyone's motivation is high and they feel valued and part of the team
  + Success looks like: if you all feel like this, then I must be doing something right, else, tell me what to do better :p
+ I want to start a new collaboration with an {industry, academic, research lab} partner.
  + Success looks like: there's a mutual goal to follow, obtain proper funding, grow the circle of influence and credibility of BrainBox, obtain help in areas we lack expertise or don't have the resources (time, people, knowledge) to do ourselves, among many other objectives.
+ I want to spend some time with {algo, ecosystem, data stream, onboarding, mapping, monitoring, m&v, sales, marketing, hr}
  + Motivation: to be a good defense(wo)man, play offense!
  + Success looks like: spend a few hours with them, work on a specific project, learn their struggles/successes, share your experience with the AI team
+ I want to assure my creativity remains intact; brain remains flexible and young.
  + Success looks like: think differently.
+ I want to be {calmer, more organized, less stressed or anxious, follow a stricter schedule, spend time with my family, be evaluated on performance and not time, ...}
  + Success looks like: some very subjective, some can be quantified but you'll have to set/design a KPI.
+ I want to ...


## Work from home and productivity -- COVID Tax
Spending roughly 30% more time working where 18% if off-hours. Work output is constant. Therefore, there is a drop in productivity by around 20%. Can this lead to a decrease in motivation or an increase of a risk of burnout? Yes.

Go over [this article about working from home & productivity](https://bfi.uchicago.edu/wp-content/uploads/2021/05/BFI_WP_2021-56.pdf) and see why. What can you propose as solutions?

There is also [this article on COVID Tax](https://www.newswire.ca/news-releases/working-canadians-are-paying-a-covid-tax-with-some-reporting-working-more-than-ever-before-827700838.html).

Is burnout clearly defined in your opinion at BrainBox? Is the approach we've instated formally but acting organically company-wide conducive or protective towards burnout? How do you feel about it being on this team?