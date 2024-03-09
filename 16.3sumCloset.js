/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSumClosest = function (nums, target) {
  let sortedNums = nums.slice().sort((a, b) => a - b);
  let triplets = [];
  for (let i = 0; i < sortedNums.length; i++) {
    let j = i + 1;
    let k = sortedNums.length - 1;
    while (j < k) {
      let sum = sortedNums[i] + sortedNums[j] + sortedNums[k];
      if (sum === target) {
        return sum;
      } else {
        if (triplets.length === 0) {
          triplets.push(sum);
        } else {
          const diff = Math.abs(target - sum);
          const closets = Math.abs(target - triplets[0]);
          if (diff < closets) {
            triplets.pop();
            triplets.push(sum);
          }
        }
      }

      if (sum < target) j++;
      if (sum > target) k--;
    }
  }

  return triplets[0];
};

console.log(threeSumClosest([-1, 2, 1, -4], 1));
