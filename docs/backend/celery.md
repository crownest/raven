# Celery


## Installation of RabbitMQ
```bash
apt-get update
apt-get install rabbitmq-server
```

If you use another os: [RabbitMQ Installation for Other Distribution](https://www.rabbitmq.com/download.html)<br>
Additional document: [Install and Manage RabbitMQ](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-rabbitmq)


## Setting up RabbitMQ
```bash
rabbitmqctl add_vhost raven_vhost
rabbitmqctl set_permissions -p raven_vhost guest ".*" ".*" ".*"
```

For further information of setting up RabbitMQ: [Setting up RabbitMQ](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq)


## How to run Celery
```bash
celery -A raven worker -n raven_celery@%h
```

**If you want to see your tasks list or output status**:
```bash
celery -A raven worker -l info -n raven_celery@%h
```

Note for supervisor users: The % sign must be escaped by adding a second one: %%h.<br>
For further information of installation and running Celery: [First Steps With Celery](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html)
