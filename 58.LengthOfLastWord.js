/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  const strs = s.split(" ");
  const words = [];
  for (let i = 0; i < strs.length; i++) {
    const len = strs[i].length;
    if (len > 0) {
      words.push(strs[i]);
    }
  }

  return words[words.length - 1].length;
};

console.log(lengthOfLastWord("   fly me   to   the moon  "));
