/**
 * @param {number} x
 * @return {number}
 */
const reverse = function (x) {
  const LIMIT = 2147483647;
  const nums = x.toString().split("").reverse();

  if (x < 0) {
    nums.pop();
    nums.unshift("-");
  }

  const res = parseInt(nums.join(""));
  return res < LIMIT * -1 || res > LIMIT ? 0 : res;
};

console.log(reverse(123));
console.log(reverse(-123));
console.log(reverse(120));
