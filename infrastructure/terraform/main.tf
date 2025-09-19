# BMC AWS Infrastructure - Main Configuration
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "BMC-Migration"
      Environment = var.environment
      ManagedBy   = "Terraform"
      Owner       = "BMC-Team"
    }
  }
}

# Data sources
data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_caller_identity" "current" {}

# Local values
locals {
  name_prefix = "${var.project_name}-${var.environment}"
  azs         = slice(data.aws_availability_zones.available.names, 0, 3)
  
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

# VPC and Networking
module "vpc" {
  source = "./modules/vpc"
  
  name_prefix = local.name_prefix
  cidr_block  = var.vpc_cidr
  azs         = local.azs
  
  tags = local.common_tags
}

# Security Groups
module "security_groups" {
  source = "./modules/security"
  
  name_prefix = local.name_prefix
  vpc_id      = module.vpc.vpc_id
  
  tags = local.common_tags
}

# RDS PostgreSQL (60M Products)
module "rds" {
  source = "./modules/rds"
  
  name_prefix           = local.name_prefix
  vpc_id               = module.vpc.vpc_id
  private_subnet_ids   = module.vpc.private_subnet_ids
  security_group_ids   = [module.security_groups.rds_sg_id]
  
  instance_class       = var.rds_instance_class
  allocated_storage    = var.rds_allocated_storage
  max_allocated_storage = var.rds_max_allocated_storage
  
  tags = local.common_tags
}

# ElastiCache Redis
module "elasticache" {
  source = "./modules/elasticache"
  
  name_prefix        = local.name_prefix
  vpc_id            = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  security_group_ids = [module.security_groups.redis_sg_id]
  
  node_type         = var.redis_node_type
  num_cache_nodes   = var.redis_num_nodes
  
  tags = local.common_tags
}

# S3 Buckets
module "s3" {
  source = "./modules/s3"
  
  name_prefix = local.name_prefix
  environment = var.environment
  
  tags = local.common_tags
}

# ECS Fargate Cluster
module "ecs" {
  source = "./modules/ecs"
  
  name_prefix        = local.name_prefix
  vpc_id            = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  public_subnet_ids  = module.vpc.public_subnet_ids
  security_group_ids = [module.security_groups.ecs_sg_id]
  
  tags = local.common_tags
}

# API Gateway
module "api_gateway" {
  source = "./modules/api_gateway"
  
  name_prefix = local.name_prefix
  environment = var.environment
  
  tags = local.common_tags
}

# Lambda Functions
module "lambda" {
  source = "./modules/lambda"
  
  name_prefix        = local.name_prefix
  vpc_id            = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  security_group_ids = [module.security_groups.lambda_sg_id]
  
  s3_bucket_name = module.s3.documents_bucket_name
  
  tags = local.common_tags
}

# EventBridge
module "eventbridge" {
  source = "./modules/eventbridge"
  
  name_prefix = local.name_prefix
  
  tags = local.common_tags
}

# SQS Queues
module "sqs" {
  source = "./modules/sqs"
  
  name_prefix = local.name_prefix
  
  tags = local.common_tags
}

# SNS Topics
module "sns" {
  source = "./modules/sns"
  
  name_prefix = local.name_prefix
  
  tags = local.common_tags
}

# CloudWatch
module "cloudwatch" {
  source = "./modules/cloudwatch"
  
  name_prefix = local.name_prefix
  
  tags = local.common_tags
}

# Cognito
module "cognito" {
  source = "./modules/cognito"
  
  name_prefix = local.name_prefix
  
  tags = local.common_tags
}

# Transfer Family (SFTP)
module "transfer_family" {
  source = "./modules/transfer_family"
  
  name_prefix        = local.name_prefix
  vpc_id            = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_subnet_ids
  s3_bucket_arn     = module.s3.sftp_bucket_arn
  
  tags = local.common_tags
}
