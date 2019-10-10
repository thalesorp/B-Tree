#!/usr/bin/env python3

################################################################################
#                                                                              #
#  B Tree:                                                                     #
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
    ''' Main class of this project.'''

    def __init__(self):
        self.ordem = 2
        self.root = Node(self.ordem)

    def run(self):
        ''' Method docstring.'''
        numbers_to_insert = [1, 3, 4, 7, 8, 15, 10, 12, 13, 14, 18, 20, 25, 29, 37,
                             45, 60, 30, 35, 40, 41, 42, 43, 51, 52, 70, 77, 83]
        for num in numbers_to_insert:
            self.insert(num)

    def insert(self, key):
        ''' Method docstring.'''
        self.root = self.root.insert(key)
        self.show()

    def show(self):
        ''' Method docstring.'''
        print(self.root.__complete_str__())


class Node():
    ''' Node or page object.'''

    def __init__(self, order, keys=None):
        self.order = order

        self.n_keys = self.order * 2
        self.n_pages = self.n_keys + 1

        self.keys = keys
        self.pages = list()

        if self.keys is None:
            self.keys = list()
            for _ in range(self.n_keys):
                self.keys.append(None)

        for _ in range(self.n_pages):
            self.pages.append(None)

    def search(self, key):
        ''' This method search for the "key" argument in the current node.
        If finds it, true is returned. Otherwise, it's returned false.'''

        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return True
        return False

    def insert(self, key):
        ''' This method insert the "key" argument in the current node.
        If new root is created, the new root is returned.
        Otherwie, the current node is returned.'''

        print("\n\n--> Inserting " + str(key) + " on: " + str(self))

        for i in range(self.n_keys):
            current_key = self.keys[i]

            if current_key is not None:

                # If the key is found, return the current node because he is already in.
                if key == current_key:
                    return self

                if key < current_key:
                    # If there's a page in LEFT side of currrent key, go to that page.
                    page_index = self.__get_page_index__("L", current_key)
                    if self.pages[page_index] is not None:
                        return self.pages[page_index].insert(key)

                    # Trying to perform a shift left.
                    if self.__shift__("R", current_key):
                        self.keys[i] = key
                        # Return the current node because the key was inserted with success.
                        return self
                    # When there's no space to shift right.
                    new_root = self.__split_current_node__(key)
                    # Return a new node because the key was inserted with success.
                    return new_root

                # Otherwise, there's a page in RIGHT side of currrent key, go to that page.
                page_index = self.__get_page_index__("R", current_key)
                if self.pages[page_index] is not None:
                    return self.pages[page_index].insert(key)

                # Checking if the current page is full.
                if None not in self.keys:
                    # When there's no space to shift right.
                    new_root = self.__split_current_node__(key)
                    # Return a new node because the key was inserted with success.
                    return new_root

            else:
                self.keys[i] = key
                # Return the current node because the key was inserted with success.
                return self

        return None

    def insert_page(self, side, key, page):
        '''Insert the "page" in the "side" of "key".'''

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

    def __split_current_node__(self, key):
        ''' Split the current node in the key position and return new root created.'''

        print("Splitting the current node...")

        half_keys = self.order

        # Finding which side the key should be inserted.
        #i = 0
        #while not key < self.keys[i]:
        #   i += 1
        for i in range(len(self.keys)):
            if key > self.keys[i]:
                i += 1

        # Getting the last "half_keys", putting in new keys list and completing with None.
        new_node_keys = self.keys[-half_keys:] + ([None] * half_keys)

        # Replacing the "half_keys" keys with None in the current node keys list.
        self.keys = self.keys[:-half_keys] + ([None] * half_keys)

        print(self.keys, new_node_keys)

        new_node = Node(self.order, new_node_keys)

        # Inserting the key in the correct node.
        if i < half_keys:
            self.insert(key)
            # Promote the key with HIGHEST value.
            # Getting the key to promote, and placing None where it is.
            index_key_promote = self.keys.index(None)-1
            key_to_promote = self.keys[index_key_promote]
            self.keys[index_key_promote] = None
        else:
            new_node.insert(key)
            # Promote the key with LOWEST value.
            # Getting the key to promote, and placing None where it is.
            index_key_promote = 0
            key_to_promote = new_node.keys[index_key_promote]
            new_node.keys[index_key_promote] = None
            new_node.__shift__("L", new_node.keys[index_key_promote + 1])

        new_root = Node(self.order)
        new_root.insert(key_to_promote)

        # Updating the pointers to pages of new root.
        new_root.insert_page("L", key_to_promote, self)
        new_root.insert_page("R", key_to_promote, new_node)

        return new_root

    def __get_page_index__(self, side, key):
        ''' Return the index of page in the "side" of the key.'''

        key_index = self.keys.index(key)

        if side == "L":
            if key_index == 0:
                return 0
            return key_index-1

        if side == "R":
            if key_index == self.n_keys:
                return self.n_keys
            return key_index+1

        return None

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
