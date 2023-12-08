# Kubernetes deployment

```bash
> kubectl apply -f k8s/app_python/deployment.yml -f k8s/app_python/service.yml -f k8s/app_rust/deployment.yml -f k8s/app_rust/service.yml

deployment.apps/app-python created
service/app-python created
deployment.apps/app-rust created
service/app-rust created
```

```bash
> kubectl get po,svc
NAME                              READY   STATUS    RESTARTS   AGE
pod/app-python-644dc76bd9-d8bhn   1/1     Running   0          28s
pod/app-python-644dc76bd9-ntpcw   1/1     Running   0          27s
pod/app-python-644dc76bd9-tgrlc   1/1     Running   0          27s
pod/app-rust-5d9cfbd577-9d589     1/1     Running   0          27s
pod/app-rust-5d9cfbd577-cdqdl     1/1     Running   0          27s
pod/app-rust-5d9cfbd577-g77bk     1/1     Running   0          27s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
service/app-python   ClusterIP   10.106.19.149   <none>        80/TCP    28s
service/app-rust     ClusterIP   10.111.17.193   <none>        80/TCP    27s
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   10m
```

```bash
minikube service --all
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | app-python |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/app-python has no node port
|-----------|----------|-------------|--------------|
| NAMESPACE |   NAME   | TARGET PORT |     URL      |
|-----------|----------|-------------|--------------|
| default   | app-rust |             | No node port |
|-----------|----------|-------------|--------------|
😿  service default/app-rust has no node port
|-----------|------------|-------------|--------------|
| NAMESPACE |    NAME    | TARGET PORT |     URL      |
|-----------|------------|-------------|--------------|
| default   | kubernetes |             | No node port |
|-----------|------------|-------------|--------------|
😿  service default/kubernetes has no node port
```

## Enable ingress

```bash
> minikube addons enable ingress
...
🌟  The 'ingress' addon is enabled
```

```bash
> kubectl apply -f ingress.yml
ingress.networking.k8s.io/common-ingress created
```

## Test applications

```bash
> curl -H "Host: app-rust" http://$(minikube ip)/
2023-11-06T21:59:35.599201360+03:00
```

```bash
> curl -H "Host: app-python" http://$(minikube ip)/notes/
[]
```
