#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# deselect items with non-empty label


import modo
import modo.constants as c

from h3d_level_by_label.scripts.level_by_label import get_label


def main():
    items = modo.Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)
    for item in items:
        label = get_label(item)
        if label:
            item.deselect()


if __name__ == '__main__':
    main()
