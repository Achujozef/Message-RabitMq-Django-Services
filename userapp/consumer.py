import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "userapp.settings")
django.setup()

from main.models import Product
from django.core.exceptions import ObjectDoesNotExist

params = pika.URLParameters('amqp://guest:guest@localhost:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='userapp')

def callback(ch, method, properties, body):
    print('Received in UserApp')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        product.save()
        print('Product Created')

    elif properties.content_type == 'product_updated':
        try:
            product = Product.objects.get(id=data['id'])
            product.title = data['title']
            product.image = data['image']
            product.save()
            print('Product Updated')
        except ObjectDoesNotExist:
            print('Product not found')

    elif properties.content_type == 'product_deleted':
        try:
            product = Product.objects.get(id=data)
            product.delete()
            print('Product Deleted')
        except ObjectDoesNotExist:
            print('Product not found')

channel.basic_consume(queue='userapp', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
