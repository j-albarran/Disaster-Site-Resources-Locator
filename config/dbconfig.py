#Database configuration information

import psycopg2
'''import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port'''

dbname = 'd3efu32or6poc9'
user = 'wwoiuehjrodcic'
password = '9b88e61f237fce06035bde4baf4299e6c1134cabbcc20429c8030e67ce97d235'
host = 'ec2-107-21-201-57.compute-1.amazonaws.com'
port = '5432'
sslmode = 'require'

conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            sslmode=sslmode
            )
