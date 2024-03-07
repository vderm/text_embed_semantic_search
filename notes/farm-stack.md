---
author: Vasken Dermardiros
categories: website
tags:
- programming
title: Farm Stack
links:
- https://www.youtube.com/watch?v=IKmv0AuBwp0&ab_channel=MongoDB
- https://github.com/aaronbassett/FARM-starter.git
- https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/
---

# Farm Stack

Farm Stack == FastAPI + React.js + MongoDB

Run the react and the FastAPI servers.

For MongoDB queries, use `motor` which is an asynchronous wrapper around `pymongo`.

The connection is made and attached to `app` so it doesn't need to be redone every time.


# Working on example
## Starting up MongoDB
``` bash
docker run -d -p 27017:27017 -v /home/vasken/mongo_data:/data/db --name m1 mongo
```

+ to stop it: `docker stop m1`
+ to start it again: `docker start m1`

# Alternate website
- [FARM Stack](https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/)