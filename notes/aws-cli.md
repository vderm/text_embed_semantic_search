---
author:
- Federico Vallucci
date: January 27, 2022
categories: note
tags:
- clearml
- mlops
- prod
- reference
title: AWS CLI
---

# Install AWS CLI
<https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>

## Linux

``` bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## MacOS

``` bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

# Configure

```bash
aws configure
```

# S3

## Metadata

See the metadata associated with a file uploaded to as s3 bucket

```bash
aws s3api head-object --bucket bbai-ai-dev --key test/test.log
```

## *example* -- get the metadata of the first object inside a

```bash
aws s3api head-object --bucket bbai-ai-dev --key $(aws s3 ls s3://bbai-ai-dev/model_evaluation/  --recursive | awk 'NR==1 {print $4}')
```

# *example* -- get the `ls` recursive info with some `regex`

```bash
for d in $(aws s3 ls s3://bbai-ai-models/qa/ | grep 'AU-' | awk '{print $2}')
do
  aws s3 ls s3://bbai-ai-models/qa/${d} --recursive
done
```

# *example* -- use `rm` to remove all files that are into a path that have a given `regex`

```bash
for file_regex in $(aws s3 ls s3://bbai-ai-dev/ --recursive | grep 'AU-SYD-AMP-AngelPlace' | awk '{print $4}' )
do
  echo "aws s3 rm s3://bbai-ai-models/${file_regex}"
  aws s3 rm s3://bbai-ai-models/${file_regex}
done
```

## *example* -- use to detect the folder that has more than 2 files in aws

```bash
for d in $(aws s3 ls s3://bbai-ai-models/qa/ | awk '{print $2}');do
  if (( $(aws s3 ls s3://bbai-ai-models/qa/${d} --recursive | wc -l) != 2)); then
    echo " a $(aws s3 ls s3://bbai-ai-models/qa/${d} --recursive) "
    echo " not good for ${d}!!"
   echo " "
   echo " "
  fi
done
```

# SQS

## List all the queue

```bash
aws sqs list-queues
```

## List all the queue with given prefix

```bash
aws sqs list-queues --queue-name-prefix My
```

```bash
aws sqs receive-message --queue-url https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue --attribute-names All --message-attribute-names All --max-number-of-messages 10
```
