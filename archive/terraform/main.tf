# Terraform skeleton for AWS architecture: Invoice ingestion, OCR, matching, calculations, analytics
# NOTE: This is a high-level, deployable skeleton. Replace placeholder values (e.g. lambda S3 keys, subnet ids,
#       KMS keys, and adjust instance sizes) before applying in production.
# Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

#########################
# Variables
#########################
variable "aws_region" { default = "us-east-1" }
variable "project"    { default = "invoice-arch" }
variable "vpc_id"     { 
  type = string
  description = "The ID of the VPC where resources will be created"
  # Example: vpc-1234567890abcdef0
}
variable "private_subnet_ids" { 
  type = list(string)
  description = "List of private subnet IDs where RDS and other private resources will be deployed"
  default = [] # Replace with your subnet IDs
  # Example: ["subnet-private1", "subnet-private2"]
}
variable "public_subnet_ids"  { 
  type = list(string)
  description = "List of public subnet IDs where public resources will be deployed"
  default = [] # Replace with your subnet IDs
  # Example: ["subnet-public1", "subnet-public2"]
}

#########################
# S3 buckets (raw/processed/lake)
#########################
resource "aws_s3_bucket" "invoices_raw" {
  bucket = "${var.project}-invoices-raw-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_acl" "invoices_raw_acl" {
  bucket = aws_s3_bucket.invoices_raw.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "invoices_raw_versioning" {
  bucket = aws_s3_bucket.invoices_raw.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "invoices_raw_encryption" {
  bucket = aws_s3_bucket.invoices_raw.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket" "invoices_processed" {
  bucket = "${var.project}-invoices-processed-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_acl" "invoices_processed_acl" {
  bucket = aws_s3_bucket.invoices_processed.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "invoices_processed_versioning" {
  bucket = aws_s3_bucket.invoices_processed.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "invoices_processed_encryption" {
  bucket = aws_s3_bucket.invoices_processed.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket" "data_lake" {
  bucket = "${var.project}-data-lake-${random_id.suffix.hex}"
}

resource "aws_s3_bucket_acl" "data_lake_acl" {
  bucket = aws_s3_bucket.data_lake.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "data_lake_versioning" {
  bucket = aws_s3_bucket.data_lake.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data_lake_encryption" {
  bucket = aws_s3_bucket.data_lake.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "random_id" "suffix" { byte_length = 4 }

#########################
# IAM roles and policies for Lambdas, Step Functions, Glue, Textract, etc.
#########################
resource "aws_iam_role" "lambda_role" {
  name = "${var.project}-lambda-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume.json
}

data "aws_iam_policy_document" "lambda_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "lambda_basic_exec" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Inline policy giving Lambdas access to S3, Textract, DynamoDB, StepFunctions, OpenSearch and RDS
resource "aws_iam_policy" "lambda_app_policy" {
  name   = "${var.project}-lambda-app-policy"
  policy = data.aws_iam_policy_document.lambda_app_policy.json
}

data "aws_iam_policy_document" "lambda_app_policy" {
  statement {
    actions = [
      "s3:GetObject", "s3:PutObject", "s3:ListBucket",
      "textract:*",
      "dynamodb:GetItem", "dynamodb:Query", "dynamodb:PutItem",
      "states:StartExecution",
      "es:ESHttpPost", "es:ESHttpGet", "es:ESHttpPut",
      "rds-data:ExecuteStatement", "rds-data:BatchExecuteStatement"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role_policy_attachment" "attach_lambda_app_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_app_policy.arn
}

#########################
# DynamoDB for SKU/GTIN exact lookups
#########################
resource "aws_dynamodb_table" "sku_lookup" {
  name           = "${var.project}-sku-lookup"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "product_id"
  attribute {
    name = "product_id"
    type = "S"
  }
  attribute {
    name = "sku"
    type = "S"
  }
  global_secondary_index {
    name               = "sku-index"
    hash_key           = "sku"
    projection_type    = "ALL"
  }
}

#########################
# Aurora Serverless (RDS) - cluster for OLTP (facturas, productos, reglas)
#########################
resource "aws_rds_cluster" "aurora_cluster" {
  cluster_identifier = "${var.project}-aurora-cluster"
  engine             = "aurora-postgresql"
  engine_mode        = "serverless"
  backup_retention_period = 7
  skip_final_snapshot = true
}

resource "aws_rds_cluster_instance" "aurora_instances" {
  count              = 2
  identifier         = "${var.project}-aurora-idx-${count.index}"
  cluster_identifier = aws_rds_cluster.aurora_cluster.id
  engine             = "aurora-postgresql"
  instance_class     = "db.serverless" # placeholder; adjust per provider support
}

#########################
# OpenSearch domain (for hybrid text + vector search)
#########################
resource "aws_opensearch_domain" "products_index" {
  domain_name = "${var.project}-products-os"
  engine_version = "OpenSearch_2.3"
  cluster_config {
    instance_type = "r6g.large.search"
    instance_count = 2
  }
  ebs_options {
    ebs_enabled = true
    volume_size = 50
  }
  advanced_options = {
    "rest.action.multi.allow_explicit_index" = "true"
  }
  node_to_node_encryption { enabled = true }
  encrypt_at_rest { enabled = true }
}

#########################
# Redshift cluster for analytics (or consider Redshift Serverless)
#########################
resource "aws_redshift_cluster" "redshift" {
  cluster_identifier = "${var.project}-rs-cluster"
  node_type          = "dc2.large"
  number_of_nodes    = 2
  database_name      = "analytics"
  master_username    = "admin"
  master_password    = "ChangeMe123!" # replace with secrets manager in prod
}

#########################
# AWS Glue Catalog and Job (ETL from S3 -> Redshift)
#########################
resource "aws_glue_catalog_database" "data_lake_db" {
  name = "${var.project}_lake_db"
}

resource "aws_glue_job" "invoices_etl" {
  name     = "${var.project}-invoices-etl"
  role_arn = aws_iam_role.glue_role.arn
  command {
    name            = "glueetl"
    python_version  = "3"
    script_location = "s3://${aws_s3_bucket.data_lake.id}/scripts/invoices_etl.py"
  }
  max_retries = 1
  glue_version = "3.0"
}

resource "aws_iam_role" "glue_role" {
  name = "${var.project}-glue-role"
  assume_role_policy = data.aws_iam_policy_document.glue_assume.json
}

data "aws_iam_policy_document" "glue_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["glue.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "glue_service_policy" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

#########################
# Step Functions state machine (orchestration)
#########################
resource "aws_iam_role" "sfn_role" {
  name = "${var.project}-sfn-role"
  assume_role_policy = data.aws_iam_policy_document.sfn_assume.json
}

data "aws_iam_policy_document" "sfn_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["states.${data.aws_region.current.name}.amazonaws.com"]
    }
  }
}

data "aws_region" "current" {}

resource "aws_sfn_state_machine" "ingest_workflow" {
  name     = "${var.project}-ingest-workflow"
  role_arn = aws_iam_role.sfn_role.arn
  definition = <<JSON
{
  "Comment": "Ingest workflow: Textract -> Normalize -> Match -> Calc -> Persist",
  "StartAt": "CallTextract",
  "States": {
    "CallTextract": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": { "FunctionName": "${aws_lambda_function.textract_invoke.arn}", "Payload.$": "$" },
      "Next": "NormalizeLines"
    },
    "NormalizeLines": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": { "FunctionName": "${aws_lambda_function.normalize.arn}", "Payload.$": "$" },
      "Next": "MatchProducts"
    },
    "MatchProducts": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": { "FunctionName": "${aws_lambda_function.matcher.arn}", "Payload.$": "$" },
      "Next": "CalcCommissions"
    },
    "CalcCommissions": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": { "FunctionName": "${aws_lambda_function.calculator.arn}", "Payload.$": "$" },
      "End": true
    }
  }
}
JSON
}

#########################
# Lambdas (placeholders) - textract_invoke, normalize, matcher, calculator
#########################
resource "aws_lambda_function" "textract_invoke" {
  function_name = "${var.project}-textract-invoke"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "handler.lambda_handler"
  s3_bucket     = aws_s3_bucket.data_lake.id
  s3_key        = "lambdas/textract_invoke.zip" # upload code to this location
  memory_size   = 1024
  timeout       = 300
}

resource "aws_lambda_function" "normalize" {
  function_name = "${var.project}-normalize"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "handler.lambda_handler"
  s3_bucket     = aws_s3_bucket.data_lake.id
  s3_key        = "lambdas/normalize.zip"
  memory_size   = 512
  timeout       = 120
}

resource "aws_lambda_function" "matcher" {
  function_name = "${var.project}-matcher"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "handler.lambda_handler"
  s3_bucket     = aws_s3_bucket.data_lake.id
  s3_key        = "lambdas/matcher.zip"
  memory_size   = 1024
  timeout       = 120
}

resource "aws_lambda_function" "calculator" {
  function_name = "${var.project}-calculator"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.9"
  handler       = "handler.lambda_handler"
  s3_bucket     = aws_s3_bucket.data_lake.id
  s3_key        = "lambdas/calculator.zip"
  memory_size   = 1024
  timeout       = 300
}

#########################
# S3 event notification: raw bucket triggers Step Function via Lambda starter
#########################
resource "aws_lambda_function_event_invoke_config" "invoke_config" {
  function_name = aws_lambda_function.textract_invoke.function_name
}

# NOTE: For simplicity we attach a bucket notification using lambda permission and aws_s3_bucket_notification is not fully defined here.

#########################
# Outputs
#########################
output "s3_raw_bucket" { value = aws_s3_bucket.invoices_raw.bucket }
output "s3_processed_bucket" { value = aws_s3_bucket.invoices_processed.bucket }
output "opensearch_endpoint" { value = aws_opensearch_domain.products_index.endpoint }
output "redshift_endpoint" { value = aws_redshift_cluster.redshift.endpoint }
output "aurora_cluster_arn" { value = aws_rds_cluster.aurora_cluster.arn }

# End of terraform file
# --------------------
# This HCL file describes the main resources and integration points for:
# - S3 raw/processed/data-lake
# - Lambda functions to orchestrate Textract, normalization, matching and calculations
# - Step Functions orchestration
# - DynamoDB for fast lookups
# - Aurora (OLTP) and Redshift (analytics)
# - OpenSearch for hybrid text+vector search
# - Glue job for ETL (S3 -> Redshift)

# To render this visually you can use tools that convert terraform plans to diagrams
# (eg. terragrunt graph, terraform graph, or external tools like cloudcraft or Hava) or
# run `terraform plan` and use graphviz. Replace placeholders before applying.
