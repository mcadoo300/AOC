file = open('input_07.txt','r')
lines = file.readlines()



directories = {}
parents = {}

current_directory = "/"
i = 0
while i < len(lines):
    line = lines[i].strip().split(' ')
    print(line)
    # if command
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                for key, value in parents.items():
                    if value is not None and current_directory in value:
                        current_directory = key
                        break
            else:
                next_directory = line[2]
                if current_directory in parents.keys():
                    old_list = parents.get(current_directory)
                    old_list.append(next_directory)
                    old_list = list(set(old_list))
                    parents.update({current_directory : old_list})
                else:
                    parents.update({current_directory : [next_directory]})

                current_directory = next_directory

            i += 1
        else:
            i+=1
            while i < len(lines) and lines[i][0] != "$":
                line = lines[i].strip().split(' ')
                if line[0] == "dir":
                    if current_directory in parents.keys():
                        old_list = parents.get(current_directory)
                        old_list.append(line[1])
                        old_list = list(set(old_list))
                        parents.update({current_directory : old_list})
                    else:
                        parents.update({current_directory : [line[1]]})
                else:
                    if current_directory in directories.keys():
                        old_val = directories.get(current_directory)
                        old_val += int(line[0])
                        directories.update({current_directory: old_val})
                    else:
                        directories.update({current_directory: int(line[0])})
                i += 1






def dirSize(dir,direct,rents):
    size = 0
    if dir in directories.keys():
        size += directories.get(dir)
    if dir in rents.keys():
        children = rents.get(dir)
        for child in children:
            if child != dir:
                size += dirSize(child,direct,rents)
    return size
print(directories)
print(parents)
ans = 0
for key, value in directories.items():
    sz = dirSize(key,directories,parents)
    if sz <= 100000:
        ans +=sz
print(ans)
