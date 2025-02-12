terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "2.46.0"
    }
  }
}
provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_container_registry" "gr_registry" {
  name                   = "game-recommender"
  subscription_tier_slug = "starter"
}

resource "digitalocean_kubernetes_cluster" "gr_cluster" {
  name    = "my-k8s-cluster"
  region  = "ams3"
  version = "1.28.0-do.0"

  node_pool {
    name       = "default-node-pool"
    size       = "s-1vcpu-2gb"
    node_count = 1
  }
}

output "registry_endpoint" {
  value = digitalocean_container_registry.gr_registry.endpoint
}
