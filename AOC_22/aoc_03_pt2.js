const fs = require('fs');
let ans = 0;
let code = 0;

const readFileLines = filename =>
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n');

let arr = readFileLines('input_03.txt');

for (let i = 0 ; i < arr.length - 2; i+=3){
  let line1 = arr[i];
  let line2 = arr[i+1];
  let line3 = arr[i+2];
  let line_set = [line1,line2,line3];
  let index = 0;
  if (line2.length <= line1.length && line2.length <= line3.length){
    index = 1;
  } else if (line3.length <= line1.length && line3.length <= line2.length){
    index = 2;
  }
  //console.log(line_set);
  let iter = Math.min(line1.length,line2.length,line3.length);
  //console.log(iter);
  for (let j =0; j < iter; j ++){
    let test = line_set[index][j];
    //console.log(test);
    if (line_set[1].includes(test) && line_set[2].includes(test) && line_set[0].includes(test)){
      if (test == test.toUpperCase()){
        test = test.toLowerCase();
        code = test.charCodeAt(0);
        code = code % 96;
        code += 26;
        line_set[0] = line_set[0].replaceAll(test.toUpperCase(),'' );
        line_set[1] = line_set[1].replaceAll(test.toUpperCase(),'' );
        line_set[2] = line_set[2].replaceAll(test.toUpperCase(),'' );
      }else{
        code = test.charCodeAt(0);
        code = code % 96;
        line_set[0] = line_set[0].replaceAll(test,'' );
        line_set[1] = line_set[1].replaceAll(test,'' );
        line_set[2] = line_set[2].replaceAll(test,'' );
      }
      ans += code;
      console.log(ans);
    }
  } 

}
