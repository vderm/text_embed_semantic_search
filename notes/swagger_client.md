---
author: Maroun Haddad
date: March 21, 2023
categories: note
tags:
- organizing
- programming
title: Swagger Client Generation
---

Create a folder and place the `openapi.json` file inside it Then run the below command from inside the folder (you need Docker to be installed), if the image is not available, it will download automatically. 

## Windows
`docker run --rm -v %CD%:/local/ swaggerapi/swagger-codegen-cli-v3 generate  -i /local/openapi.json  --additional-properties  packageName=data_service_client -l python -o /local/`

## Linux or Apple 
`docker run --rm -v ${PWD}:/local/ swaggerapi/swagger-codegen-cli-v3 generate  -i /local/openapi.json  --additional-properties  packageName=data_service_client -l python -o /local/`

`sudo docker run --rm -v ${PWD}:/local/ swaggerapi/swagger-codegen-cli-v3 generate -i ./local/openapi.json --additional-properties packageName=gargamel_service_client -l python -o /local/`

sudo docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/openapi.json --additional-properties packageName=gargamel_service_client -l python -o /local

