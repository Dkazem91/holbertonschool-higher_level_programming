#!/usr/bin/node
let nums = process.argv.slice(2).map(x => Number(x));
if (nums.length <= 1) {
  console.log(0);
} else {
  console.log(nums.sort().reverse()[1]);
}
