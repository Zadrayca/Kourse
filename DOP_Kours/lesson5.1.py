
from concurrent.futures import ThreadPoolExecutor, Future

pool = ThreadPoolExecutor(max_workers=4)
futures = [pool.submit(print, num) for num in range(1000)]
#fu = pool.submit(print, 'hello world')



print(futures)

#Future().