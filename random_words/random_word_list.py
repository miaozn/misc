#!/usr/bin/python2.7
import sys
from random import randint

k = int(sys.argv[1])
if k < 1:
    print 'ERROR: k must be positive'
    sys.exit(0)
    



result = []
count = 0
with open('words_alpha.txt', 'r') as f:
    # Waterman's Reservoir Sampling Algorithm 
    for line in f:
        word = line.strip()
        count += 1
        if count == 1:
            result.append(word)
        else:
            x = randint(1, count)
            # let keep this word in 
            # possibility = k / count            
            if x <= k:
                if count <= k:
                    result.append(word)
                else:
                    # select 1 in k and replace
                    y = randint(0, k - 1)
                    result[y] = word
            
        
print result