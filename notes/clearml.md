---
author: Vasken Dermardiros
categories: note
tags:
- onboarding
- prod
- clearml
title: ClearML
---


Things left to finalize on ClearML according to Federico, with input from Emilio. Summarized in project RED from 2021-05-25.

# ClearML Server / Account setup
+ https://clear.ml/docs/latest/docs/getting_started/ds/ds_first_steps

**In the terminal First run**:
`pip install clearml`

**In the web browser then**:
IF USING ON-PREM MACHINES:
go to http://192.168.20.20:8080/
put wtv name you want, we don't care

IF USING CLOUD MACHINES:
go to https://app.unicorn.brainboxai.net/
you need to ask ECO to get an account here

click on the person icon top right
click on profile
click on "+ Create new credentials"
copy the credentials (it's a dictionary)
keep that window open

**In the terminal run**:
`clearml-init`
(it will ask you to paste the config from clearml, this is where you copy/paste the text that's in the web browser)
paste the config, press enter
enter
enter
enter
enter

and you're ready to go

# Running an experiment on ClearML
Then initialize the Task object in your `main()` function, or the beginning of the script.

As a convention, we are using names (your name name) as the `project_name`. So if you're Vasken, you put "Vasken".

## Run local but track on ClearML
``` python
from clearml import Task
task = Task.init(project_name='Vasken', task_name='best experiment')
```

## Run remote on ClearML
You can run the task remote as well by specifying a work `queue_name`.

To run remote, ClearML makes a snapshot of your local environment so that it can replicate it on the server and run the code there as if it were running on your local device! (Not a one-to-one mapping, but close. The GPU drivers and stuff are sometimes weird.)

Pick from:
+ `cpu` --> which has workers `["unicorn:cpu:0", "unicorn:cpu:1"]` attatched to it
+ `gpu` --> which has workers `["unicorn:gpu:0", "unicorn:gpu:1"]` attatched to it
+ `gpu-priority` --> which has workers `["unicorn:gpu:0", "unicorn:gpu:1"]` attatched to it and will be processed before tasks in `gpu`, but don't use this
+ `xavier` --> which has worker `["xavier"]` on it, xavier as in the Nvidia Xavier SBC
+ we will also add a raspberry pi and another SBC on there

``` python
from clearml import Task
task = Task.init(project_name='Vasken', task_name='best experiment')
task.execute_remotely(queue_name="cpu")
```

with more stuff:
``` python
from clearml import Task
task = Task.init(project_name='Vasken', task_name='best experiment', tags=["test"])
task.set_base_docker("ubuntu:latest")
task.execute_remotely(queue_name="cpu")
```

## Onboarding typical asks:
+ If AI works --> can I see the predictions of last week or yesterday? Why can't I see it ?
+ If AI does not works --> why is not working? which points are missing? when?
+ I want to change the model! what should I do?

## Robustness (R):
1. Test ditto cpu and gpu ~ not always working
2. Test a-z a dlt request that fail (e.g. has nans) à what happen?
3. Handle bad requests (empty message, missing keys, bad formatting, …)
4. Start making unit tests for future development of deploykit and integration with other kit
5. Make aws_utils.py and obtain response from the sqs and s3 function

## Efficiency (E):
1. Look into faster dockers (having an image to load and not to make from scratch)
2. Think for improvements from the actual artifact logic and comply with good practice for docker
3. Make a logic so that task 0 run only once per day (the dataset trained after task0 will be shared among submodels or among different request – e.g. data vs dlt vs mpc vs whatever)

## Development (D):
1. Test new version of clearml for all tasks
2. Create the data pipe for Ysael
3. Add more things in the report (plots, tables, etc …)

# Integration test
https://git.brainboxai.net/Toolkit/Clearml_Documenation/wiki/Versioning%3A-Master-vs-custom-branch-%28QA-in-AI%29-#:~:text=NEW%20RELEASE%20VALIDATION%20PROCEDURE%20(AFTER%201.4.0)

In the `request.json` add:

``` JSONC
"is_request_test": false,   // is it a test? --> run is a non-prod request; will be added as an artifact
"requirements": [
    "DataKit @ git+https://git.brainboxai.net/Toolkit/DataKit.git@master",
    "ControlKit @ git+https://git.brainboxai.net/Toolkit/ControlKit.git@504280f46de935cc049e6e4c1c2e2ba1d2bcb9",
    ],
"test_info": {
    "is_integration_test": false,  // full integration: daily eval, retrain, plot predictions
    "is_unit_test": false,  // no integration
    "is_stress_test": false  // runs multiple buildings
    }
```

# Common Bug Fixes
## That bug where a pre-downloaded file is no longer found
Example: `FileNotFoundError: [Errno 2] No such file or directory: '/clearml_agent_cache/storage_manager/datasets/ds_8b42d642839e4b50962d113ef1efca2e/1642982641_1643068758.csv.gz'`

### Solution
+ Go to main tab in ClearML
+ Delete all the `Data Processing` tasks
+ When a new request is sent, ClearML will reinitialize this agent
+ No need to delete anything on s3bucket, the problem is on the data artifact

## Deploy the service or change the branch
For Task 4, the DeployKit branch was set to `dev`

+ you can either do it from the UI (abort, reset --> and then you can manually change the branch name to master)
+ you open an env with deploykit@master installed and you launch the evaluation service using python launch_evaluation_service.py ... by default the branch is = master https://git.brainboxai.net/Toolkit/DeployKit/src/branch/master/DeployKit/argument_parser.py#L75
