/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  let len = 0;
  let last = 0;
  for (let i = 0; i < s.length; i++) {
    const letter = s.substring(i, i + 1);
    if (letter !== " ") {
      len++;
    } else {
      if (len !== 0) {
        last = len;
        len = 0;
      }
    }
  }
  if (len !== 0) {
    last = len;
  }
  return last;
  // return words[words.length - 1].length;
};
// var lengthOfLastWord = function (s) {
//   const strs = s.split(" ");
//   const words = [];
//   for (let i = 0; i < strs.length; i++) {
//     const len = strs[i].length;
//     if (len > 0) {
//       words.push(strs[i]);
//     }
//   }

//   return words[words.length - 1].length;
// };

// console.log(lengthOfLastWord("   fly me   to   the moon  "));
console.log(lengthOfLastWord("ld   "));
