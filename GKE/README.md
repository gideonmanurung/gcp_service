# Google-Cloud-Note

## WARNING !!!
Never **DELETE** this service accounts in your project [im and admin/IAM]:
- Compute Engine default service account
- Cloud Build Service Account (in Role column)
- Google APIs Service Agent
- App Engine default service account
- Compute Engine Service Agent 
- Kubernetes Engine Service Agent
- Google Container Registry Service Agent 
- App Engine Flexible Environment Service Agent 
- Cloud Build Service Agent (in Role column)

IF unfortunately you delete one of it, your GKE never successfully deployed, the example errors are:
- FAILED PRECONDITION: the app engine service account not exist in this [your project name]

SOLUTION: Make new project, ensure you don't delete it again.

## Service Account Requirements:
To deploy app engine, your service account has contain this permissions:
- Kubernetes engine admin
- Cloud Build Service Account

IF still fail to deploy: set service account as project owner. kwkwkwkwmk

## Command:
#### Yaml Format
```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: my-app #name app
  labels:
    name: my-app #name app
spec:
  replicas: 1 # to set number of replicas
  selector:
    matchLabels:
      name: my-app #name app
  template:
    metadata:
      name: my-app #name app
      labels:
        name: my-app #name app
    spec:
      containers:
        - name: my-app
          image: us.gcr.io/qoala-217505/ocr_project/my-app
          ports:
            - containerPort: 8080
          resources:
            requests:
              memory: 256Mi
            limits:
              memory: 512Mi
          env:
            - name: PORT
              value: "8080"
            - name: DEBUG_MODE
              value: "1"
```

#### Add specific configuration for gunicon
```
from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
```


#### Docker Process
```
docker build -t us.gcr.io/<project name>/<folder>/<dockername> .
docker push us.gcr.io/<project name>/<folder>/<dockername>
```
#### Deploy to google kubernete engine:
```
# create cluster
#gcloud container clusters resize <cluster name> --node-pool <pool name> --num-nodes <num nodes>
gcloud container clusters create <cluster name> --zone=asia-southeast1-a
gcloud config set compute/zone asia-southeast1-a
gcloud container clusters get-credentials <cluster name> 

# run container
kubectl run <deployment name> --image=<image url> --port=8080
# expose
kubectl expose deployment <deployment name> --type="LoadBalancer"
kubectl get service <deployment name>

# autoscale
kubectl autoscale deployment telkomedika-gke --min=<num units> --max=<num units> --cpu-percent=<num percent>

# logging pods in kubernetes

# To get all pods id
kubectl get pods --all-namespaces

# To see the log from pods
kubectl logs -f <pods id>

kubectl delete pods <pods id>

# run your app
http://EXTERNAL-IP:8080
```
```






