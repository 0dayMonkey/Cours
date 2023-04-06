""" Code sur piles et files par HM"""
import random
import operator


class Node:
    def __init__(self, v):
        self.v = v
        self.next = None


def test_parenthesage(char):
    """ with no stack"""
    n, i = 0, 0
    ln = len(char)
    while n >= 0 and i < ln:
        if char[i] == "(":
            n += 1
            i += 1
        elif char[i] == ")":
            n -= 1
            i += 1
        else:
            return False
    return n == 0


def test_parenthesage2(char):
    """ with pile"""
    print(1)
    stk = Stack()
    for i in char:
        print(i)
        if i == "(" or i == "[":
            stk.push(i)
        elif i == ")" or i == "]":  # or another if
            if stk.is_empty():
                print(20)
                return False
            j = stk.pop()
            if j + i != "[]" and j + i != "()":
                return False
        elif "a" <= i <= "z":
            pass
        else:
            return False
    return stk.is_empty()


def wait_double(n):
    lst = []
    while True:
        alea = random.randint(1, n)
        if alea in lst:
            lst.append(alea)
            return lst, lst.__len__()
        lst.append(alea)


def wait_double_set(n):
    lst = set()
    while True:
        alea = random.randint(1, n)
        if alea in lst:
            lst.add(alea)
            return lst.__len__()
        lst.add(alea)


def waiting_mean(n, nb):
    summ = 0
    for i in range(nb):
        summ += wait_double(n)
    return summ / nb


def waiting_mean_set(n, nb):
    summ = 0
    for i in range(nb):
        summ += wait_double(n)
    return summ / nb


operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def calcul(pile, op):
    pile.push(operators[op](pile.pop(), pile.pop()))


class EmptyStack(Exception):
    pass


class InvalidExpression(Exception):
    pass


def evaluation(lst):
    stk = Stack()
    try:
        for i in lst:
            if i == " ":
                pass
            elif i in operators.keys():
                try:
                    stk.push(operators[i](stk.pop(), stk.pop()))
                except EmptyStack:
                    raise InvalidExpression("Empty Stack 1")  # That will never happen
            else:
                try:
                    stk.push(float(i))
                except ValueError:
                    raise RuntimeError("expression non valide not flat")
        res = stk.pop()
        if stk.is_empty():
            return res
        else:
            raise RuntimeError("Expression non valide pile not empty at the end")
    except EmptyStack:
        raise InvalidExpression("empty stack 2")


def is_float(n):
    #  return type(n) is float or type(n) is int
    return isinstance(n, float) or isinstance(n, int)


class Stack:
    def __init__(self):
        self.head = None
        # self.last = None

    def is_empty(self):
        return self.head is None

    def push(self, v):
        v_node = Node(v)
        if self.head is None:
            self.head = v_node
        else:
            v_node.next = self.head
            self.head = v_node

    def pop(self):
        if self.head is None:
            raise RuntimeError(" pop ()  Empty stack")
        else:
            v = self.head.v
            self.head = self.head.next
            return v

    def display(self):
        sta = Stack()
        while self.head is not None:
            v = self.pop()
            print(v)
            sta.push(v)
        while sta.head is not None:
            self.push(sta.pop())

    def search(self, value):
        find = False
        sta = Stack()
        while not find and self.head is not None:
            v = self.head.v
            if v == value:
                find = True
            else:
                sta.push(self.pop())
        while sta.head is not None:
            self.push(sta.pop())
        return find

    def update(self, value, nv):
        qu = Stack()
        while not self.is_empty():
            v = self.pop()
            if v == value:
                qu.push(nv)
            else:
                qu.push(v)
        while not qu.is_empty():
            self.push(qu.pop())

    def inverse(self):
        sta = Stack()
        while not self.is_empty():
            sta.push(self.pop())
        self.head = sta.head

    def copy(self):
        sta, sta2 = Stack(), Stack()
        while not self.is_empty():
            sta.push(self.pop())
        while not sta.is_empty():
            v = sta.pop()
            sta2.push(v)
            self.push(v)
        return sta2

    def separate(self):
        """ pair and impair numbers"""
        sta, pair, impair = Stack(), Stack(), Stack()
        while not self.is_empty():
            sta.push(self.pop())
        while not sta.is_empty():
            v = sta.pop()
            if v % 2 == 0:
                pair.push(v)
            else:
                impair.push(v)
            self.push(v)
        return pair, impair

    def parenthesage(self, char):
        for i in char:
            if i == "(":
                self.push(3)
            elif i == ")":  # or another if
                self.pop()
            else:
                pass

    def empty(self):
        while not self.is_empty():
            self.pop()

    def test_parenthesage2(self, char):
        """ with ( and [ ..."""
        n, m, i = 0, 0, 0
        ln = len(char)
        while n >= 0 and i < ln and m >= 0:
            print(i, n, m)
            if char[i] == "(":
                n += 1
            elif char[i] == ")":
                n -= 1
            elif char[i] == "[":
                m += 1
            elif char[i] == "]":
                m -= 1
            i += 1
        self.empty()
        return n == m == 0


a = Stack()
a.push(1)
a.push(2)
"""a.push(3)
a.push(2)
a.push(3)
a.push(30)
a.push(21)
a.push(3)"""

""" Utilisation d'une liste Python """


class Stack2:
    def __init__(self):
        self.head = []

    def push(self, v):
        self.head.append(v)

    def pop(self):
        self.head.pop()


class Queue:
    """ with acces to first and last node
        we enqueue at the end and dequeue at the firt
    """

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, v):
        v_node = Node(v)
        if self.first is None:  # or self.is_empty()
            self.last = v_node
            self.first = v_node
        else:
            self.last.next = v_node
            self.last = v_node

    def is_empty(self):
        return self.last is None  # or self.first is None

    def dequeue(self):
        if self.is_empty():  # or self.fist is None or self.last  is None
            raise RuntimeError("Empty Queue")
        else:
            v = self.first.v
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return v

    def disp_try(self):
        var = self.first
        while var is not None:
            print(var.v)
            var = var.next

    def display(self):
        qu = Queue()
        while not self.is_empty():
            v = self.dequeue()
            print(v)
            qu.enqueue(v)
        while not qu.is_empty():
            self.enqueue(qu.dequeue())

    def search(self, value):
        """" We transfer all in another stack by searching """
        find = False
        queue = Queue()
        while not self.is_empty():
            v = self.dequeue()
            if v == value:
                find = True
            queue.enqueue(v)
        self.first = queue.first
        self.last = queue.last
        return find

    def update(self, value, nv):
        qu = Queue()
        while not self.is_empty():
            v = self.dequeue()
            if v == value:
                qu.enqueue(nv)
            else:
                qu.enqueue(v)
        self.first = qu.first
        self.last = qu.last


b = Queue()
b.enqueue(1)
b.enqueue(2)
b.enqueue(1)
b.enqueue(4)
b.enqueue(5)








c = Queue()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
