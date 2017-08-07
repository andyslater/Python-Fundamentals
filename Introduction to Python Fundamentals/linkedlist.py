#
#
#

class Node(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next_node = node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, root = None ):
        self.size = 0
        self.root = root
        self.last_node = root

    def get_size(self):
        return self.size

    def add_node(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self.last_node = new_node
        else:
            self.last_node.set_next(new_node)
            self.last_node = new_node
        self.size += 1


    def find_node(self, data):
        prev_node = None
        this_node = self.root

        while this_node:
            if data == this_node.get_data():
                return prev_node, this_node
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return prev_node, this_node


    def remove_node(self, data):
        prev_node, found_node = self.find_node(data)

        if found_node == None:
            return False

        if prev_node == None:
            self.root = found_node
        else:
            prev_node.set_next( found_node.get_next() )
        self.size -= 1
        return True


    def print_list(self):
        this_node = self.root
        print("size: {}  root: {}".format(self.get_size(), self.root))
        i = 1
        while this_node:
            print("pos: {}  node: {}  data: {}  next: {}".format(i, this_node, this_node.get_data(), this_node.get_next()))
            this_node = this_node.get_next()
            i += 1

ll = LinkedList()
ll.print_list()
ll.add_node(55)
ll.add_node(56)
ll.add_node(57)
ll.add_node(58)
ll.print_list()

ll.find_node(57)
ll.remove_node(57)
ll.print_list()



