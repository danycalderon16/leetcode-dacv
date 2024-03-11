function findLongestSubArray(arr, target) {
  let left = 1;
  let rigth = 1;
  let accum = 0;

  for (let i = 0; i < arr.length; i++) {
    accum += arr[i];
    while (accum <= target) {}
  }

  return [left, rigth];
}

console.log(findLongestSubArray([1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], 15));
