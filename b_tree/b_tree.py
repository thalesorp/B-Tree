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

        numbers = [33, 50, 50, 29, 26, 12, 44, 70, 56, 90, 60, 92, 87, 75, 89, 55, 43, 15, 26, 57, 8, 100, 96, 39, 13, 21, 101, 45, 41, 84, 35, 51]
        #numbers = [3234, 7715, 4126, 8858, 1234, 6340, 4077, 6412, 8596, 4837, 4110, 4593, 3824, 5028, 5803, 5516, 8681, 9137, 3025, 8705, 2818, 6241, 6008, 4326, 7544, 1465, 3505, 3799, 658, 5935, 2559, 7773, 8705, 7952, 4187, 1733, 2272, 1061, 1905, 1935, 5807, 51, 9954, 5806, 8267, 1782, 1874, 2090, 2339, 3966, 1906, 8274, 8231, 3489, 2747, 1945, 737, 2425, 7415, 4014, 1113, 1907, 1038, 4375, 1121, 3025, 4130, 9895, 8745, 534, 7406, 1542, 4559, 7139, 4333, 6207, 5349, 6807, 8900, 382, 7520, 9705, 226, 9042, 9280, 2578, 3418, 5215, 6175, 9494, 9317, 6604, 6171, 6445, 7732, 7941, 2837, 7378, 3827, 2253, 8319, 3372, 5118, 8713, 3293, 1507, 435, 3616, 9996, 7881, 7793, 7290, 6066, 2039, 6979, 4584, 4374, 7599, 1712, 9449, 6844, 4679, 2437, 4466, 9581, 9813, 6450, 6342, 6161, 6680, 1116, 6666, 4750, 1491, 1637, 7198, 4568, 8813, 9618, 4218, 5014, 981, 2413, 3641, 4464, 7200, 5731, 2280, 5596, 9967, 9057, 9722, 6664, 9053, 7566, 3159, 6389, 5377, 7515, 8399, 6738, 6605, 2547, 9725, 3747, 7935, 9491, 8337, 8377, 8584, 8682, 8523, 8471, 1054, 9293, 7302, 9730, 1486, 7958, 8614, 5454, 5222, 6113, 7310, 4578, 8574, 6260, 6338, 4105, 6475, 4449, 9329, 9942, 168, 2995, 9348, 5843, 421, 6599, 8513, 712, 5361, 7539, 1383, 1947, 3923, 7465, 5709, 6576, 180, 7435, 1987, 4337, 9371, 932, 1893, 2507, 3302, 9132, 8791, 9619, 2104, 7265, 2362, 284, 4797, 983, 4421, 4157, 4657, 7580, 3294, 2012, 2556, 9806, 5329, 4948, 9330, 2561, 3890, 4105, 7506, 8524, 2225, 1044, 3340, 8510, 2333, 8463, 5544, 4514, 8511, 4837, 8900, 7722, 2807, 2212, 7791, 7450, 5202, 8640, 5946, 3983, 6845, 2312, 5139, 8408, 6643, 2281, 9972, 3990, 8124, 5819, 8243, 2019, 7801, 5792, 5690, 4374, 8201, 7525, 3948, 7818, 9874, 6820, 9111, 636, 3742, 291, 806, 634, 2163, 887, 7326, 3388, 462, 4095, 3926, 5642, 260, 3404, 304, 8014, 7657, 4101, 320, 1084, 3480, 4414, 8801, 5454, 2357, 7077, 334, 2577, 3344, 711, 7350, 4078, 2679, 7565, 5682, 3199, 4549, 3066, 3480, 6415, 6197, 8613, 3472, 587, 2339, 7796, 9669, 8120, 7555, 7278, 4935, 5601, 3234, 4711, 8155, 7892, 6114, 7807, 8927, 4734, 9631, 2407, 1788, 8912, 2870, 7768, 2183, 1661, 7950, 3283, 826, 9479, 7329, 2888, 4290, 4755, 6280, 3374, 2853, 2136, 7404, 6672, 4850, 2589, 3969, 1626, 1863, 1024, 9042, 9614, 3806, 5038, 6168, 4127, 8252, 3954, 8869, 5126, 4697, 5597, 6030, 5165, 9062, 6493, 7237, 6251, 316, 4577, 6159, 7789, 2427, 6309, 8261, 7721, 7353, 8603, 3795, 3251, 9883, 7898, 5133, 4502, 2836, 3581, 949, 7427, 5593, 6062, 6213, 142, 5303, 4606, 8990, 1126, 2304, 2490, 4401, 616, 2696, 1732, 7491, 1870, 9034, 735, 5640, 8779, 2923, 6771, 6249, 4709, 5160, 597, 2478, 9924, 7137, 6194, 6650, 1195, 2392, 259, 9954, 4780, 9826, 1060, 5551, 5043, 1884, 5990, 4081, 9763, 546, 990, 7361, 2118, 4228, 8412, 2879, 9781, 1127, 1804, 6723, 9017, 7075, 3081, 1617, 7086, 2538, 482, 1547, 5506, 1857, 2740, 5850, 1125, 2300, 5740, 6166, 7599, 4652, 2205, 3566, 5274, 5331, 344, 9905, 3009, 6876, 6363, 9604, 6526, 3814, 6272, 5313, 7425, 6379, 7485, 5718, 8748, 7283, 1032, 7090, 3817, 1171, 3390, 8965, 8347, 600, 5991, 7888, 1597, 8109, 7350, 77, 6806, 7850, 2495, 994, 8913, 325, 2848, 2622, 7095, 4054, 8332, 165, 2666, 2403, 2484, 9889, 4979, 8140, 7750, 7693, 965, 6697, 8278, 1113, 571, 5277, 8303, 5604, 7131, 4463, 2051, 9022, 7719, 1908, 4519, 6854, 7493, 7967, 7178, 3007, 5091, 8321, 6510, 2009, 88, 7175, 7299, 2460, 2280, 2847, 5035, 35, 6864, 6202, 4198, 7939, 1237, 791, 5561, 9261, 2439, 7697, 1324, 9988, 7100, 521, 7869, 1110, 7497, 8454, 4806, 9689, 6904, 720, 1521, 6067, 3010, 921, 3628, 6618, 1506, 468, 4921, 9544, 3437, 4362, 3228, 8598, 7919, 7051, 7191, 7361, 487, 264, 9067, 9793, 4552, 8154, 3733, 9989, 2751, 1436, 2926, 9111, 664, 2788, 1634, 379, 1915, 3331, 9242, 7823, 7064, 724, 5258, 9763, 9683, 9989, 8588, 5265, 3803, 6502, 8558, 7100, 6332, 7628, 4638, 2275, 32, 1263, 4804, 7391, 4524, 7316, 4678, 9558, 928, 5148, 5624, 2634, 3115, 1600, 456, 2080, 9425, 8512, 9441, 6586, 9322, 1790, 7080, 5200, 2333, 1253, 2558, 6413, 1155, 7632, 2324, 4506, 3304, 5649, 3333, 6318, 2938, 2500, 1873, 2531, 3711, 2898, 1806, 2467, 605, 9309, 8123, 4551, 7762, 1196, 8390, 586, 743, 7799, 1177, 2653, 2935, 8048, 5072, 1375, 3737, 2374, 2863, 8860, 2158, 9298, 4209, 5918, 8944, 4089, 7227, 3993, 1376, 2990, 5120, 3013, 9878, 9093, 2449, 9292, 3185, 6872, 174, 5038, 5293, 7983, 7187, 8650, 1310, 1790, 4617, 6655, 5186, 259, 2084, 5946, 8879, 4084, 151, 2988, 7192, 3947, 5707, 4037, 5052, 3218, 685, 9162, 1990, 9533, 8514, 1736, 9281, 1103, 848, 9281, 8129, 9552, 1017, 7037, 6347, 165, 557, 7132, 47, 3830, 315, 2993, 1875, 1015, 2720, 829, 4038, 1101, 3399, 2084, 6807, 4298, 7876, 476, 3460, 9908, 8111, 7580, 8568, 2940, 7134, 3250, 6356, 662, 810, 5762, 968, 528, 461, 1135, 6232, 521, 4567, 7387, 1416, 8053, 5713, 2364, 7818, 9233, 1860, 6543, 6451, 3040, 1447, 59, 5005, 6732, 5922, 9871, 181, 8294, 650, 5295, 7215, 9688, 1578, 4530, 1021, 2727, 9631, 9208, 7226, 9701, 428, 3749, 955, 8210, 7599, 1199, 4631, 5078, 8704, 2393, 5861, 6865, 3321, 8465, 3219, 8886, 4156, 2911, 8215, 4680, 1018, 6695, 2430, 5039, 4878, 7075, 7385, 9766, 5699, 7765, 19, 8706, 499, 4568, 7770, 7824, 1751, 8464, 5668, 3051, 2597, 6646, 4622, 4187, 2934, 3753, 6794, 9719, 565, 634, 3734, 8622, 4447, 9283, 310, 7667, 8058, 1995, 8478, 9187, 1900, 8001, 5355, 6198, 9839, 2310, 6921, 821, 1325, 9882, 3810, 2727, 531, 3453, 413, 7287, 1327, 8967, 4441, 8297, 5414, 6294, 4962, 6203, 8724, 474, 9193, 6788, 5367, 7664, 9450, 2551, 3930, 1999, 692, 829, 4110, 983, 5091, 5110, 5547, 6679, 8398, 9663, 3206, 1464, 4402, 1212, 2093, 2347, 7536, 6618, 6799, 6606, 3185, 4562, 8819, 4247, 7131, 8105, 884, 1929, 4841, 4556, 9658, 8959, 7858, 2685, 778, 2794, 8217, 1835, 4342, 571, 4176, 2193, 420, 4309, 4717, 202, 4380, 2304, 1719, 3013, 2819, 5832, 6731, 9760, 5987, 8686, 4194, 4555, 9448, 1553, 8069, 7172, 9967, 304, 1915, 5312, 7339, 9694]
        #numbers = [1, 2, 3, 4]#, 5, 6, 7, 8, 9, 10]

        for number in numbers:
            self.insert(number)
        self.show()

        #number = 101
        #print(str("Finding value " + str(number) + ": "), end = '')
        #print(str(self.search(number)))

        number = 4
        print(str("Deleting value " + str(number) + "."))
        self.show()

    def insert(self, key):
        ''' Insert the "key" value in current B Tree.'''

        keys = [key] + ([None] * ((self.order * 2)-1))
        page = Page(self.order, keys)

        self.root = self.root.insert(page)

    def search(self, key):
        ''' Depth search algorithm.'''

        return self.root.search(key)

    def delete(self, key):
        ''' Delete the "key" from the tree.'''

        self.root.delete(key)

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
                        self._shift(self.RIGHT, self.keys[i])

                        # Insert the new page into the new allocated position.
                        self._insert_page(new_page, i)

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
                    self._shift(self.RIGHT, self.keys[i])
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
                        self._shift(self.RIGHT, self.keys[i])

                        # Insert the new page into the new allocated position.
                        self._insert_page(new_page, i)

                    # However, when split doesn't happend, the changes has already made in current page.

                return self

        # When it didin't search space to insert, it means that key will be inserted into rightmost page.

        # We know that isn't leaf (How?). Inserting the page in the page on RIGHT side.
        new_page = self._insert_into_page(self.RIGHT, self.keys[i], page)

        # When split happens, attach the key and pages into current page.
        if self._split_happened(new_page):
            # What we have is a root page, with one key and two pages attached.

            # Getting the split made in right page and putting on current page.
            if self._is_page_full():
                return self._split(new_page)

            # When there's a element in current position, shift is needed.
            self._shift(self.RIGHT, self.keys[i])

            # Insert the new page into the new allocated position.
            self._insert_page(new_page, i)

        return self

    def search(self, key):
        ''' Depth search algorithm.'''

        if key in self.keys:
            # If the sought key is in current page.
            return True
        elif self._is_leaf():
            # If current page is leaf and the number isn't here.
            return False

        for i in range(self.n_keys):

            # If there's a left page, go there.
            if self._has_page(self.LEFT, self.keys[i]):
                page_index = self._get_page_index(self.LEFT, self.keys[i])
                # If finds it, return True. Else, keep searching.
                if self.pages[page_index].search(key) is True:
                    return True

        # If there's a right page, go there.
        if self._has_page(self.RIGHT, self.keys[i]):
            page_index = self._get_page_index(self.RIGHT, self.keys[i])
            # If finds it, return True.
            if self.pages[page_index].search(key) is True:
                return True

        # If the key wasn't found, it's because current tree doesn't have it.
        return False

    def delete(self, key):
        ''' Delete the "key" from the current page, or children pages.'''

        if key in self.keys:
            if self._is_leaf():
                # Actually removing the key from the keys list.
                self.keys.remove(key)
                self._shift(self.LEFT)
                return True
            else:
                # ???
                return True

        for i in range(self.n_keys):

            # If there's a left page, go there.
            if self._has_page(self.LEFT, self.keys[i]):
                page_index = self._get_page_index(self.LEFT, self.keys[i])
                # If has already deleted, return True. Else, keep searching.
                if self.pages[page_index].delete(key) is True:
                    return True

        # If there's a right page, go there.
        if self._has_page(self.RIGHT, self.keys[i]):
            page_index = self._get_page_index(self.RIGHT, self.keys[i])
            # If has already deleted, return True.
            if self.pages[page_index].delete(key) is True:
                return True

        # If the key wasn't found, it's because current tree doesn't have it.
        return False

    def _shift(self, side, key=None):
        ''' Shift to "side" the elements after "key", with "key" included.'''

        if side == self.RIGHT and key is None:
            return False

        key_index = self.keys.index(key) # TODO: WARNING! Doing this before removing None from keys list.

        # Removing the first occurence of None from keys list.
        self.keys.remove(None)

        # Now putting the None in the correct position.
        if side == self.LEFT:
            self.keys.append(None)
        if side == self.RIGHT:
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

        new_root._insert_single_page(self.LEFT, 0, left_page)
        new_root._insert_single_page(self.RIGHT, 0, right_page)

        return new_root

    # Utils.
    def _insert_into_page(self, side, key, page):
        ''' Insert the "page" into the page "side" of "key".'''

        page_index = self._get_page_index(side, key)
        return self.pages[page_index].insert(page)

    def _insert_single_page(self, side, key_index, page):
        '''Insert the "page" in the "side" of key in position "key_index".'''

        #key_index = self.keys.index(key)

        if side == self.LEFT:
            self.pages[key_index] = page

        if side == self.RIGHT:
            self.pages[key_index + 1] = page

    def _insert_page(self, page, key_index):
        new_key = page.keys[0]
        left_page = page.pages[0]
        right_page = page.pages[1]
        self.keys[key_index] = new_key
        self._insert_single_page(self.LEFT, key_index, left_page)
        self._insert_single_page(self.RIGHT, key_index, right_page)

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
