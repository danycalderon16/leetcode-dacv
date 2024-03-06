/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
  const matchers = [".", "*"];
  const str = s.split("");
  const patter = p.split("");
  const j = 0;
  for (let i = 0; i < str.length; i++) {
    const c = str[i];
    const pa = patter[j];
    if (c == pa) {
      j++;
      continue;
    }
    if (pa === ".") {
      j++;
      continue;
    }
    if (pa === "*") {
    }
  }
};
console.log(isMatch("aa ", "a"));
