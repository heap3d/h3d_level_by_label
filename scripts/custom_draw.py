#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# set custom draw options for selected items


import modo
import modo.constants as c
import lx


CUSTOM_COLOR_STR = '0.0 0.0 1.0'


def main():
    items = modo.Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)
    for item in items:
        try:
            lx.eval(f'!item.draw add locator item:{{{item.id}}}')
        except RuntimeError:
            print(f'item <{item.name}> already has custom Draw Options')
        lx.eval(f'item.channel locator$wireOptions user item:{{{item.id}}}')
        lx.eval(f'item.channel locator$wireColor {{{CUSTOM_COLOR_STR}}} item:{{{item.id}}}')
        lx.eval(f'item.channel locator$style wire item:{{{item.id}}}')


if __name__ == '__main__':
    main()
