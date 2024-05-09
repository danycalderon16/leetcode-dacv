/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  const strs = s.split(" ");
  let max = 0;

  for (let i = 0; i < strs.length; i++) {
    if (strs[i].length > max) max = strs[i].length;
  }

  return max;
};

log(lengthOfLastWord("   fly me   to   the moon  "));
