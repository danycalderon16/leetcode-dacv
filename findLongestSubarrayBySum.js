function findLongestSubArray(arr, target) {
  let result = [-1];
  let left = 0;
  let right = 0;
  let sum = 0;

  while (right < arr.length) {
    sum += arr[right];
    while (left < right && sum > target) {
      sum -= arr[left++];
    }
    if (
      sum === target &&
      (result.length === 1 || result[1] - result[0] < right - left)
    ) {
      result = [left + 1, right + 1];
    }
    right++;
  }

  return result;
}

console.log(findLongestSubArray([1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], 15));
