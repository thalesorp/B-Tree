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
        self.root = Page(self.order, None, None, True)

    def run(self):
        ''' Method used to test.'''

        numbers = [33, 50, 50, 29, 26, 12, 44, 70, 56, 90, 60, 92, 87, 75, 89, 55, 43, 15, 26, 57, 8, 100, 96, 39, 13, 21, 101]#, 45, 41, 84, 35]
        for number in numbers:
            print("Inserting", number)
            self.insert(number)
            self.show()

    def insert(self, key):
        ''' Insert the "key" value in current B Tree.'''

        keys = [key] + ([None] * ((self.order * 2)-1))
        page = Page(self.order, keys)

        self.root = self.root.insert(page)

    def show(self):
        ''' Show the current B Tree.'''

        print(self.root._complete_str())


class Page():
    ''' Class of each page used in B Tree.'''

    LEFT = "L"
    RIGHT = "R"

    def __init__(self, order, keys=None, pages=None, root=None):
        self.order = order

        self.n_keys = self.order * 2
        self.n_pages = self.n_keys + 1

        self.keys = keys
        if self.keys is None:
            self.keys = [None] * self.n_keys

        self.pages = pages
        if self.pages is None:
            self.pages = [None] * self.n_pages

        self.root = root
        if self.root is None:
            self.root = False

    def insert(self, page):
        ''' Insert the "page" in the current page according to the B Tree rules.'''

        key = page.keys[0]

        # If the key is already in, do nothing.
        if key in self.keys and page._is_leaf():
            return self

        # When there's no room to insert new key and it's leaf, split the current page.
        if None not in self.keys and self._is_leaf():
            # When the current page is root, the tree is growing upwards.
            return self._split(page)


        for i in range(self.n_keys):

            if self.keys[i] is None:
                # If there's a left page, go there.
                if self._has_page(self.LEFT, self.keys[i]):
                    new_page = self._insert_into_page(self.LEFT, self.keys[i], page)

                    # When split happens, attach the key and pages into current page.
                    if self._split_happened(new_page):
                        # What we have is a root page, with one key and two pages attached.

                        # Getting the split made in left page and putting on current page.
                        if self._is_page_full():
                            return self.insert(new_page)

                        # When there's a element in current position, shift is needed.
                        self._shift(self.keys[i])

                        # Insert the new page into the new allocated position.
                        new_key = new_page.keys[0]
                        left_page = new_page.pages[0]
                        right_page = new_page.pages[1]
                        self.keys[i] = new_key
                        self._insert_page(self.LEFT, new_key, left_page)
                        self._insert_page(self.RIGHT, new_key, right_page)

                    # However, when split doesn't happend, the changes has already made in current page.

                else:
                    # In case there's no pages to go, here's the place to put the key.
                    self.keys[i] = key

                return self


            if key < self.keys[i]:

                if self._is_leaf():
                    # When there's a element in current position, shift is needed.
                    if self._is_page_full():
                        # But if the current page is full, split is needed.
                        return self._split(page)

                    # When there's room to insert the key, perform a right shift.
                    self._shift(self.keys[i])
                    self.keys[i] = key
                    return self

                # If there's a left page, go there.
                if self._has_page(self.LEFT, self.keys[i]):
                    new_page = self._insert_into_page(self.LEFT, self.keys[i], page)

                    # When split happens, attach the key and pages into current page.
                    if self._split_happened(new_page):
                        # What we have is a root page, with one key and two pages attached.

                        # Getting the split made in left page and putting on current page.
                        if self._is_page_full():
                            return self._split(new_page)

                        # When there's a element in current position, shift is needed.
                        self._shift(self.keys[i])

                        # Insert the new page into the new allocated position.
                        new_key = new_page.keys[0]
                        left_page = new_page.pages[0]
                        right_page = new_page.pages[1]
                        self.keys[i] = new_key
                        self._insert_page(self.LEFT, new_key, left_page)
                        self._insert_page(self.RIGHT, new_key, right_page)

                    # However, when split doesn't happend, the changes has already made in current page.

                return self

        # When it didin't find space to insert, it means that key will be inserted into rightmost page.

        # We know that isn't leaf (How?). Inserting the page in the page on RIGHT side.
        new_page = self._insert_into_page(self.RIGHT, self.keys[i], page)

        # When split happens, attach the key and pages into current page.
        if self._split_happened(new_page):
            # What we have is a root page, with one key and two pages attached.

            # Getting the split made in right page and putting on current page.
            if self._is_page_full():
                return self._split(new_page)

            # When there's a element in current position, shift is needed.
            self._shift(self.keys[i])

            # Insert the new page into the new allocated position.
            new_key = new_page.keys[0]
            left_page = new_page.pages[0]
            right_page = new_page.pages[1]
            self.keys[i] = new_key
            self._insert_page(self.LEFT, new_key, left_page)
            self._insert_page(self.RIGHT, new_key, right_page)

        return self

    def _shift(self, key):
        ''' Shift to "side" the elements after "key", with "key" included.'''

        if key is None:
            return False

        # Removing the first occurence of None from keys list.
        self.keys.remove(None)

        # Now putting the None in the correct position.
        key_index = self.keys.index(key)

        # Now putting the None in the correct position.
        self.keys = self.keys[:key_index] + [None] + self.keys[key_index:]

        # Shifting the pages attached to the non leaf page too.
        if self._is_leaf() is False:
            self.pages.remove(None)
            # Silicing the pages list, removing the old page and putting Nones inside.
            self.pages = self.pages[:key_index] + [None, None] + self.pages[key_index+1:]

        return True

    def _split(self, page):
        ''' Add the "page" to current page, split it, and return a new page created.'''

        key = page.keys[0]

        # Placing the new key in the correct place.
        self.keys.append(key)
        self.keys.sort()

        # Promote the middle key of current page.
        middle_key_index = len(self.keys)//2
        promoted_key = self.keys[middle_key_index]

        new_keys = [promoted_key] + ([None] * (self.n_keys - 1))
        new_root = Page(self.order, new_keys, None, True)

        # Splitting the keys into two new list keys: right and left.
        # E.g.: keys = ["a", "b", "NEW", "c", "d"]
        # left_keys = ["a", "b", None, None] and right_keys = ["c", "d", None, None]
        left_keys = self.keys[:middle_key_index] + ([None] * middle_key_index)
        right_keys = self.keys[middle_key_index+1:] + ([None] * middle_key_index)

        left_page = Page(self.order, left_keys)
        right_page = Page(self.order, right_keys)

        # If the page isn't leaf: handling the pages.
        if page._is_leaf() is False:
            right_page = page.pages[0]
            left_page = page.pages[1]

            # Getting the index of the previously splitted page and deleting it.
            page_index = self.keys.index(key)
            self.pages.pop(page_index)

            # Inserting the new pages (the resulting ones of last leaf split) on the position of the deleted page.
            self.pages.insert(page_index, left_page)
            self.pages.insert(page_index, right_page)

            left_pages = self.pages[:middle_key_index+1] + ([None] * (middle_key_index))
            right_pages = self.pages[middle_key_index+1:] + ([None] * (middle_key_index))

            left_page = Page(self.order, left_keys, left_pages)
            right_page = Page(self.order, right_keys, right_pages)

        new_root._insert_page(self.LEFT, promoted_key, left_page)
        new_root._insert_page(self.RIGHT, promoted_key, right_page)

        return new_root

    # Utils.
    def _insert_page(self, side, key, page):
        '''Insert the "page" in the "side" of "key".'''

        key_index = self.keys.index(key)

        if side == self.LEFT:
            self.pages[key_index] = page

        if side == self.RIGHT:
            self.pages[key_index + 1] = page

    def _insert_into_page(self, side, key, page):
        ''' Insert the "page" into the page "side" of "key".'''

        page_index = self._get_page_index(side, key)
        return self.pages[page_index].insert(page)

    def _has_page(self, side, key):
        ''' Check if there's a page in "side" of "key".'''

        page_index = self._get_page_index(side, key)
        if self.pages[page_index] is not None:
            return True
        return False

    def _new_page(self, key):
        keys = [key] + ([None] * (self.n_keys - 1))
        return Page(self.order, keys)

    def _delete_page(self, side, key):
        '''Delete the "page" in the "side" of "key".'''

        page_index = self._get_page_index(side, key)

        self.pages[page_index] = None

    def _get_page_index(self, side, key):
        ''' Return the index of page in the "side" of the "key".'''

        key_index = self.keys.index(key)

        if side == self.LEFT:
            return key_index

        if side == self.RIGHT:
            return key_index+1

        return None

    def _is_page_full(self):
        ''' Checks if the current page is full. If there's space to insert a key, false is returned.'''

        if None in self.keys:
            return False
        return True

    def _is_leaf(self):
        ''' Return True if the current page is leaf. If isn't, return False.'''

        for page in self.pages:
            if page is not None:
                return False
        return True

    @staticmethod
    def _split_happened(page):
        ''' Check if the "page" was splitted.'''

        none_quantity = page.keys.count(None)
        if none_quantity == (page.n_keys-1) and page._is_leaf() is False:
            return True
        return False

    def __str__(self):

        result = "["
        for i in range(len(self.keys)-1):
            result += str(self.keys[i]) + " "
        result += str(self.keys[i+1]) + "]"

        return result

    def _complete_str(self, level=0):
        ''' Return string containing complete tree to show.'''

        if level == 0:
            result = "Root: "
        else:
            result = "\t" * level

        result += self.__str__() + "\n"

        for i in range(self.n_pages):
            if self.pages[i] is not None:
                result += str(i) + ":" + self.pages[i]._complete_str(level + 1)

        return result
