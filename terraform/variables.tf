variable "do_token" {
  type        = string
  description = "DigitalOcean API Token"
  sensitive   = true
}

variable "cluster_name" {
  type        = string
  description = "Name of the Kubernetes cluster"
}

variable "region" {
  type        = string
  description = "Region where the Kubernetes cluster will be created"
}

variable "node_size" {
  type        = string
  description = "Size of the nodes in the Kubernetes cluster"
}

variable "namespace" {
  type        = string
  description = "Namespace where the application will be deployed"
}

variable "monitoring_namespace" {
  type        = string
  description = "Namespace where monitoring resources will be deployed"
}

variable "container_port" {
  type        = number
  description = "Port where the application will be exposed"
}

variable "node_count" {
  type        = number
  description = "Number of nodes in the Kubernetes cluster"
}

variable "docker_username" {
  type        = string
  description = "Docker username for the Docker registry"
}

variable "website_image" {
  type        = string
  description = "Docker image for the website deployment"
}

variable "db_user" {
  type        = string
  description = "Database user"
  sensitive   = true
}

variable "db_password" {
  type        = string
  description = "Database password"
  sensitive   = true
}

variable "db_name" {
  type        = string
  description = "Database name"
  sensitive   = true
}

variable "db_host" {
  type        = string
  description = "Database host"
  sensitive   = true
}

variable "db_port" {
  type        = number
  description = "Database port"
  sensitive   = true
}

variable "grafana_admin_password" {
  type        = string
  description = "Password for the Grafana admin user"
  sensitive   = true
}



