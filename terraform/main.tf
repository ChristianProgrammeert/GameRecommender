# Providers instellen
terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = var.do_token
}


provider "kubernetes" {
  host                   = digitalocean_kubernetes_cluster.gr_cluster.endpoint
  token                  = digitalocean_kubernetes_cluster.gr_cluster.kube_config[0].token
  cluster_ca_certificate = base64decode(digitalocean_kubernetes_cluster.gr_cluster.kube_config[0].cluster_ca_certificate)
}

provider "helm" {
  kubernetes {
    host                   = digitalocean_kubernetes_cluster.gr_cluster.endpoint
    token                  = digitalocean_kubernetes_cluster.gr_cluster.kube_config[0].token
    cluster_ca_certificate = base64decode(digitalocean_kubernetes_cluster.gr_cluster.kube_config[0].cluster_ca_certificate)
  }
}


# Kubernetes-cluster aanmaken
resource "digitalocean_kubernetes_cluster" "gr_cluster" {
  name    = var.cluster_name
  region  = var.region
  version = "1.32.1-do.0"

  node_pool {
    name       = "gameapi"
    size       = var.node_size
    node_count = var.node_count
  }
}

# Namespaces
resource "kubernetes_namespace" "app_namespace" {
  metadata {
    name = var.namespace
  }
}

resource "kubernetes_namespace" "monitoring_namespace" {
  metadata {
    name = var.monitoring_namespace
  }
}

resource "kubernetes_secret" "docker_registry" {
  metadata {
    name      = "docker-registry"
    namespace = kubernetes_namespace.app_namespace.metadata[0].name
  }
  type = "kubernetes.io/dockerconfigjson"

  data = {
    ".dockerconfigjson" = jsonencode({
      auths = {
        "registry.digitalocean.com" = {
          username = var.docker_username
          password = var.do_token
          auth     = base64encode("${var.docker_username}:${var.do_token}")
        }
      }
    })
  }
}

resource "kubernetes_config_map" "grafana_dashboard" {
  metadata {
    name      = "gameapi-cluster-dashboard"
    namespace = kubernetes_namespace.monitoring_namespace.metadata[0].name
    labels = {
      grafana_dashboard = "1"
    }
  }

    data = {
    "cluster-monitoring-dashboard.json" = file("${path.module}/grafana/dashboards/cluster-monitoring-dashboard.json")
  }
}


# Helm Release: Prometheus
resource "helm_release" "prometheus" {
  chart      = "kube-prometheus-stack"
  name       = "prometheus"
  namespace  = kubernetes_namespace.monitoring_namespace.metadata[0].name
  repository = "https://prometheus-community.github.io/helm-charts"
  version    = "56.3.0"
  values = [file("${path.module}/values.yaml")]

  set {
    name  = "podSecurityPolicy.enabled"
    value = true
  }

  set {
    name  = "server.persistentVolume.enabled"
    value = false
  }

    set {
    name  = "grafana.adminPassword"
    value = var.grafana_admin_password
  }
}

# Website Deployment binnen het Kubernetes-cluster
resource "kubernetes_deployment" "website" {
  metadata {
    name      = "website"
    namespace = var.namespace
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "website"
      }
    }

    strategy {
      type = "RollingUpdate"
      rolling_update {
        max_unavailable = 0
      }
    }

    template {
      metadata {
        labels = {
          app = "website"
        }
      }
      spec {
        image_pull_secrets {
          name = kubernetes_secret.docker_registry.metadata[0].name
        }
        container {
          name  = "website"
          image = "registry.digitalocean.com/game-recommender/gameapi:latest"
          image_pull_policy = "Always"
          port {
            container_port = 8000
          }
          env {
            name  = "DATABASE_URL"
            value = "postgresql://${var.db_user}:${var.db_password}@${var.db_host}:${var.db_port}/${var.db_name}?sslmode=require&connect_timeout=60"
          }
        }
          image_pull_secrets {
          name = "docker_registry"
        }
      }

    }
  }
}


resource "kubernetes_service" "gameapi-loadbalancer" {
  metadata {
    name      = "gameapi-loadbalancer"
    namespace = kubernetes_namespace.app_namespace.metadata[0].name
  }

  spec {
    selector = {
      app = "website" # Match labels van je deployment
    }

    port {
      protocol    = "TCP"
      port        = 80       # Externe poort
      target_port = var.container_port    # Poort waar je app luistert
    }

    type = "LoadBalancer"
  }
}