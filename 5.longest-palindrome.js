/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  const review = (l, r) => {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      l--;
      r++;
    }
    return s.substring(l + 1, r);
  };

  let longest = "";
  for (let i = 0; i < s.length; i++) {
    sub1 = review(i, i);
    if (sub1.length > longest.length) longest = sub1;
    sub2 = review(i, i + 1);
    if (sub2.length > longest.length) longest = sub2;
  }
  return longest;
};

console.log(longestPalindrome("babad"));
console.log(longestPalindrome("abcdcba"));
console.log(longestPalindrome("abccba"));
