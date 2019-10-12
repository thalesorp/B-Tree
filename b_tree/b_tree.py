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

    def __init__(self, order):
        self.order = order
        self.root = Node(self.order, None, True)

    def run(self):
        ''' Method docstring.'''

        numbers = [33, 50, 50, 29, 26, 12, 44, 70, 56, 90, 60, 92, 87, 75, 89, 55, 43, 15, 26, 57, 8, 100, 96, 39, 13, 21, 45, 41, 84, 35]
        for number in numbers:
            print("Inserting", number)
            self.insert(number)
            self.show()

    def insert(self, key):
        ''' Insert the "key" value in current B Tree.'''

        keys = [None] * (self.order * 2)
        keys[0] = key
        page = Node(self.order, keys)

        self.root = self.root.insert(page)

    def show(self):
        ''' Show the current B Tree.'''

        print(self.root._complete_str())


class Node():
    ''' Class of each page used in B Tree.'''

    def __init__(self, order, keys=None, root=None):
        self.order = order

        self.n_keys = self.order * 2
        self.n_pages = self.n_keys + 1

        self.keys = keys
        if self.keys is None:
            self.keys = [None] * self.n_keys

        self.root = root
        if self.root is None:
            self.root = False

        self.pages = [None] * self.n_pages

    def insert(self, page):
        ''' Insert the "page" in the the page according to the B Tree rules.'''

        key = page.keys[0]

        # If the key is already in, do nothing.
        if key in self.keys:
            return self

        # When there's no room to insert new key and it's leaf.
        if None not in self.keys and self._is_leaf():
            # Spliting the current page.
            # When the current node is root, the tree is growing upwards.
            return self._split(key)

        for i in range(self.n_keys):

            if self.keys[i] is None:
                # If there's a left page, go there.
                page_index = self._get_page_index("L", i)
                if self.pages[page_index] is not None:
                    new_page = self.pages[page_index].insert(page)

                    # When split happens, attach the key and pages into current page.
                    if new_page._is_leaf() is False:
                        # What we have is a root page, with one key and two pages attached.
                        # TODO: AND WHEN THERE'S NO ROOM TO SHIFT? MAYBE CHECK IF SHIFT IS NEEDED?
                        self._shift("R", self.keys[i])
                        # Insert the new_page (which is root) into the new allocated position.
                        new_key = new_page.keys[0]
                        left_page = new_page.pages[0]
                        right_page = new_page.pages[1]
                        self.keys[i] = new_key
                        self._insert_page("L", new_key, left_page)
                        self._insert_page("R", new_key, right_page)
                else:
                    # In case there's no pages to go, here's the place to put the key.
                    self.keys[i] = key

                # Return the current node because the key was inserted with success.
                return self


            if key < self.keys[i]:
                # When what i'm trying to insert is root, it means that shift right is needad
                # and the pages of that root will be attached to current page.
                #if page.root is True:

                # When it's leaf but there's a element in the position. Shift right is needed.
                if self._is_leaf():
                    # TODO: AND WHEN THERE'S NO ROOM TO SHIFT?
                    self._shift("R", self.keys[i])
                    self.keys[i] = key
                    # Return the current node because the key was inserted with success.
                    return self

                # When it's not leaf, there's a page in LEFT side of currrent key.
                # Go to that page.
                page_index = self._get_page_index("L", i)
                new_page = self.pages[page_index].insert(page)

                # When split happens, attach the key and pages into current page.
                if new_page._is_leaf() is False:
                    # What we have in new_page is a root page, with one key and two pages attached.
                    # TODO: AND WHEN THERE'S NO ROOM TO SHIFT?
                    self._shift("R", self.keys[i])
                    # Insert the new_page (which is root) into the new allocated position.
                    new_key = new_page.keys[0]
                    left_page = new_page.pages[0]
                    right_page = new_page.pages[1]
                    self.keys[i] = new_key
                    self._insert_page("L", new_key, left_page)
                    self._insert_page("R", new_key, right_page)

                return self

        # When it didin't find space to insert, it means that key will be inserted into last page.

        print("------------------------------DANGEROUS ZONE!------------------------------")

        # We know that isn't leaf. Going to the page in RIGHT side.
        page_index = self._get_page_index("R", i)
        new_page = self.pages[page_index].insert(page)

        # When split happens, attach the key and pages into current page.
        if new_page._is_leaf() is False:
            # What we have is a root page, with one key and two pages attached.
            # TODO: AND WHEN THERE'S NO ROOM TO SHIFT?
            self._shift("R", self.keys[i])
            # Insert the new_page (which is root) into the new allocated position.
            new_key = new_page.keys[0]
            left_page = new_page.pages[0]
            right_page = new_page.pages[1]
            self.keys[i] = new_key
            self._insert_page("L", new_key, left_page)
            self._insert_page("R", new_key, right_page)

        return self

    def _insert_page(self, side, key, page):
        '''Insert the "page" in the "side" of "key".
        If side is "L", "page" is inserted on left side of key.
        If side is "E", "page" is inserted on right side of key.'''

        # Getting the index of "key".
        key_index = self.keys.index(key)
        if side == "L":
            self.pages[key_index] = page
        if side == "R":
            self.pages[key_index + 1] = page

    def _shift(self, side, key):
        ''' Shift to "side" the elements after "key", with "key" included.
        If side is "L", shift left is performed.
        If side is "R", then shift right.'''

        # Checking if there's space to move.
        if None not in self.keys:
            return False

        if self._is_leaf():
            # Removing the first occurence of None from keys list.
            self.keys.remove(None)

            # TODO: NEVER ENTERING HERE.
            if side == "L":
                # Now putting the None in the last position.
                self.keys.append(None)

            elif side == "R":
                # Now putting the None in the correct position.
                key_index = self.keys.index(key)
                self.keys = self.keys[:key_index] + [None] + self.keys[key_index:]

        else: # Shifting the pages attached to the non leaf page too.

            # Removing the first occurence of None on pages list.
            self.keys.remove(None)
            self.pages.remove(None)

            # TODO: NEVER ENTERING HERE.
            if side == "L":
                self.keys.append(None)
                self.pages.append(None)

            elif side == "R":
                key_index = self.keys.index(key)

                # Now putting the None in the correct position.
                self.keys = self.keys[:key_index] + [None] + self.keys[key_index:]

                # Silicing the pages list, removing the old page and putting Nones inside.
                self.pages = self.pages[:key_index] + [None, None] + self.pages[key_index+1:]

        return True

    def _split(self, key):
        ''' Split the current leaf node in the key position and return new root created.'''

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

        keys = [None] * self.n_keys
        keys[0] = key_to_promote
        new_root = Node(self.order, keys, True)

        new_root._insert_page("L", key_to_promote, left_page)
        new_root._insert_page("R", key_to_promote, right_page)

        return new_root

    def _is_leaf(self):
        ''' Return True if the current page is leaf. If isn't, return False.'''

        for page in self.pages:
            if page is not None:
                return False
        return True

    @staticmethod
    def _get_page_index(side, key_index):
        ''' Return the index of page in the "side" of the key in "key_index"
        position of keys list.'''

        if side == "R":
            return key_index+1

        if side == "L":
            return key_index

        return None

    def __str__(self):

        result = "["
        for i in range(len(self.keys)-1):
            result += str(self.keys[i]) + " "
        result += str(self.keys[i+1]) + "]"

        return result

    def _complete_str(self, level=0):

        if level == 0:
            result = "Root: "
        else:
            result = "\t" * level

        result += self.__str__() + "\n"

        for i in range(self.n_pages):
            if self.pages[i] is not None:
                result += str(i) + ":" + self.pages[i]._complete_str(level + 1)

        return result
