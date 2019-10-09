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

from b_tree import BTree # pylint: disable=no-name-in-module,no-absolute-import

def main():
    '''Main.'''
    b_tree = BTree()
    b_tree.run()

if __name__ == '__main__':
    main()
