#!/bin/bash

set -e  # Exit immediately if a command fails

echo "Setting up Kubernetes"
doctl kubernetes cluster kubeconfig save game-cluster  # Replace with your cluster name

echo "Forcing Kubernetes to pull the latest image"
kubectl set image deployment/gameapi gameapi=registry.digitalocean.com/game-recommender/gameapi:latest --record

echo "Rolling update in progress"
kubectl rollout status deployment/gameapi

echo "Deployment successful!"

chmod +x deploy.sh