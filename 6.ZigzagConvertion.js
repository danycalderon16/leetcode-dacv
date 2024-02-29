/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1 || numRows >= s.length) return s;

  const rows = [];
  for (let i = 0; i < numRows; i++) {
    rows.push([]);
  }

  let index = 0;
  let step = 0;
  for (let i = 0; i < s.length; i++) {
    rows[index].push(s[i]);
    if (index === 0) step = 1;
    else if (index === numRows - 1) step = -1;
    index += step;
  }

  const flatRow = rows.flatMap((m) => m);
  return flatRow.join("");
};

console.log(convert("PAYPALSHARING", 3));
