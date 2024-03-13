function binarySearh(nums, target) {
  let left = 0;
  let right = nums.length - 1;
  return bsr(nums, target, left, right);
}

function bsr(nums, target, left, right) {
  if (left > right) {
    return -1;
  } else {
    const piv = Math.ceil((right + left) / 2);
    if (nums[piv] === target) {
      return piv;
    } else {
      if (target < nums[piv]) {
        return bsr(nums, target, left, piv - 1);
      } else {
        return bsr(nums, target, piv + 1, right);
      }
    }
  }
}

console.log(binarySearh([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1));
