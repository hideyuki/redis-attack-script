# -*- coding: utf-8 -*-

import redis
import time

BENCH_COUNT = 10000
HOST = "127.0.0.1"
PORT = 6379
DB = 3
KEY = "test_key"

r=redis.Redis(host=HOST, port=PORT, db=DB)

t_before = time.time() * 1000
for i in range(BENCH_COUNT):
  r.set(KEY, i)
  if int(r.get(KEY)) != i:
    print("error")
    break
t_after = time.time() * 1000

print "SET/GET (%dtimes): %fms" % (BENCH_COUNT, t_after-t_before)


