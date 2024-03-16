/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  let left = searchLeft(nums, target, 0, nums.length - 1);
  let right = searchRight(nums, target, 0, nums.length - 1);
  return left > right ? [-1, -1] : [left, right];
};

function searchLeft(nums, target, left, right) {
  while (left <= right) {
    const mid = (left + right) >> 1;
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return left;
}

function searchRight(nums, target, left, right) {
  while (left <= right) {
    const mid = (left + right) >> 1;
    if (nums[mid] <= target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return right;
}

console.log(searchRange([5, 7, 7, 8, 8, 10], 8));
