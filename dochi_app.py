from celery import Celery
 
app = Celery(
    'my_tasks'
    , broker='amqp://heo:heo@localhost:5672//'
    , backend='amqp://' # rpc -> amqp
    , include=[
        'tasks.example'
        , 'tasks.calc'
    ]
)