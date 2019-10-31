# Note for how to use google cloud service

This notes is guide how to use google pubsub.

## Important
### To create a topic
```
gcloud pubsub topics create topic_name
```

### To create a subscriptions
```
gcloud pubsub subscriptions create --topic topic_name subscription_name
```

### To publish message
#### From gsutils
```
gcloud pubsub topics publish topic_name --message "hello"
```
#### From code
```
message_pubsub = {}

publisher_crack = pubsub_v1.PublisherClient()
topic_path = publisher_crack.topic_path(project_id, topic_name)
publisher_crack.publish(topic_path, data=json.dumps(message_pubsub).encode('utf-8'))
```

### To Receive message
#### From gsutils
```
gcloud pubsub subscriptions pull --auto-ack subscription_name
```
#### From code
```
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_name)

def callback(message):
    print('Received message: {}'.format(message))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

```

### To activate notification from storage
```
gsutil notification create -t topic_name -f json -e type_event -p path_storage storage_name
```

