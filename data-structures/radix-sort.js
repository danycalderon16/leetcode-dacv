function radixSort(nums = []) {
  let high = 0;
  nums.forEach((el) => {
    if (el.length > high) high = el.length;
  });
  for (let i = 0; i < nums.length; i++) {
    while (nums[i].length < high) {
      nums[i] = "0" + nums[i];
    }
  }
  for (let i = high - 1; i >= 0; i--) {
    const subs = Array.from({ length: 10 }, () => []);
    for (let j = 0; j < nums.length; j++) {
      const pos = parseInt(nums[j].charAt(i));
      subs[pos].push(nums[j]);
    }
    nums = subs.flatMap((el) => el);
  }

  return nums;
}

console.log(
  radixSort(["31", "7", "14", "144", "111", "13", "1878", "43", "102"])
);
