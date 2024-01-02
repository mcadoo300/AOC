const fs = require('fs')

const readFileLines = filename =>
fs 
  .readFileSync(filename)
  .toString('UTF8')
  .split('\n')

const lines = readFileLines('input_07.txt');
lines.pop();
let current_directory = "/";
let i = 0;

const directories = {"/":0};
const parent_directories = {"/":[]};
while( i < lines.length) {
  let new_line = lines[i];
  if (new_line[0] == "$"){
    new_line = new_line.split(' ');
    if (new_line[1] == "cd"){
      current_directory = new_line[2];
      i++;
    } else{
      i++;
      new_line = lines[i];
      while (i < lines.length && new_line[0] != "$"){
        new_line = new_line.split(' ');
        if (new_line[0] == "dir"){
          if (parent_directories.hasOwnProperty(current_directory)){
            let old_list = parent_directories[current_directory];
            old_list.push(new_line[1]);
            parent_directories[current_directory] = old_list;
          } else{
            parent_directories[current_directory] = [new_line[1]];
          }
        } else {
          let new_val = parseInt(new_line[0]);
          if (directories.hasOwnProperty(current_directory)){
            let old_val = directories[current_directory];
            old_val+=new_val;
            directories[current_directory] = old_val;
          } else{
            directories[current_directory] = new_val;
          }
        }
        i++;
        new_line = lines[i];
      }
    }
  }
}

function getDirectorySize(dir,base_dir, parents){
  let sz = base_dir[dir];

  if (parents.hasOwnProperty(dir)){
    let child_dirs = parents[dir];
    for (let new_dir of child_dirs){
      sz += getDirectorySize(new_dir,base_dir,parents);
    }
  }
  return sz
}


let ans = 0;
let cur_total = 0;
console.log(parent_directories)
for ( let key in directories){
  let val = (getDirectorySize(key,directories,parent_directories));
  if (val <=100000){
    ans += val;
  }
}
console.log(ans);
