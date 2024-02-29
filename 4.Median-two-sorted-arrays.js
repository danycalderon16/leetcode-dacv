/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let p1 = 0;
  let p2 = 0;
  const merged = [];
  while (true) {
    if (typeof nums1[p1] === "undefined" && typeof nums2[p2] === "undefined")
      break;
    if (typeof nums1[p1] !== "undefined" && typeof nums2[p2] !== "undefined") {
      if (nums1[p1] <= nums2[p2]) {
        merged.push(nums1[p1]);
        p1++;
      } else {
        merged.push(nums2[p2]);
        p2++;
      }
    }
    if (typeof nums1[p1] !== "undefined" && nums2[p2] === undefined) {
      merged.push(nums1[p1]);
      p1++;
    }
    if (typeof nums2[p2] !== "undefined" && nums1[p1] === undefined) {
      merged.push(nums2[p2]);
      p2++;
    }
  }
  const len = merged.length;
  if (len === 1) return merged[0];
  for (let index = 0; index < 10; index++) {
    const mid = Math.ceil(index / 2);
    if (index % 2 === 0) console.log(index, index % 2, "par");
    else console.log(index, index % 2, "impar");
  }
  // const mid = Math.ceil(len / 2);
  // if ((len / 2) % 2 === 0 || len === 2) {
  //   return (merged[mid] + merged[mid - 1]) / 2;
  // }
  // return merged[mid - 1];
  return 0;
};

function addNums1() {}

console.log(findMedianSortedArrays([], [1, 2, 3, 4, 5, 6]));
