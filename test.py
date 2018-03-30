import numpy as np
import time
from pool import Pool


def my_function(x):
    '''
    Wastes a random amount of time, then
    returns the average of :py:obj:`x`.

    '''
    j = 0
    for i in range(np.random.randint(9999999)):
        if np.random.random() > 0.5:
            j += np.sqrt(i)
        else:
            j -= np.sqrt(i)

    return j


# Instantiate the pool
with Pool() as pool:

    tstart = time.time()

    # The iterable we'll apply ``my_function`` to
    walkers = np.arange(100)

    # Use the pool to map ``walkers`` onto the function
    res = pool.map(my_function, walkers)

    print("Time elapsed: %.3f seconds" % (time.time() - tstart))
    print(res)
