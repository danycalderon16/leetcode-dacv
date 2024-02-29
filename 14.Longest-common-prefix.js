/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length === 0) return "";
  if (strs.length === 1) return "";

  const first = strs[0].split("");
  const second = strs[1].split("");
  let prefix = getPrefix(first, second);

  if(strs.length === 2) return prefix;

  for (let i = 2; i < strs.length; i++) {
    if(prefix === "") return []
    if(strs[i].includes(prefix))
  }
  return prefix;
};

const getPrefix = (first, second) => {
  let prefix = "";
  for (let i = 0; i < first.length; i++) {
    if (first[i] === second[i] && second[i] !== undefined) {
      prefix = prefix + first[i];
    } else {
      break;
    }
  }

  return prefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
// console.log(longestCommonPrefix(["dog","racecar","car"]));
