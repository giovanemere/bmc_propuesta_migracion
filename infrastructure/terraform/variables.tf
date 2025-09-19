# BMC Infrastructure Variables

variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "prod"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "bmc"
}

# VPC Configuration
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

# RDS Configuration (60M Products)
variable "rds_instance_class" {
  description = "RDS instance class for 60M products"
  type        = string
  default     = "db.r6g.2xlarge"
}

variable "rds_allocated_storage" {
  description = "Initial allocated storage in GB"
  type        = number
  default     = 1000
}

variable "rds_max_allocated_storage" {
  description = "Maximum allocated storage in GB"
  type        = number
  default     = 5000
}

# ElastiCache Configuration
variable "redis_node_type" {
  description = "ElastiCache Redis node type"
  type        = string
  default     = "cache.r6g.xlarge"
}

variable "redis_num_nodes" {
  description = "Number of Redis cache nodes"
  type        = number
  default     = 3
}

# ECS Configuration
variable "ecs_cpu" {
  description = "CPU units for ECS tasks"
  type        = number
  default     = 2048
}

variable "ecs_memory" {
  description = "Memory for ECS tasks"
  type        = number
  default     = 4096
}

# Microservices Configuration
variable "microservices" {
  description = "Microservices configuration"
  type = map(object({
    cpu    = number
    memory = number
    port   = number
    min_capacity = number
    max_capacity = number
  }))
  
  default = {
    invoice = {
      cpu    = 2048
      memory = 4096
      port   = 8000
      min_capacity = 2
      max_capacity = 10
    }
    product = {
      cpu    = 4096
      memory = 8192
      port   = 8001
      min_capacity = 3
      max_capacity = 15
    }
    ocr = {
      cpu    = 2048
      memory = 4096
      port   = 8002
      min_capacity = 2
      max_capacity = 8
    }
    commission = {
      cpu    = 1024
      memory = 2048
      port   = 8003
      min_capacity = 2
      max_capacity = 6
    }
    certificate = {
      cpu    = 1024
      memory = 2048
      port   = 8004
      min_capacity = 2
      max_capacity = 5
    }
  }
}

# Lambda Configuration
variable "lambda_runtime" {
  description = "Lambda runtime"
  type        = string
  default     = "python3.9"
}

variable "lambda_timeout" {
  description = "Lambda timeout in seconds"
  type        = number
  default     = 300
}

# Monitoring Configuration
variable "enable_detailed_monitoring" {
  description = "Enable detailed CloudWatch monitoring"
  type        = bool
  default     = true
}

variable "log_retention_days" {
  description = "CloudWatch log retention in days"
  type        = number
  default     = 30
}

# Security Configuration
variable "enable_waf" {
  description = "Enable AWS WAF"
  type        = bool
  default     = true
}

variable "enable_shield" {
  description = "Enable AWS Shield Advanced"
  type        = bool
  default     = false
}

# Backup Configuration
variable "backup_retention_days" {
  description = "Backup retention period in days"
  type        = number
  default     = 35
}

variable "enable_cross_region_backup" {
  description = "Enable cross-region backup"
  type        = bool
  default     = true
}

# Cost Optimization
variable "enable_spot_instances" {
  description = "Enable Spot instances for non-critical workloads"
  type        = bool
  default     = false
}

variable "s3_intelligent_tiering" {
  description = "Enable S3 Intelligent Tiering"
  type        = bool
  default     = true
}
