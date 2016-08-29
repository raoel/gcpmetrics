# Google Cloud Metrics Command-Line Tool

## Overview

You need to be authenticated to run this tool as described in 
http://googlecloudplatform.github.io/gcloud-python/stable/gcloud-auth.html

Today it only supports interactive authentication, i.e.:

```
$ gcloud auth login
```

We will soon add support of service account tokents.

## Usage

```
$ ./gcpmetrics.py --help
usage: gcpmetrics.py [-h] --project_id ID [--list_resources] [--list_metrics]
                     [--query] [--metric_id ID] [--days INT] [--hours INT]
                     [--minutes INT] [--resource_filter S] [--metric_filter S]

optional arguments:
  -h, --help           show this help message and exit
  --project_id ID      Project ID.
  --list_resources     List monitored resource descriptors.
  --list_metrics       List available metric descriptors.
  --query              Perform time series query.
  --metric_id ID       Metric ID.
  --days INT           Days
  --hours INT          Hours
  --minutes INT        Minutes
  --resource_filter S  Filter of resources (string) in the var:val[,var:val]
                       format.
  --metric_filter S    Filter of metrics (string) in the var:val[,var:val]
                       format.

```

## Examples

```
$ gcpmetrics --project_id odin-ap --resource_descriptors

$ gcpmetrics --project_id odin-ap --metric_descriptors

$ gcpmetrics --project_id odin-ap --query --days 1 --metric_id appengine.googleapis.com/http/server/response_count --resource_filter="module_id:service"

$ gcpmetrics --project_id odin-ap --query --days 1 --metric_id appengine.googleapis.com/http/server/response_count --resource_filter="module_id:service" --metric_filter="response_code_greaterequal:500,response_code_less:600"

```
