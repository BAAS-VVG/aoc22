import time

from d1 import d1
from d10 import d10
from d11 import d11
from d12 import d12
from d13 import d13
from d14 import d14
from d15 import d15, d15_2
from d16 import d16
from d17 import d17
from d18 import d18
from d19 import d19
from d2 import d2
from d20 import d20
from d21 import d21
from d22 import d22
from d23 import d23
from d24 import d24
from d25 import d25
from d3 import d3
from d4 import d4
from d5 import d5
from d6 import d6
from d7 import d7
from d8 import d8
from d9 import d9

if __name__ == '__main__':
    start_time = time.time()
    # d1()
    # d2()
    # d3()
    # d4()
    # d5()
    # d6()
    # d7()
    # d8()
    # d9()
    d10()
    d11()
    d12()
    d13()
    d14()
    # d15()  # SLOW
    d15_2()  # FAST
    d16()
    d17()
    d18()
    d19()
    d20()
    d21()
    d22()
    d23()
    d24()
    d25()
    print("--- %s seconds ---" % (time.time() - start_time))
