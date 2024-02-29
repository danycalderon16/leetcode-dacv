/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  const chars = s.split("");
  const LIMIT = 2147483647;
  const allowsChars = [32, 43, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57];
  let number = "";
  let firstLetter = false;
  let firstNumbers = false;
  for (let i = 0; i < chars.length; i++) {
    const element = chars[i] + "";
    // if (element === " ") continue;
    if (allowsChars.includes(element.charCodeAt(0))) {
      number += chars[i];
      !firstLetter && !firstNumbers ? (firstNumbers = true) : firstNumbers;
      continue;
    }
    console.log(number);
    if (!firstNumbers) return 0;
    if (firstNumbers) break;
  }
  const res = parseInt(number);
  if (isNaN(res)) return 0;
  return res > LIMIT ? LIMIT : res < -LIMIT ? -LIMIT - 1 : res;
};

console.log(myAtoi("   +0 123"));
