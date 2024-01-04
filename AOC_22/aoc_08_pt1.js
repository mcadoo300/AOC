const fs = require('fs');

const readFileLines = filename =>
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n')

const lines = readFileLines('input_08.txt')
if (lines[lines.length-1].length == 0 ){
  lines.pop();
}
const direcctions = [[0,1],[0,-1],[1,0],[-1,0]];

let visible = 0;

let min_row = 0;
let min_col = 0;
for (let row = 0; row < lines.length-1; row++){
  for(let col = 0; col < lines[row].length-1; col++){
    
  }
}
