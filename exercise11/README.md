# Exercise 11

## Installing Dependencies

```bash
brew install minikube
brew install hyperkit
```

## Useful commands

```bash
minikube start
eval $(minikube -p minikube docker-env) # Point the minicube to the docker daemon
minikube status                         # Status of minicube
ssh minikube
kubectl run nginx --image=nginx         # Run docker image in kubernetes
kubectl get all                         # See what's running on your Minikube cluster - all | service | deployment | pod
minikube stop
```

## Commands

```bash
kubectl apply -f secret.yaml # apply or create the deployment
kubectl apply -f configmap.yaml # apply secret and configmap first (dependencies)
kubectl apply -f mongo.yaml
kubectl apply -f mongoexpress.yaml
kubectl apply –f . # apply all yaml files in current dir
minikube service --url mongo-express-service # inspect service
kubectl delete all --all # deletes all the deployments, services, etc.
```
