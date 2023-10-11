#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(15):
    sleep(random.random())
    sys.stdout.write("Welcome My Friend")
    sys.stdout.flush()

