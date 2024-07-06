#!/usr/bin/python
# ================================
# (C)2024 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# set pos Y for the selected items using label data


import modo
import lx
import modo.constants as c

from h3d_utilites.scripts.h3d_debug import H3dDebug
from h3d_utilites.scripts.h3d_utils import replace_file_ext


class Axis:
    x = 'X'
    y = 'Y'
    z = 'Z'


def get_label(item: modo.Item) -> str:
    return lx.eval(f'item.help label:? item:{item.id}')  # type: ignore


def set_pos(axis: str = Axis.y, item=None, value=None):
    if not item:
        return
    if not value:
        return
    lx.eval(f'transform.channel pos.{axis} {value} item:{item.id}')


def main():
    items = modo.Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)

    for item in items:
        set_pos(item=item, value=get_label(item))


if __name__ == '__main__':
    h3dd = H3dDebug(
        enable=False, file=replace_file_ext(modo.Scene().filename, ".log")
    )
    main()
