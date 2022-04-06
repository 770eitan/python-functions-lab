def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum


  
#challenge 2
def largest(nums):
  nums.sort()
  return nums[-1]

#challenge 3
def occurances(string, substr):
  return string.count(substr)

#challenge4
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product