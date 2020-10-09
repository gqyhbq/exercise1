import random
import sys
from Interger import Integer_Calcu
from Fractional_ import Fractional_Calcu

#test_number = sys.argv[2]
#test_scopte = sys.argv[4]
test_number = 20
test_scopte = 5

i = 0
while (i < int(test_number)):
    i = i + 1
    test1 = random.randint(1,2)
    test2 = random.randint(1,3)
    if(test1 == 1):
        Integer_Calcu(i, int(test_scopte), test2)
    else:
        Fractional_Calcu(i, int(test_scopte), test2)
