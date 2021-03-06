from google.cloud import pubsub_v1

def callback(message):
    message.ack()

def publish_message(project_id, topic_name, payload_pubsub):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    result = publisher.publish(topic_path, data=data).result()

    return result

def pull_message(project_id, subscription_name, timeout=5.0):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

    try:
        result = streaming_pull_future.result(timeout=timeout)
    except:
        result = streaming_pull_future.cancel()

    return result