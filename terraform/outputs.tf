output "kubeconfig" {
  value = digitalocean_kubernetes_cluster.gr_cluster.kube_config[0].raw_config
  sensitive = true
  description = "Kubeconfig file for accessing the Kubernetes cluster"
}