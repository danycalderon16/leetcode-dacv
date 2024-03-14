/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  if (x === 0 || x === 1) return x;
  let left = 0;
  let right = x;

  return bs(x, left, right);
};

function bs(x, left, right) {
  if (left > right) return left - 1;
  else {
    const middle = Math.floor((right + left) / 2);
    if (middle * middle === x) return middle;
    else {
      if (middle * middle > x) {
        return bs(x, left, middle - 1);
      } else {
        return bs(x, middle + 1, right);
      }
    }
  }
}

console.log(mySqrt(14));

//| 2 3 | 4 5 | 6 7 8 | 9 10 11 12 13 14
