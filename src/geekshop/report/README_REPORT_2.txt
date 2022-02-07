ТЕСТИРОВАНИЕ РАБОТОСПОСОБНОСТИ САЙТА.

Пробный запуск siege
-----------------------------------------------------------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop# siege -f /home/django/django-start-v2/src/geekshop/geekshop_urls_combat.txt -d1 -r29 -c1
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        8059 hits
Availability:		      100.00 %
Elapsed time:		       19.43 secs
Data transferred:	        6.98 MB
Response time:		        0.00 secs
Transaction rate:	      414.77 trans/sec
Throughput:		        0.36 MB/sec
Concurrency:		        0.92
Successful transactions:        8059
Failed transactions:	           0
Longest transaction:	        0.07
Shortest transaction:	        0.00


Та же команда с прежними параметрами, но в режиме --debug:
-----------------------------------------------------------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop# siege -f /home/django/django-start-v2/src/geekshop/geekshop_urls_combat.txt -d1 -r29 -c1 --debug
** SIEGE 4.0.4: debugging enabled
** Preparing 1 concurrent users for battle.
The server is now under siege...[debug] browser.c:870 attempting connection to 31.31.201.195:80
[debug] browser.c:885 creating new socket:     31.31.201.195:80
[debug] browser.c:905 good socket connection:  31.31.201.195:80

Lifting the server siege...
Transactions:		       11352 hits
Availability:		      100.00 %
Elapsed time:		       30.28 secs
Data transferred:	        9.36 MB
Response time:		        0.00 secs
Transaction rate:	      374.90 trans/sec
Throughput:		        0.31 MB/sec
Concurrency:		        0.91
Successful transactions:       11352
HTTP OK received:	       11351
Failed transactions:	           0
Longest transaction:	        0.03
Shortest transaction:	        0.00


Запуск siege с передачей в POST данных о пользователе и пароле, для прохождения авторизации на сайте.
---------------------------------------------------------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege -f ./geekshop_urls_auth_combat.txt -d0 -r2 -c1 --debug
** SIEGE 4.0.4: debugging enabled

Copyright (C) 2017 by Jeffrey Fulmer, et al.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.

** Preparing 1 concurrent users for battle.
The server is now under siege...[debug] browser.c:870 attempting connection to 31.31.201.195:80
[debug] browser.c:885 creating new socket:     31.31.201.195:80
[debug] browser.c:905 good socket connection:  31.31.201.195:80
POST /auth/login/ HTTP/1.1
Host: 31.31.201.195
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (pc-x86_64-linux-gnu) Siege/4.0.4
Connection: close
Content-type: application/x-www-form-urlencoded
Content-length: 35

username=django&password=geekbrains

...
[debug] browser.c:870 attempting connection to 31.31.201.195:80
[debug] browser.c:885 creating new socket:     31.31.201.195:80
[debug] browser.c:905 good socket connection:  31.31.201.195:80
GET /static/debug_toolbar/js/toolbar.js HTTP/1.1
Host: 31.31.201.195
Cookie: sessionid=rbjehem2yo3ylun3it4jvlcaabnvyob2
Accept: */*
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (pc-x86_64-linux-gnu) Siege/4.0.4
Connection: close
...
(прим. В cookie есть сведения о сессии - авторизация пользователя пройдена)

Transactions:		          32 hits
Availability:		      100.00 %
Elapsed time:		        1.14 secs
Data transferred:	        1.50 MB
Response time:		        0.04 secs
Transaction rate:	       28.07 trans/sec
Throughput:		        1.32 MB/sec
Concurrency:		        0.99
Successful transactions:          32
HTTP OK received:	          30
Failed transactions:	           0
Longest transaction:	        0.59
Shortest transaction:	        0.00


ФУНКЦИОНАЛЬНОЕ ТЕСТИРОВАНИЕ.
(реализована авторизация пользователя)
--------------------------------------------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege -f ./geekshop_urls_combat.txt -d0 -r49 -c1
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1206 hits
Availability:		      100.00 %
Elapsed time:		       16.57 secs
Data transferred:	       10.50 MB
Response time:		        0.01 secs
Transaction rate:	       72.78 trans/sec
Throughput:		        0.63 MB/sec
Concurrency:		        0.99
Successful transactions:        1206
Failed transactions:	           0
Longest transaction:	        0.23
Shortest transaction:	        0.00


НАГРУЗОЧНОЕ ТЕСТИРОВАНИЕ.
---------------------------------------------------------------------
Адрес               | Переходов | Время теста, с. | Транзакций/сек | Время отклика, с.
-----------------------------------------------------------------------------------
/                       1206        16,57              72.78           0.01
/products/              2508        21.05             119.14           0.34
/product/category/1/     282        18.59              15.22           2.99
/basket/                1075        17.61              61.04           0.74
/order/                  985        15.71              62.70           0.47
/order/update/1/        1214        18.98              63.96           0.48
/order/read/1/          1130        17.82              63.41           0.47

Во всех тестах доступность сервера составила 100%
Наиболее медленным оказалась страница категорий продуктов.

Далее: количество пользователей увеличено до:

--100 - отказов нет
-------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege -f ./geekshop_urls_combat.txt -d0 -r49 -c1
** SIEGE 4.0.4
** Preparing 1 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1206 hits
Availability:		      100.00 %
Elapsed time:		       16.57 secs
Data transferred:	       10.50 MB
Response time:		        0.01 secs
Transaction rate:	       72.78 trans/sec
Throughput:		        0.63 MB/sec
Concurrency:		        0.99
Successful transactions:        1206
Failed transactions:	           0
Longest transaction:	        0.23
Shortest transaction:	        0.00


--150 - отказов нет
--------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r5 -c150
** SIEGE 4.0.4
** Preparing 150 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1886 hits
Availability:		      100.00 %
Elapsed time:		       14.56 secs
Data transferred:	       87.26 MB
Response time:		        0.49 secs
Transaction rate:	      129.53 trans/sec
Throughput:		        5.99 MB/sec
Concurrency:		       63.33
Successful transactions:        1886
Failed transactions:	           0
Longest transaction:	       14.25
Shortest transaction:	        0.00


--175 - отказов нет
--------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r5 -c175
** SIEGE 4.0.4
** Preparing 175 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1755 hits
Availability:		      100.00 %
Elapsed time:		       12.84 secs
Data transferred:	       81.22 MB
Response time:		        0.44 secs
Transaction rate:	      136.68 trans/sec
Throughput:		        6.33 MB/sec
Concurrency:		       59.87
Successful transactions:        1755
Failed transactions:	           0
Longest transaction:	       12.68
Shortest transaction:	        0.00


--200 - отказов нет
-------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r5 -c175
** SIEGE 4.0.4
** Preparing 175 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1755 hits
Availability:		      100.00 %
Elapsed time:		       12.84 secs
Data transferred:	       81.22 MB
Response time:		        0.44 secs
Transaction rate:	      136.68 trans/sec
Throughput:		        6.33 MB/sec
Concurrency:		       59.87
Successful transactions:        1755
Failed transactions:	           0
Longest transaction:	       12.68
Shortest transaction:	        0.00


--225 - отказов нет
--------------------------------
env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r5 -c225
** SIEGE 4.0.4
** Preparing 225 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1720 hits
Availability:		      100.00 %
Elapsed time:		       13.08 secs
Data transferred:	       79.48 MB
Response time:		        0.43 secs
Transaction rate:	      131.50 trans/sec
Throughput:		        6.08 MB/sec
Concurrency:		       56.49
Successful transactions:        1720
Failed transactions:	           0
Longest transaction:	       12.66
Shortest transaction:	        0.00


--255 - отказов нет (более - ограничение)
--------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r5 -c1000

================================================================
WARNING: The number of users is capped at 255.  To increase this
         limit, search your .siegerc file for 'limit' and change
         its value. Make sure you read the instructions there...
================================================================
** SIEGE 4.0.4
** Preparing 255 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        1590 hits
Availability:		      100.00 %
Elapsed time:		       12.49 secs
Data transferred:	       73.58 MB
Response time:		        0.42 secs
Transaction rate:	      127.30 trans/sec
Throughput:		        5.89 MB/sec
Concurrency:		       53.82
Successful transactions:        1590
Failed transactions:	           0
Longest transaction:	       12.06
Shortest transaction:	        0.00


Увеличиваем количество запросов:
---------------------------------------------------------------
шагом в 100 и так до...
...
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r3000 -c250
** SIEGE 4.0.4
** Preparing 250 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		         210 hits
Availability:		      100.00 %
Elapsed time:		       11.94 secs
Data transferred:	        9.72 MB
Response time:		        0.74 secs
Transaction rate:	       17.59 trans/sec
Throughput:		        0.81 MB/sec
Concurrency:		       13.01
Successful transactions:         210
Failed transactions:	           0
Longest transaction:	       11.71
Shortest transaction:	        0.00

...
Отказ сервера произошел при следующих параметрах
-----------------------------------------------------------------
(env) root@31-31-201-195:/home/django/django-start-v2/src/geekshop/siege_test# siege http://31.31.201.195:80/ -d0 -r3001 -c250
** SIEGE 4.0.4
** Preparing 250 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		           0 hits
Availability:		        0.00 %
Elapsed time:		       10.23 secs
Data transferred:	        0.00 MB
Response time:		        0.00 secs
Transaction rate:	        0.00 trans/sec
Throughput:		        0.00 MB/sec
Concurrency:		        0.00
Successful transactions:           0
Failed transactions:	           0
Longest transaction:	        0.00
Shortest transaction:	        0.00
