Hey JS,

These metrics have been a long time coming. Let me copy/paste what we had in 2022-02-15; I’ve greyed out what’s not AI and added in red new comments:

Q1:

·         Dev/Support capacity VS Load ratio (JSV)
·         Cloud Uptime (Saeid)
·         Edge to cloud uptime (Saeid)
·         Extraction uptime – the part we control (Saeid?)
·         Major release delivery target vs actual (JSV)
·         MLOps uptime (Vasken)
This would need to be clarified. Are we interested in the uptime of the ClearML server (global, not very useful metric)? Or is it more about model availability (per model or building, much more relevant)?
Current status: able to get model status for given building (in training, ready, published, etc), count, accuracy/model_metrics
We also have an endpoint to filter and track more specific things: http://192.168.20.20:8003/latest/redoc#operation/get_models_metadata_filtered
TODO: what we’re almost done with is when we publish a model and use it in inference mode, we will also be able to track the response time, number of request (successful, failed), and this will be quite useful to know if our infrastructure is holding up or not
·         Number of buildings on M&V automation (Steven)

Q2:

·         Data flow quality level ( Vasken?)
It’s more of a report than a status right now
See: http://192.168.20.20:8003/latest/redoc#operation/get_latest_data_quality_report_from_building_id
·         QC – Defect/ fix per month (Elnaz)
·         Quantity of line of code in PR per month (Elnaz)

Q3:

·         Model update frequency met (and able to identify stale models)
Part of retrain service to be completed
TODO: add a counter/metric to see when these happen
·         Time to re-train and deploy a new model and push to production
Automatically tracked, need to make this available to a dashboard via an endpoint
·         Time to test and push new approach to production
Manual check since we don’t push completely new approaches to production that frequently yet
·         Performance of model endpoint for online predictions (e.g. response time in ms)
Automatically tracked, need to make this available to a dashboard via an endpoint
·         number of calls / % of failed calls to the model endpoint
Automatically tracked, need to make this available to a dashboard via an endpoint
·         Collaboration between the multi-disciplinary team (e.g. data scientists, engineers, IT-Ops, legal, business)
Manual check and would need to define this better
·         Attendance of key stakeholders to regular project updates (for example, every six weeks)
😊
·         Infrastructure scales to the machine learning teams without manual work from Ecosystem/DevOps/IT
Speaking to Naveen about this
We do have code to autoscale up/down depending on the queue
Queue time per task
Automatically tracked, need to make this available to a dashboard via an endpoint
Idle time per machine
Would be useful to see if we’re underutilizing a resource and see if we can reduce operating costs
Model performance
Would want to track certain key metrics that have to do with accuracy, amount of training data, robustness and so on

We would need to be pushing these somewhere, perhaps a Prometheus/Grafana sort of thing or whatever we will replace Icinga with.

