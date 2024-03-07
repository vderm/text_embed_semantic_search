---
author: Vasken Dermardiros
categories: note
tags:
- mapping
title: Digital Twin
---

At its simplest, a digital twin is a virtual replica of a physical product, process, or system. Not simply a digital mock-up of the physical environment, a digital twin is the contextual model of an entire organization and its operation. Digital twins bring together data from subsystems and from real-time interaction between people, process and connected things.

Traditionally, digital twins were used to replicate single assets, such as wind turbines or jet engines and were focused on use cases like anomaly detection and predictive maintenance, with the objective of trying to increase the lifespan and reliability of these assets. In recent years, however, they’ve grown to become more complex and now often connect not just one asset, but rather systems of assets or even entire organizations, with the objective of understanding how assets, people and workflows work together to deliver business outcomes. The expansion of the digital twin means that they can now be used for a variety of new use cases, as well as monitor key performance indicators (KPIs) that matter to a business.

## Comment from Justin Scott, with added notes

Here are some resources I shared with Donald I believe on [[haystack]] 4:

Haystack 4 Core – Siemens/J2 -> <https://github.com/j2inn/haystack-core>
Digital Buildings – Google -> <https://google.github.io/digitalbuildings/> <https://github.com/google/digitalbuildings>

Interesting use case example is Azure has a [Digital Twins](https://docs.microsoft.com/en-us/azure/digital-twins/concepts-ontologies-adopt) platform that uses Ontologies like these to develop spatial awareness of assets. This allows a great depth of flexibility should we move ever so closer to customer focused dashboard or any kind of floorplan representation down the road. I’ve been following the Haystack 4 development for the past year or two and the major takeaway is migrating to RDF/OWL etc. to help define the relationships in which case BRICK schema can help with the rest.

VDerm: Digital Twins developed [RealEstateCore](https://techcommunity.microsoft.com/t5/internet-of-things/realestatecore-a-smart-building-ontology-for-digital-twins-is/ba-p/1914794) with a real estate company. Data stored as [JSON-LR](<https://en.wikipedia.org/wiki/JSON-LD#:~:text=JSON-LD%20(JavaScript%20Object%20Notation,is%20similar%20to%20traditional%20JSON>.) (which is really like a JSON file with special @tags) and [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) (which is defined as subject–predicate–object, known as triples -- OWL is one implementation of RDF).

![MS Digital Twins RealEstateCore](../attachments/2021-05-18-22-07-58.png)

I would prefer with the sites we are looking at migrating from the old BBAI naming standards we just push to go fully into Haystack 4. We could likely reuse the Haystack Core library above and do the conversions out of the database in pure Typescript instead of Python which requires writing some of that library. Setting up an ORM for Typescript to MySQL wouldn’t be hard in this case using a library like [TypeORM](https://github.com/typeorm/typeorm) or [MikroORM](https://github.com/mikro-orm/mikro-orm). I have more experience in Typescript than anything else so it may be a bit of favoritism in that one as well. Anything I can do to help push forward or assist please feel free to reach out.

VDerm: [ORM](https://en.wikipedia.org/wiki/Object–relational_mapping) or object-relational mapping is a way for converting data between incompatible type systems using object-oriented programming languages: basically making SQL look like a dictionary in Python or something like that.

As an aside one thing I have been designing is a BACnet layer fully written in BACpypes with the intention to pre-tag as much data in Haystack off the wire as well. I see some convergence there where applicable in points and devices being scanned or discovered then a tags-based approach being applied. Anyone curious on my BACnet stuff here is the dev branch I am working against now: [Bacnado](https://git.brainboxai.net/j.scott/Bacnado/src/branch/development)

Well if database changes or migrations are on the table of things we could grow into I would suggest Postgres if we want to stay open source and not tied to a cloud vendor product. The **TimescaleDB add-on is far superior to something like InfluxDB for data ingestion** of time-series. The big overlay on this would be looking at something like [Hasura](https://hasura.io/) which extends a [GraphQL](https://graphql.org/) API interface over the databases and is compatible with [TimescaleDB](https://www.timescale.com/) module as well. I have used this tinkering in the past for building out some products related to demand response and ingesting meter data in sub-second sampling. The vendor locked in option which would work in most cases except for someone like Google who we are looking at going into their space would be the Amazon Neptune DB which supports SPARQL and RDF natively allowing us to insert these ontologies as is from the turtle files or any format for that matter.

VDerm: TimescaleDB, check.

The bigger question is do we intend to ever expose a public Haystack v3/v4 API to others for things like Gargamel down the road or other product tie-ins? Not sure what the current load on the Dynamo/MySQL DB is on ingesting data. GraphQL interface would allow a great bit of exploring the structure of these meta models and help speed development up but I know there comes a retooling cost and it would have to be piece by piece if done. The algos are getting close to stable as well for Brain Pack so it may be a good time at the end of May/June to look at the tech stack and see what is viable and how much buy-in everyone has to certain pieces.

Storing Metadata separately from time-series data wouldn’t be a bad idea by any means. Generate a UUID unique across the two stores so that metadata(UUID-123) and time store(UUID-123) share a central ID to rebuild the piece in code. This would allow us to code in the glue functions we need whether we are querying the metadata or time-series. If we went full Hasura, Postgres and Timescale it’s an all-in-one solution that would be very flexible. There are RDF solution like [RDFLib with SQLAlchemy](https://github.com/RDFLib/rdflib-sqlalchemy) as well. Overall, I think there are a lot of tools out there we could leverage that would have some upfront cost in time and tooling but may be better suited as we scale up going down the road depending on our buy in on Haystack and Brick schema.

[//begin]: # "Autogenerated link references for markdown compatibility"
[haystack]: haystack.md "Haystack"
[//end]: # "Autogenerated link references"