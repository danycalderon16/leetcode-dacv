class Solution {
  maxArea(height) {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;

    while (left < right) {
      const area = Math.min(height[left], height[right]) * (right - left);

      maxArea = Math.max(maxArea, area);

      if (height[left] < height[right]) {
        left++;
      } else {
        right--;
      }
    }

    return maxArea;
  }
}

// Ejemplo de prueba
const solution = new Solution();
const heights = [1, 8, 6, 2, 5, 4, 8, 3, 7];
const maxArea = solution.maxArea(heights);
console.log("Max area:", maxArea);
