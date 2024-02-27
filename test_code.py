import sys
import time
import itertools
from itertools import accumulate, product, permutations, combinations
import collections
from collections import Counter, OrderedDict, deque, defaultdict, ChainMap
from functools import lru_cache
import math
from math import sqrt, sin, cos, tan, ceil, fabs, floor, gcd, exp, log, log2
import fractions
from typing import List, Tuple
import numpy as np
import random
import heapq
from heapq import *
stdin = sys.stdin
stdout = sys.stdout
def code():
	for _ in range(int(input())):
	    n = int(input())
	    mass = []
	    zo = 0
	    oz = 0
	    zz = 0
	    oo = 0
	    ozs = []
	    zos = []
	    ozss = set()
	    zoss = set()
	    for j in range(n):
	        k = input()
	        mass.append(k)
	        if k[0] == '0' and k[-1] == '1':
	            zoss.add(k)
	            zos.append(j + 1)
	            zo += 1
	        elif k[0] == '1' and k[-1] == '0':
	            ozss.add(k)
	            ozs.append(j + 1)
	            oz += 1
	        elif k[0] == '0' and k[-1] == '0':
	            zz += 1
	        else:
	            oo += 1
	    if zz and oo and not oz and not zo:
	        print(-1)
	        continue
	    else:
	        if zo > oz:
	            print((zo - oz) // 2)
	            ans = []
	            need = (zo - oz) // 2
	            i = 0
	            while need:
	                zzz = mass[zos[i] - 1][len(mass[zos[i] - 1]) - 1:: -1]
	                if zzz not in ozss:
	                    ans.append(zos[i])
	                    need -= 1
	                i += 1
	            print(*ans)
	        else:
	            print((oz - zo) // 2)
	            ans = []
	            need = (oz - zo) // 2
	            i = 0
	            while need:
	                zzz = mass[ozs[i] - 1][len(mass[ozs[i] - 1]) - 1:: -1]
	                if zzz not in zoss:
	                    ans.append(ozs[i])
	                    need -= 1
	                i += 1
	            print(*ans)