const fs = require('fs');
let ans = 0;

const readFileLines = filename =>
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n');

const arr = readFileLines('input_04.txt');

console.log(arr);
for (let i = 0; i < arr.length; i++){
  arr[i] = arr[i].trim();
  if (arr[i].length == 0){
    arr.splice(i,1);
    console.log(arr);
  }
}


for (let i=0; i < arr.length ; i++){
  let line1 = arr[i].split(",")[0];
  let line2 = arr[i].split(",")[1];
  lower1 = line1.split("-")[0];
  lower2 = line2.split("-")[0];
  upper1 = line1.split("-")[1];
  upper2 = line2.split("-")[1];
  lower1 = parseInt(lower1);
  lower2 = parseInt(lower2);
  upper1 = parseInt(upper1);
  upper2 = parseInt(upper2);
  console.log(lower1 + " " + lower2);
  console.log(upper1 + " " + upper2);
  if (lower1 <= lower2 && upper1 >= upper2){
    ans+=1;

  }else if (lower2 <= lower1 && upper2 >= upper1){
    ans+=1;
  }
  console.log(ans);
}
