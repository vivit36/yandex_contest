class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.number = None


class Tree:
    def __init__(self):
        self.root = Node()
        self.root.number = 1
        self.size = 1
        self.nodes_dict = dict()
        self.nodes_dict[self.root.number] = self.root

    def find(self, number):
        return self.nodes_dict[number]

    def add_node(self):
        self.size += 1
        if self.size % 2 == 0:
            parent_number = self.size // 2
        else:
            parent_number = (self.size - 1) // 2

        to_node = self.find(parent_number)
        new_node = Node()
        new_node.number = self.size
        new_node.parent = to_node
        if self.size % 2 == 0:
            to_node.left = new_node
        else:
            to_node.right = new_node

        self.nodes_dict[new_node.number] = new_node

    def create_tree(self, number):
        for i in range(number - 1):
            self.add_node()

    def print_tree_lvr(self, cur_node):
        if cur_node.left is not None:
            self.print_tree_lvr(cur_node.left)
        print(cur_node.number, end=' ')
        if cur_node.right is not None:
            self.print_tree_lvr(cur_node.right)

    def swap_with_parent(self, number):
        v = self.find(number)
        if v.parent is not None:
            p = v.parent
            tmp_pp = p.parent
            if tmp_pp is not None:
                if tmp_pp.left == p:
                    tmp_pp.left = v
                else:
                    tmp_pp.right = v
            v.parent = tmp_pp
            if p == self.root:
                self.root = v
            if p.left == v:
                p.left = v.left
                if v.left is not None:
                    v.left.parent = p
                v.left = p
                p.parent = v
            else:
                p.right = v.right
                if v.right is not None:
                    v.right.parent = p
                v.right = p
                p.parent = v


def main():
    my_tree = Tree()
    s = input().split(' ')
    n = int(s[0])
    s = input()
    vect = [int(x) for x in s.split(' ')]
    my_tree.create_tree(n)

    for i in vect:
        my_tree.swap_with_parent(i)
    my_tree.print_tree_lvr(my_tree.root)


if __name__ == '__main__':
    main()
