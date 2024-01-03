const fs = require('fs');
const readline = require('readline');


const file = readline.createInterface({
  input : fs.createReadStream('input_01.txt'),
  output : process.stdout,
  terminal: false
});

let max_sum = 0;
let current_sum = 0;

file.on('line', (line) => {
  line = line.trim();
  if (line.length === 0){
    max_sum = max_sum > current_sum ? max_sum : current_sum;
    current_sum = 0;
    console.log(max_sum);
  } else {
    str_val = line.trim();
    current_sum += parseInt(str_val);
  }
});
