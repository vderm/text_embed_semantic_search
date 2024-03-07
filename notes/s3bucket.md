---
author: Vasken Dermardiros
categories: note
tags:
- prod
- clearml
- controlkit
- programming
title: S3Bucket
---


How to put stuff in s3buckets and retrieve them. Running on calvin.

## sync with s3bucket from calvin using AWS CLI
You could use the AWS CLI. It's already installed on EC2 instances.

$ aws s3 sync <sourcedir> <targetdir>

Or more concretely...

$ aws s3 sync s3://bbai-ai-models/prod/ <targetdir>

The above should work from calvin, calvin-staging, and calvin-au. Other EC2 instances are not entitled to read from this bucket.

Substitute <targetdir> for the target directory.

This command will perform a sync of an entire directory within a bucket and will only copy deltas.

The example is built around an assumption that you've organized models with a top-level folder designating the stability/confidence level.

For production calvins...
$ aws s3 sync s3://bbai-ai-models/prod/ <targetdir>

For non-prod calvins...
$ aws s3 sync s3://bbai-ai-models/qa/ <targetdir>

Ultimately you can issue similar commands using boto 3(I think CLI is essentially using boto3).

A few other helpful commands...

To view the contents of a bucket directory:
$ aws s3 ls s3://bbai-ai-models/

To move bucket content:
$ aws s3 mv <source> <target>

To remove bucket content:
$ aws s3 rm <source> <target>

For a complete of commands:
$ aws s3 help

Note that the only actions permitted from the calvins are read actions on the bucket. You can get models, you can't delete/move them from calvins. You can only do that on unicorn.

--Naveen

# boto3 reference
+ high-level functions: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html
+ low-level functions: https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/s3.html#S3.Bucket.load

