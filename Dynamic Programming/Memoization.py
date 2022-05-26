def add80(n):
  print('Long time')
  return n + 80

print(add80(5))
print(add80(5))

#Memoization 1

cache = {}

def memoization(n):
  if n in cache:
    return n + 80
  else:
    print('Long time')
    cache[n] = n + 80
    return cache[n]

print(memoization(6))
print(memoization(6))

#Memoization 2
def memoization():
  cache = {}

  def memoized(n):
      if n in cache:
        return n + 80
      else:
        print('Long time')
        cache[n] = n + 80
        return cache[n]
  return memoized

memo = memoization()
print(memo(7))
print(memo(7))



# https://docs.python.org/3.3/library/functools.html --> Doc for lru_cache

from functools import lru_cache

@lru_cache(maxsize = 1000)
def memoized2add80(n):
  return n + 80


print(memoized2add80(8))
print(memoized2add80(8))
print(memoized2add80.cache_info())



