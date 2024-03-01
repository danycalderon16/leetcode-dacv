/**
 * @param {string[]} strs
 * @return {string}
 */
function longestCommonPrefix(strs) {
  console.log(strs.sort());
  console.log(strs);

  let prefix = "";
  const fisrt = strs[0].split("");
  const last = strs[strs.length - 1].split("");

  for (let i = 0; i < fisrt.length; i++) {
    if (fisrt[i] === undefined || last[i] === undefined) return prefix;

    if (fisrt[i] === last[i]) prefix += fisrt[i];
    else return prefix;
  }
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
// console.log(longestCommonPrefix(["dog","racecar","car"]));
