from collections import Counter
from collections import deque


class Potion:
    def __init__(self, number):
        self.number = number
        self.recipe_dict = dict()
        self.recipe_size = 0
        self.total_a = 0
        self.total_b = 0
        self.include_set = set()

    def check(self, big_dict, queue):
        if self.recipe_size == 0:
            for i in self.include_set:
                big_dict[i].sum_up(self, queue)
            return True
        return False

    def sum_up(self, pot, queue):
        tmp = self.recipe_dict[pot.number]
        self.total_a += pot.total_a * tmp
        self.total_b += pot.total_b * tmp
        self.recipe_size -= 1
        if self.recipe_size == 0:
            queue.remove(self.number)
            queue.appendleft(self.number)

    def add_to_include_set(self, big_dict, queue):
        cur_a = self.recipe_dict.get(1, None)
        if cur_a is not None:
            self.total_a += cur_a
            self.recipe_size -= 1
        cur_b = self.recipe_dict.get(2, None)
        if cur_b is not None:
            self.total_b += cur_b
            self.recipe_size -= 1

        if self.recipe_size == 0:
            queue.remove(self.number)
            queue.appendleft(self.number)

        for i in self.recipe_dict.keys():
            if i != 1 and i != 2:
                big_dict[i].include_set.add(self.number)

    def print(self):
        print('------------------')
        print(self.number)
        print(self.recipe_dict)
        print(self.recipe_size)
        print(f"Total A {self.total_a}")
        print(f"Total B {self.total_b}")
        print(self.include_set)


def main():
    n = int(input())
    poitions_dict = dict()
    final_vect = [0 for i in range(n + 1)]
    queue = deque([i for i in range(3, n + 1, 1)])

    for i in range(3, n + 1, 1):
        poitions_dict[i] = Potion(i)
    for i in range(3, n + 1, 1):
        input_vect = [int(ts) for ts in input().split(' ')]
        poitions_dict[i].recipe_dict = Counter(input_vect[1:])
        poitions_dict[i].recipe_size = len(poitions_dict[i].recipe_dict)
        poitions_dict[i].add_to_include_set(poitions_dict, queue)

    flag = True
    while flag:
        cycle = True
        if len(poitions_dict) == 0:
            flag = False
            break

        for i in queue:
            if poitions_dict[i].check(poitions_dict, queue):
                final_vect[i] = (poitions_dict[i].total_a, poitions_dict[i].total_b)
                queue.remove(i)
                cycle = False
                break

        if cycle is True:
            for i in queue:
                final_vect[i] = (-1, -1)
            flag = False

    output_str = ''
    q = int(input())
    for i in range(q):
        input_vect = [int(ts) for ts in input().split(' ')]
        ind = input_vect[2]
        a_q = input_vect[0]
        b_q = input_vect[1]
        if final_vect[ind][0] == -1:
            output_str += '0'
        elif final_vect[ind][0] <= a_q and final_vect[ind][1] <= b_q:
            output_str += '1'
        else:
            output_str += '0'
    print(output_str)


if __name__ == '__main__':
    main()
