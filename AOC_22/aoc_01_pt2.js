const fs = require('fs');
const readline = require('readline');


const file = readline.createInterface({
  input : fs.createReadStream('input_01.txt'),
  output : process.stdout,
  terminal: false
});

let current_sum = 0;
let top_set = []
file.on('line', (line) => {
  line = line.trim();
  if (line.length === 0){
    top_set.push(current_sum);
    top_set = top_set.sort(function (a, b) {return a-b;}); 
    while (top_set.length > 3){
      top_set.shift();
    }
    current_sum = 0;
    let top_sum = 0
    for (let index = 0; index < top_set.length; index++) {
      top_sum += top_set[index]
    }
    console.log(top_sum);
  } else {
    str_val = line.trim();
    current_sum += parseInt(str_val);
  }
});
