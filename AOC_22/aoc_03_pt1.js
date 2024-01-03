const fs = require('fs');
const readline = require('readline');
let ans = 0;
let code = 0;
const file = readline.createInterface({
  input : fs.createReadStream('input_03.txt'),
  output : process.stdout,
  terminal : false
});

file.on('line', (line) => {
  let index_1 = line.length /2;
  let comp1 = line.substring(0,index_1);
  let comp2 = line.substring(index_1);
  for (let i =0; i < index_1; i++){
    if (comp2.includes(comp1[i])){
      if (comp1[i] == comp1[i].toUpperCase()){
        let test = comp1[i].toLowerCase();
        code = test.charCodeAt(0);
        code = code % 96;
        code += 26;
        comp1 = comp1.replaceAll(test.toUpperCase(),'');
        comp2 = comp2.replaceAll(test.toUpperCase(),'');
      } else{
        let test = comp1[i];
        code = comp1[i].charCodeAt(0);
        code = code % 96;
        comp1 = comp1.replaceAll(test,'');
        comp2 = comp2.replaceAll(test,'');
        
      }
      ans += code;
      console.log(ans);
      
      
    }
  }
});



/*
if (test == test.toUpperCase()){
  test = test.toLowerCase() ;
  code = test.charCodeAt(0);
  code = code % 96;
  code += 26;
} else{
  code = test.charCodeAt(0);
  code = code % 96;
}
console.log(code);
*/
