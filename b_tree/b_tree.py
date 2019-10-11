#!/usr/bin/env python3

################################################################################
#                                                                              #
#  B Tree                                                                      #
#                                                                              #
#  Instituto Federal de Minas Gerais - Campus Formiga, 2019                    #
#                                                                              #
#  Contact: Thales Otávio | @ThalesORP | ThalesORP@gmail.com                   #
#                                                                              #
#  Matrícula: 0016074                                                          #
#                                                                              #
################################################################################

''' Module docstring.'''

class BTree():
    ''' Main class of B Tree.'''

    def __init__(self):
        self.ordem = 2
        self.root = Node(self.ordem, None, True)

    def run(self):
        ''' Method docstring.'''

        #numbers_to_insert = [1, 3, 4, 7, 8, 15, 10, 12, 13, 14, 18, 20, 25, 29, 37,
        #                     45, 60, 30, 35, 40, 41, 42, 43, 51, 52, 70, 77, 83]

        #numbers_to_insert = [1, 7, 6, 2, 11, 4, 8, 5, 15, 3, 12]

        numbers_to_insert = [11, 36, 53, 95, 8]

        for num in numbers_to_insert:
            self.insert(num)
            input()

    def insert(self, key):
        ''' Method docstring.'''
        self.root = self.root.insert(key)
        self.show()

    def show(self):
        ''' Method docstring.'''
        print("\nFinally: ")
        print(self.root.__complete_str__())


class Node():
    ''' Class of each page used in B Tree.'''

    def __init__(self, order, keys=None, root=None):
        self.order = order

        self.root = root
        if self.root is None:
            self.root = False

        self.n_keys = self.order * 2
        self.n_pages = self.n_keys + 1

        self.keys = keys
        if self.keys is None:
            self.keys = [None] * self.n_keys

        self.pages = [None] * self.n_pages

    def insert(self, key):
        ''' Method docstring.'''

        print("\n\n--> Inserting " + str(key) + " on: " + str(self))


        # When there's no room to insert new key AND it's leaf.
        if (None not in self.keys) and (self.__has_pages_attached__() == False):
            key_to_promote, left_page, right_page = self.__split__(key)

            if self.root is False:
                # When this is not root, return the key that will be attached to the root and the pages within.
                return key_to_promote, left_page, right_page
            else:
                # When the current node is root, create new node that will turn into new root.
                # Tree growing up.
                new_node = Node(self.order, key_to_promote, True)
                new_node.insert_page("L", key_to_promote, left_page)
                new_node.insert_page("R", key_to_promote, right_page)
                self.root = False
                return new_node


        for i in range(self.n_keys):

            # When there's no one in that position, insert the key right there.
            if self.keys[i] is None:
                self.keys[i] = key
                # Return the current node because the key was inserted with success.
                return self

            # If the key is found, return the current node because he is already in.
            if self.keys[i] == key:
                return self

            if key < self.keys[i]:
                # If there's a page in LEFT side of currrent key, go to that page.
                page_index = self.__get_page_index__("L", self.keys[i])
                if self.pages[page_index] is not None:

                    page_insert_return = [self.pages[page_index].insert(key)]

                    if len(page_insert_return) == 3:
                        #return key_to_promote, left_page, right_page
                        new_key = page_insert_return[0]
                        left_page = page_insert_return[1]
                        right_page = page_insert_return[2]

                        self.insert(new_key)
                        self.insert_page("L", new_key, left_page)
                        self.insert_page("R", new_key, right_page)
                        return self
                    else:
                        # When there's only one value, it's the new root created.
                        return page_insert_return[0]
                
                # When there's no page to go.
                else:
                    self.__shift__("R", self.keys[i])
                    self.keys[i] = key
                    # Return the current node because the key was inserted with success.
                    return self

    def insert_page(self, side, key, page):
        '''Insert the "page" in the "side" of "key".
        If side is "L", "page" is inserted on left side of key.
        If side is "E", "page" is inserted on right side of key.'''

        # Getting the index of "key".
        key_index = self.keys.index(key)
        if side == "L":
            self.pages[key_index] = page
        if side == "R":
            self.pages[key_index + 1] = page

    def __shift__(self, side, key):
        ''' Shift to "side" the elements after "key", with "key" included.
        If side is "L", shift left is performed.
        If side is "R", then shift right.'''

        # Checking if there's no space to move.
        if None not in self.keys:
            return False

        # Removing the first occurence of None from keys list.
        self.keys.remove(None)

        if side == "L":
            # Now putting the None in the last position.
            self.keys.append(None)

        elif side == "R":
            key_index = self.keys.index(key)
            # Now putting the None in the correct position.
            self.keys = self.keys[:key_index] + [None] + self.keys[key_index:]

        return True

    def __split__(self, key):
        ''' Split the current leaf node in the key position and return new root created.'''

        print("Splitting the node:", self)

        self.keys.append(key)
        self.keys.sort()
        
        half_keys = len(self.keys)//2

        key_to_promote = self.keys.pop(half_keys)

        # Splitting the keys into two new list keys: right and left. E.g.:
        # keys=[1,2,3,4] -> left_keys=[1,2,None,None] and right_keys=[3,4,None,None]
        left_keys = self.keys[:half_keys] + ([None] * half_keys)
        right_keys = self.keys[half_keys:] + ([None] * half_keys)

        left_page = Node(self.order, left_keys)
        right_page = Node(self.order, right_keys)

        return key_to_promote, left_page, right_page

    def __get_page_index__(self, side, key):
        ''' Return the index of page in the "side" of the key.'''

        key_index = self.keys.index(key)

        if side == "L":
            if key_index == 0:
                return 0
            return key_index-1

        if side == "R":
            return key_index+1

        return None

    def __has_pages_attached__(self):
        for page in self.pages:
            if page is not None:
                return True
        return False

    def __str__(self):
        result = "["
        for i in range(len(self.keys)-1):
            result += str(self.keys[i]) + " "
        result += str(self.keys[i+1]) + "]"

        return result

    def __complete_str__(self):
        result = "Root: " + self.__str__()

        result += "\nPages: "
        for i in range(self.n_pages):
            result += str(i) + ":"
            if self.pages[i] is None:
                result += "[]  "
            else:
                result += str(self.pages[i]) + "  "

        return result
