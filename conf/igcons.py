# coding=utf-8

jwt = True
# Secret for JWT
JWT_SECRET = '7aym5RUek2J1TzE09uJEOuQ2RiNkTNwSqGapImlzAMA'

# Database URI, example: mysql://username:password@server/db?charset=utf8mb4
# SQLALCHEMY_DATABASE_URI = ''

server_address = 'localhost:8068'
spider_service_address = 'localhost:8012'
expand_service_address = 'localhost:8020'
judge_service_address = ''

task_context_dir = '/home/carrie/workbench/igcons/igcons/.task_context/'
spider_dir = '/home/carrie/workbench/Spiderflow/'
expand_dir = '/home/carrie/workbench/Expandflow/'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/igcons?charset=utf8mb4'