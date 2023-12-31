const fs = require('fs');
const readline = require('readline');



function gameOutcome(m1, m2){
  let score = 0;
  if (m1 === "A"){
    if (m2 === "X"){
      score = 3;
    } else if (m2 === "Y"){
      score = 6;
    }
  } else if (m1 === "B"){
    if (m2 === "Y"){
      score = 3;
    } else if (m2 === "Z"){
      score = 6;
    }
  } else{
    if (m2 === "Z"){
      score = 3;
    } else if (m2 === "X"){
      score = 6;
    }
  }
  return score;
}



const file = readline.createInterface({
  input : fs.createReadStream('input_02.txt'),
  output : process.stdout,
  terminal : false
});



const throw_to_score = {"X" : 1, "Y" : 2 , "Z" : 3};

let ans = 0;


file.on('line', (line) => {
  let split_string = line.split(' ');
  ans += throw_to_score[split_string[1]];
  ans += gameOutcome(split_string[0],split_string[1]);
  console.log(ans);
});

