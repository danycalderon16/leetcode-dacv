/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let sortedNums = nums.slice().sort((a, b) => a - b);
  let triplets = new Set();
  for (let i = 0; i < sortedNums.length; i++) {
    let j = i + 1;
    let k = sortedNums.length - 1;
    while (j < k) {
      let sum = sortedNums[i] + sortedNums[j] + sortedNums[k];
      if (sum === 0) {
        triplets.add(
          JSON.stringify([sortedNums[i], sortedNums[j], sortedNums[k]])
        );
        j++;
        k--;
      }
      if (sum < 0) j++;
      if (sum > 0) k--;
    }
  }

  return Array.from(triplets).map((triplet) => JSON.parse(triplet));
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
