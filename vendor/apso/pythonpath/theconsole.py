# -*- coding: utf-8 -*-

console = None
history = []


def tofront():
    console.dialog.setVisible(True)
    console.dialog.toFront()


def close():
    console.enddialog()
