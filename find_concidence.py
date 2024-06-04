def find(num_a, num_b, limit):
  multi_a = num_a
  multi_b = num_b
  while multi_a <= limit:
    if multi_a == multi_b:
      return multi_a
    if multi_a < multi_b:
      multi_a += num_a
      continue
    if multi_a > multi_b:
      multi_b += num_b
  
  return -1

if __name__ == '__main__':
  num_a = 37
  num_b = 79
  limit = 10000
  print(find(num_a, num_b, limit))