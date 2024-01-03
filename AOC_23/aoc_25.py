input_file = open('input_25.txt', 'r')
lines = input_file.readlines()


class Node():
    def __init__(self, parent = None, child = None, label = ""):
        self.parent = parent
        self.child = child
        self.label = label
   
    def Set_parent(self,new_parent):
        self.parent = new_parent

    def Get_parent(self):
        return self.parent

    def Set_child(self, new_child):
        self.child = new_child

    def Get_child(self):
        return self.child

    def Set_label(self, new_label):
        self.label = new_label

    def Get_label(self):
        return self.label



# label : index of list
connection_dict = {}
wire_connections = []


for line in lines:
    line = line.strip()
    line = line.split(":")
    base = line[0].strip()
    connected_labels = [segment.strip() for segment in line[1].strip().split(' ')]
    if base in connection_dict.getkeys():

    else:q
        index_of_list = len(wire_connections)
        connection_dict.update({base:index_of_list})
        new_parent = Node(parent=None,child=None,label=base)
        wire_connections.append(new_parent)

