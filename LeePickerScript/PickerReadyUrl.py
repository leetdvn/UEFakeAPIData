import urllib as ulib
import maya.OpenMayaMPx as ompx
url='%1'
content = ulib.urlopen(url)
data=content.read()
ompx.MPxCommand_setResult(data)