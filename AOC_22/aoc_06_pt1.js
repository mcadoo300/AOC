const fs = require('fs');

const readFileLines = filename => 
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n')

const hash = readFileLines('input_06.txt')[0];


let cont = true
let i =0;
while (cont){
  let new_sub = hash.substring(i,i+4);
  console.log(new_sub);
  let new_set = new Set(new_sub);
  if (new_set.size == 4){
    cont = false;
    console.log(i+4);
    console.log(new_set);
  }
  i++
}
