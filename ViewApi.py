from View import *

def getMainWindow():
    return MainWindow.getInstance()

def updateHeader(info):
    View.getInstance().updateHeader(info)

def updateCell(name, number):
    View.getInstance().updateCell(name, number)

def setCellTransparent(number, opt):
    View.getInstance().setCellTransparent(number, opt)