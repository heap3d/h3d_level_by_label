#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# deselect items with custom draw options


import modo
import modo.constants as c
import lx


def main():
    items = modo.Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)
    for item in items:
        try:
            lx.eval(f'!item.draw add locator item:{item.id}')
        except RuntimeError:
            item.deselect()
            continue
        lx.eval(f'item.draw rem locator item:{item.id}')


if __name__ == '__main__':
    main()
