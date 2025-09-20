# Configuración de Infraestructura AWS

## Terraform Configuration

### VPC y Networking
```hcl
resource "aws_vpc" "bmc_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "BMC-VPC"
    Environment = "production"
  }
}

resource "aws_subnet" "private_subnets" {
  count             = 3
  vpc_id            = aws_vpc.bmc_vpc.id
  cidr_block        = "10.0.${count.index + 1}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "BMC-Private-Subnet-${count.index + 1}"
  }
}
```

### ECS Cluster
```hcl
resource "aws_ecs_cluster" "bmc_cluster" {
  name = "bmc-production"
  
  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_ecs_service" "invoice_service" {
  name            = "invoice-service"
  cluster         = aws_ecs_cluster.bmc_cluster.id
  task_definition = aws_ecs_task_definition.invoice_task.arn
  desired_count   = 2
  
  deployment_configuration {
    maximum_percent         = 200
    minimum_healthy_percent = 100
  }
}
```

### RDS Configuration
```hcl
resource "aws_db_instance" "bmc_postgres" {
  identifier = "bmc-postgres-prod"
  
  engine         = "postgres"
  engine_version = "14.9"
  instance_class = "db.r6g.2xlarge"
  
  allocated_storage     = 1000
  max_allocated_storage = 5000
  storage_type         = "gp3"
  storage_encrypted    = true
  
  multi_az               = true
  backup_retention_period = 7
  backup_window          = "03:00-04:00"
  maintenance_window     = "sun:04:00-sun:05:00"
  
  performance_insights_enabled = true
}
```

## Monitoring y Alertas

### CloudWatch Dashboards
```json
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/ECS", "CPUUtilization", "ServiceName", "invoice-service"],
          ["AWS/ECS", "MemoryUtilization", "ServiceName", "invoice-service"]
        ],
        "period": 300,
        "stat": "Average",
        "region": "us-east-1",
        "title": "Invoice Service Metrics"
      }
    }
  ]
}
```

### Alertas Críticas
- CPU > 80% por 5 minutos
- Memoria > 85% por 5 minutos  
- Error rate > 5% por 2 minutos
- Latencia > 3000ms por 3 minutos

Generado: 2025-09-19 23:10:58
