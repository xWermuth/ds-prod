#! /bin/bash
kubectl apply -f ./exercise12/config-map.yml
kubectl apply -f ./recommender.yml
kubectl apply -f ./feedback.yml
kubectl apply -f ./user_activity.yml
kubectl apply -f ./exercise12/prometheus_deploy.yml
kubectl apply -f ./exercise12/grafana_deploy.yml