#!/bin/bash
apk add gcc libc-dev libpthread-stubs librtmp

gcc -O3 -o exec util.c ds_queue.c aho.c handopt.c -Wno-unused-result -lrt -lpthread -Wall -march=native -fgnu89-inline
