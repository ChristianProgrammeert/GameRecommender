provider "digitalocean" {
  token = var.do_token
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
