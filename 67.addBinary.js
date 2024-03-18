/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  const length = Math.max(a.length, b.length) + 1;
  const A = a
    .split("")
    .reverse()
    .concat(Array(length - a.length).fill("0"));
  const B = b
    .split("")
    .reverse()
    .concat(Array(length - b.length).fill("0"));

  const res = Array(length).fill(0);

  for (let i = 0; i < length - 1; i++) {
    const { cout, s } = sum(parseInt(A[i]), parseInt(B[i]), res[i]);
    res[i] = s;
    res[i + 1] = cout;
  }

  const resum = res.reverse().join("");
  return resum[0] === "0" ? resum.substring(1) : resum;
};

function sum(a, b, cin) {
  return {
    cout: a * b + cin * (a ^ b),
    s: a ^ b ^ cin,
  };
}

console.log(addBinary("0", "0"));
