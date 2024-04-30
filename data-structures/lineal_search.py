def lineal_search(nums,t):
  for i in nums:
    if i == t:
      return True
  
  return False


if __name__ == "__main__":
  nums = [1,2,3,4,5,25,32,37.47,52]
  print(lineal_search(nums,235))