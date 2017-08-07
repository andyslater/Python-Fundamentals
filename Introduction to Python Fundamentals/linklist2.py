class Node(object):
    def __init__(self, data, next_node = None):
        self._data = data
        self._next_node = next_node

    def get_next(self):
        return( self._next_node )

    def set_next(self, next_node):
        self._next_node = next_node

    def get_data(self):
        return( self._data )

    def set_data(self, data):
        self._data = data


class LinkedList(object):
    # print
    # append
    # remove

    def __init__(self, data):
        self._head = None
        self._tail = None
        self._size = 0

        if data:
            self.append(data)

    def print(self):
        this_node = self._head
        print("size: {}  head: {}  tail: {} ".format(self._size, self._head, self._tail))
        i = 1
        while this_node:
            print("pos: {}  node: {}  data: {}  next: {}".format(i, this_node, this_node.get_data(), this_node.get_next()))
            this_node = this_node.get_next()

    def append(self, data):
        new_node = Node(data)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.set_next(new_node)
        self._tail = new_node
        self._size += 1

    def remove(self, data):
        prev_node, found_node = self.tfind(data)
        print("fn=", found_node)
        if not found_node:
            return False

        if prev_node:
            prev_node.set_next( found_node.get_next() )
        else:
            self._head = found_node.get_next()

        self._size -= 1
        return True


    def tfind(self, data):
        prev_node = None
        this_node = self._head

        while this_node:
            if this_node.get_data() == data:
                return prev_node, this_node
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return None, None


            
ll = LinkedList(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(8)
ll.print()

        
ll.remove(3)

ll.remove(8)
ll.remove(5)
ll.print()


    



