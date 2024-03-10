var letterCombinations = function (digits) {
  const combinatios = [];
  if (digits == "") return combinatios;
  let index = 0;
  let output = "";

  const mapping = [
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
  ];
  solve(digits, combinatios, index, output, mapping);
  return combinatios;
};
function solve(digits, ans, index, output, mapping) {
  if (index >= digits.length) {
    ans.push(output);
    return;
  }

  let number = parseInt(digits[index]);
  let temp = mapping[number];

  for (let i = 0; i < temp.length; i++) {
    output = output.concat(temp[i]);
    solve(digits, ans, index + 1, output, mapping);
    output = output.slice(0, -1);
  }
}

console.log(letterCombinations("23"));
