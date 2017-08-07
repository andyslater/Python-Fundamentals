
class TreeNode():
    def __init__(self,data):
        self._lnode = None
        self._rnode = None
        self._data = data

    def get_data(self):
        return( self._data )

    def set_data(self):
        self._data = data

    def add_right(self, data = None):
        self._rnode = TreeNode(data)

    def add_left(self, data = None):
        self._lnode = TreeNode(data)


class Tree():
    def __init__(self, data=None):
        self._size = 0
        if data:
            self._root = TreeNode(data)
        else:
            self._root = None

    def insert(self, datalist):
        offset = 0
        if self._root == None or self._root.get_data() == None:
            self._root = TreeNode(datalist[0])
            offset = 1

        for data in datalist[offset:]:
            print("data", data)
            node = self._find_insert_node(self._root,data)
            if data >= node.get_data():
                node.add_right(data) 
            else:
                node.add_left(data) 


    def find_insert_node(self, data):
        return( self._find_insert_node(self._root, data))

    def _find_insert_node(self, node, data):
        #  return the node where the insertion should be made. Alsways insert left if available and the data is < node data, otherwise right

        # if this node has no data, then its an empty tree and return None
        if node.get_data() == None:
            return None

        # if we are larger then go right, or return this one if there is no right
        if data >= node.get_data():
            # go right or return this node if there is no right
            if node._rnode == None:
                return(node)
            return(self._find_insert_node(node._rnode, data))

        # otherwise go left, or return this one if not possible
        if node._lnode == None:
            return(node)
        return(self._find_insert_node(node._lnode, data))

    def print_sorted(self):
        self.print_sorted_recurse(self._root)
    
    def print_sorted_recurse(self, node):
        if node._lnode:
            self.print_sorted_recurse(node._lnode)
        print( node.get_data() )
        if node._rnode:
            self.print_sorted_recurse(node._rnode)

    def print(self):
       self.print_recurse(0, self._root)

    def print_recurse(self, level, node):
        if not node:
            return None

#        print(' '*3*level, "LEVEL: {}  DATA: {}  NODE: {}  LEFT: {}  RIGHT: {}".format(level, node.get_data(), node, node._lnode, node._rnode))
        print(' '*3*level, "LEVEL: {}  DATA: {}  ".format(level, node.get_data()))
        
        if node._lnode:
            self.print_recurse(level +1, node._lnode)
        
        if node._rnode:
            self.print_recurse(level +1, node._rnode)

            
tt = Tree()
#print( "insertion node: ", tt.find_insert_node(4) )
#tt.insert([100,50,200,10,5,6,9,7,15,14,20,9])
#tt.insert([100,50,150,25,75,125,175,110])
#tt.insert(range(0,20))

tt.insert([10,5,15,2,7] + [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,116,17,18,19])

tt.print()
'tt.print_sorted()

print(hash('asdf'))

