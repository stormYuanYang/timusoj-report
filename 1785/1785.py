import sys
import math

A = [
    [1   , 4   , "few"    ],
    [5   , 9   , "several"],
    [10  , 19  , "pack"   ],
    [20  , 49  , "lots"   ],
    [50  , 99  , "horde"  ],
    [100 , 249 , "throng" ],
    [250 , 499 , "swarm"  ],
    [500 , 999 , "zounds" ],
    [1000, math.inf, "legion" ],
]

length = len(A)
for lineStr in sys.stdin:
    n     = int(lineStr)
    first = 0
    last  = length - 1
    while first <= last:
        middle = first + (last - first) // 2
        if A[middle][0] <= n <= A[middle][1]:
            print(A[middle][2])
            break
        elif n < A[middle][0]:
            last = middle - 1
        else:
            first = middle + 1
