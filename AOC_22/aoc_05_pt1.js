const fs = require('fs');


function isNumber(some_string){
  return !isNaN(parseFloat(some_string)) && isFinite(some_string);
}


function ProcessLine(line){
  line = line.split(' ');
  const return_values = [];
  for (let segment of line){
    if (isNumber(segment)){
      return_values.push(parseInt(segment));
      
    }
  }
  return return_values;
}

const readFileLines = filename => 
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n')

const arr = readFileLines('input_05.txt');

const buckets = [[]];

let calc_moves = false;

let bucket = 0;
for (let line of arr){
  if (line.length === 0){
    calc_moves = true;
  }
  else{
    if (calc_moves){
      let direct = ProcessLine(line);
      console.log(direct);
      console.log(buckets);
      for (let i = 0;i < direct[0];i++){
        let rmved = buckets[direct[1]-1].shift();
        buckets[direct[2]-1].unshift(rmved);
      }
      console.log(buckets);
    } else{
      bucket = 0;
      for ( let i = 0; i < line.length; i ++){
        if (((i+1) % 4) === 0){
          bucket+=1;
          if ((bucket+1) > buckets.length){
            buckets.push([]);
          }

        }
        if (line[i] === "["){
          buckets[bucket].push(line[i+1]);
        }
      }
    }

  }
}

let ans = ""
for (let i=0; i < buckets.length;i++){
  ans+=buckets[i][0];
}
console.log(ans);
