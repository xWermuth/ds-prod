#! /bin/bash
kubectl apply -f ./config-map.yml
kubectl apply -f ./prometheus_deploy.yml