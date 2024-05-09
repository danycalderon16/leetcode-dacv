/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  if (s.length % 2 === 1) return false;

  const arr = s.split("");

  const map = new Map();
  map.set("(", ")");
  map.set("{", "}");
  map.set("[", "]");

  const stack = [];

  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i])) {
      stack.push(map.get(arr[i]));
    } else {
      if (arr[i] === stack[stack.length - 1]) stack.pop();
      else return false;
    }
  }
  if (stack.length > 0) return false;
  return true;
};
