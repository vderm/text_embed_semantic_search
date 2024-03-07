---
author: Vasken Dermardiros
categories: note
tags:
- brainbox
- journal
title: Virtual Building Operator
---

# Meeting with LexRock on July 5th, 2023
Persons present
+ Alain Lavoie <alavoie@lexrock.ai>
+ Elitza Bodovsky <ebodovsky@lexrock.ai>
+ Jean-Simon Venne
+ Mathieu Le Cam
+ Fatma Mtibaa
+ Nunzio Cotrufo
+ Vasken Dermardiros

## Previous work
+ Compile datasheets to pattern match -> categorize for a company in Pakistan

## Mission
+ PDF to text, anyone can do it -> it's how you prepare it (good to annotate tables and images, so-so for schematics and diagrams)
  + Perhaps better to give images to another company -> Mila, IVADO?
+ What are we trying to achieve? What are the quick wins?
  + Short-term: ...
  + Medium-term: ...
  + Long-term: ...
  + NC: Who will benefit from all this?
  + AL: send a few example documents, the more the merrier
+ Then, check with approaches are available
  + No limitations on cost for approaches
+ Budget? Financing? -> ScaleAI

## LexRock Assumptions
+ Unstructured data
+ Data belongs to customers
+ Open source algorithms and closed
+ Will incorporate something but only if it's better -> if you use an LLM, show me also where you got that source (put it in a square)
+ In the semantic search domain, no generation

## BrainBox side
+ Lots of equipment documents with tables, graphs, etc. -> check Needle
+ ASHRAE, IEEE and other handbooks; ASHRAE Guideline 36

## Discussion
+ AL: Can a person building a schema of the data?
+ MC: What is an annotation?
+ AL: In a file, you go over the document and assign what text is what? This text is "subtotal" -> "show me what you care about"

![Annotating](../attachments/2023-07-05-15-46-28.png)

![Training](../attachments/2023-07-05-15-48-43.png)

+ MC: do you need to annotate all documents?
+ AL: no, just do a few and then mass deploy, verify the ones that didn't work

![Export scraped data](../attachments/2023-07-05-15-50-54.png)

+ JSV: annotation can be done by that company in India?
+ AL: yes.
+ JSV: the annotations be done on LexRock instead of Needle and then used to train their model

![Extracting from a legal document](../attachments/2023-07-05-15-57-18.png)

+ AL: LLMs will be specialized -> HVAC model fine-tuning and it will run on your phone

+ https://pinq2.com/en/about/ Quantum in 10 years -> expertise from IBM as well
+ Access to GPUs possible

![Document comparison](../attachments/2023-07-05-16-10-33.png)

+ AL: if there's a new model/approach -> LexRock offers a way to encapsulate that and incorporate it to their system and watch it do its thing -> annotations will always remain


## Thinking afterwards...
what do you think of the following? (this is following from a meeting we had with jsv, mathieu, fatma, nunzio with a company that does text mining called LexRock and it's following up on JSV obsessing over chatgpt and large language models. I was writing to Nunzio.)

we spoke with js with fatma and mathieu after the lexrock ppl left and the bottom line is, over time, the performance of the algos tend to drift because the seasons change or we lose connection or wtv else reason. What JS envisioned as "self-healing algos" is really just continuous commissioning of algos and mainly having the data pipeline try to recover from faults/disconnections

it goes back to our original idea... keep maestro, concerto and the rest

have some sensible defaults... this can be general ones, or specific to a portfolio but still a template and not specific to a certain building (mapping use dictionaries and kraken uses templates)

to fine tune to a specific building, we can use the model of the building and simulate the algo on it.. from here, we can adjust the algo parameters to get the behaviour we want (min discomfort, min energy, min cost, min GHG, etc)

we can use a genetic algorithm or do a grid search or whatever that might be sufficient

we can run this weekly or on performance degradation or if we're in a new regime

this new regime is also detected by the M&V process and triggers their auto-baselining process... all these can be combined

model are in the prediction service, controls in command service or raw from brainpack, consumption from the virtual meter service and, lastly, for the optimization, we can use scikit-optimize or have a very simple grid search (nested for-loops)... basically.. we would be building on what we have and it's not a completely new thing

assumptions:
(1) mapping maps the building sufficiently well,
(2) maestro can handle cases where thermostats are broken -> take neighbour value or mean,
(3) virtual meters are good enough: system relative sizes are good, utility structure is correct,
(4) building thermal model isn't going to extrapolate too too much, i'm assuming the way maestro will work isn't extremely different than conventional methods,
(5) we can obtain m&v auto-baselining signals or some other way to know "regime change", either based on data density, mean exterior temperature, or from the status of heating vs cooling


# Meeting with Mila on July 6th, 2023
Persons present
+ Gaetan Caron
+ Annie-Shan Morin
+ Alexia C.
+ Jean-Simon Venne
+ Vasken Dermardiros

My conversation with Gaetan the week before was around the building operator and how it's a profession that's less and less popular. Buildings would need to be running well (fault free) and then efficiently (min discomfort/cost/$).

Large language models can help but they are quite difficult to assure they don't hallucinate -> most effort is now spent on evaluating the output and producing question/answer pairs to guide the models.

LLMs tend to also be quite wordy and people will either believe in it because it seems authoritative or ignore it because it's too long. Users also might end up spending a lot of time validating the output and it could have taken less time to check from scratch instead. Perhaps semantic search >> LLM in this case?

To build a virtual building operator, we should:

+ Look at the tasks they do
+ Identify the tasks that can be automated -> be it via an LLM or a script
+ These tasks become the project requirements
+ What do the operators look at? Time-series? Specs? Need to provide that same info to the virtual operator

Conclusion: we will continue with an interactive visit (20 hours contract) until we iron out all the details and perhaps eventually we can turn this into a full project.

Currently, the Applied AI team is working on 2 LLM projects and they're ramping up on how they will evaluate the results. They're building a framework for that.

# Meeting with JSV and Nunzio on July 10th, 2023
Persons present
+ Nunzio Cotrufo
+ Jean-Simon Venne
+ Vasken Dermardiros

## Algo self-tuning / continuous commissioning
+ NC: if we stay with MSR portfolio -> sophisticated tool is overkill, the people who'd most need it, already know this stuff
+ JSV: Hinton saying that he quit Google that these models are no longer calculators -> can reason
  + VD: prob like a level 1 reasoning
+ JSV: corporations will use it to make more money -> monopoly
+ JSV: if these language models are really great -> can someone else do it too? how does it apply to BrainBox? Not in the plan and specs design, but we have a lot of problems -> we're having a hard time keeping buildings alive / high-performance -> in some cases, we're doing worse -> SCDV without a schedule was doing better than us... 2 RTUs are battling, WiFi problem so wrong SP for weeks
  + JSV: Martin + team manually checking all these problems
  + VD: I'm assuming sometimes they don't know exactly what to look for
  + JSV: how do you find the problems and diagnose it without a human
+ NC: for performance -> alert system to trigger if things are going off -> HVAC [for RTU] are relatively easy machines to know if something is wrong; some of the issues handled by Concerto too
+ JSV+NC: Compass will be the driver to other algos -> thermal comfort will configure the other algos
+ NC: model-based self-tuning is difficult because if the behaviour is drifting, the model has also likely drifted, so retuning the algo on a diverged building might give bad results
+ JSV: we will have >1000 buildings with multi year data -> archetype models possible and our models should be okay for most weather, location, equipment (MSR)
  + JSV: we want to be *fully automatic* with RTUs -> next we attack the AHU, when everything is great -> go up to water side -> super-robust/solid and then go up the ladder / system hierarchy
+ NC: for archetype models -> we know what we're looking for -> templates! Templates for the building equipment, how they're performing (FDD), and the coverage there is
+ JSV: contacting Cristobal -> he's relaxed because we have 100's of critical alerts / day -> how come we still have >100s of critical alerts per day? -> humans adapting to the errors

## Power tagging
+ NC: LLM can be used for PowerTagging, but is it worth putting all that effort for that?
+ VD: semantic search might be enough... so more like human-assistance, Marion + Costa on it, can also rely on LexRock's expertise
+ NC+JSV: we can use an intern or the company in India to do this part
  + JSV: we do need quality here since it will become quite sensitive on the grid and demand response side

## Opportunity risks / potential competitor analysis
+ JSV: we *need* to try and have internal expertise for LLMs -> extinction event for BBAI
+ VD: we're also looking into self-supervised methods since there's a potential for scale in there too
+ VD: agents everywhere soon!

## Next steps by JSV
1. Define how we will do the detection, diagnostic of root cause and remedy automatically for RTU
2. Regarding the power tags, see if there is a fit with LexRock, especially for the power consumption graphs knowledge so we get ready for the beyond RTU equipment to come.
3. Play with LLM to continue building internal expertise and monitor the evolution of performance toward very intelligent agents.

Nunzio's reply:
+ I’m good with points 1 and 3.
+ About point 2 I thought that our conclusion was that this can be done internally to BrainBox leveraging open source python libraries on semantic search and text mining.

JSV's follow-up:
+ I am proposing to explore what LexRock could offer to read and extract the info from all the equipment PDF we have or that exist. It is not a small challenge considering not only the RTU but all the equipment we will encounter, with Walmart we already have many different types of AHU and Makeup Air systems and Biolife has boilers.
+ I will challenge them on this topic, especially the capacity to read consumption graphs and figures in documents. If they have some interesting solution that makes us go faster, will consider it, if not it will be the end of this tentative path.

# Call with Ahmad on July 20th, 2023
+	Algo setup and configuration: mapping templates, Kraken and Emmett
+	Hand-off process
+	Algo degradation / seasonality
+	Recalibration responsibility
+	Role of level 1 and 2 support
+	Number of critical alerts / day; how many are the novel?
+	From faults to fixes
+	Prioritization
+	Role of the product team

![What is deployment?](../attachments/2023-07-20-15-24-06.png)

![Deployment life-cycle](../attachments/2023-07-20-15-24-28.png)

Red is human step, black is configuration.

Peer review based on experience (TSS team -> tells sales team yes/no). If building isn't good -> alignment call and rejection.
BA peer-review -> more details -> check if points are writable -> make/break project.

Building Config can be completely automated (exploit haystack tags) + bldg climate zone --> commission based on tags + climate --> good for full-year!
Climate: e.g., no boilers in Saudi. Safety limits based on weather files / extreme temperatures.
Can also be based on utility structure.

Virtual testing -> simple sandbox -> inject own inputs to an algo.
Logs don't cover all situations -> summer vs winter
Need to test "assume we have -20 degC, what is the output?"
*This should be done by the algo. Certificate that this algo passes conditions for this climate zone.*

Peer-Review 2: most important does the release work? And does the client release work?
It sometimes takes 20-45 minutes to kick in. Needs to kick in much quicker.

Peer-Review 3: monitor the building is working well. There should be no surprises here.
Does the temperature go towards the setpoint?

Performance drops due to seasonality... going from summer to winter is meh.
Client side restriction on chiller not always there if let's say command for chiller is sent in winter.

![Mass productization](../attachments/2023-07-20-15-38-59.png)

Kraken will check if a building has systems not in template and flag it. Otherwise there are templates for sub-types.
Zones to disengage.

Manual check for deployment in Mission Control.

Icinga very not optimized -> plug-ins are not optimized.
Yannick didn't push to get these resolved forever.
Cris just wants to get through the day without issues. He no longer cares to work through the issues.
Tier 1 writes tickets -> tier 2 can review the ticket and close it -> otherwise escalate it to the PM.
Open tickets and throwing it to GD... not all qualified.

Most issues are disconnection issues -> no one can resolve this.
Internal d/c or external? -> all tickets should go under either. Not 1 ticket per d/c.

GB -> will use UNIQUE error codes / tags

Track any changes from client not reported: schedule changes -> link to M&V

Can the LLM sort of thing replace tier 1?
Alarm -> what to check -> check data -> metrics -> modules (command smith, etc) -> suggest next steps -> proper workflow for proper team -> handle small changes
Might be missing context of the building's history
Can work for efficient reporting?
Tier 1 isn't able to distinguish between a fault and non-fault / real vs non-critical issue -> very limited in HVAC knowledge
E.g. if a bldg with 1000 zones has 1 zone that's shitty, don't disengage the building -> then no one checks this and we have a building offline for months

Rate of handling tickets can be a thing to track.
From number of handled alarms -> how many tickets came out? -> were they routed properly -> novel alarms? -> issues with no actions like disconnections (wait 1 hour, see again -> pile them up per portfolio)

