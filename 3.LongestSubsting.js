/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let length = 0;
  let l = 0;
  const seen = {};
  for (let r = 0; r < s.length; r++) {
    char = s[r];
    if (seen[char] !== undefined && seen[char] >= l) {
      l = seen[char] + 1;
    } else {
      length = Math.max(length, r - l + 1);
    }
    seen[char] = r;
  }
  return length;
};
// var lengthOfLongestSubstring = function (s) {
//   const letters = s.split("");
//   let index = 0;
//   let output = s[index];
//   let largest = output;
//   for (let i = 1; i < letters.length; i++) {
//     // if (i + 1 === letters.length) break;
//     if (output.includes(letters[i])) {
//       index++;
//       i = index;
//       output = letters[i];
//     } else output += letters[i];
//     if (output.length >= largest.length) {
//       largest = output;
//     }
//     console.log({ output, largest });
//   }
//   return largest.length;
// };

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));

/*
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
*/
