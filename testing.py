import cython_example
import timeit


cy = timeit.timeit('cython_example.test(500)', setup="import cython_example", number=100000)
my_py = timeit.timeit('python_example.test(500)', setup='import python_example', number=100000)
print(cy, my_py)
print(f"Cython is {my_py/cy}x faster")

