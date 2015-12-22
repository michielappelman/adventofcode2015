from celery import Celery
import day1_apartment
import day20_infinite_houses

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def run_test():
    return day1_apartment.move_up_down('()()((()())((((())')

@app.task
def find_house(presents):
    return day20_infinite_houses.house_with_presents(presents)