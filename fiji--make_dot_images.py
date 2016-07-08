from ij import IJ
from ij.gui import OvalRoi, Line

imp = IJ.createImage("Untitled", "8-bit black", 512, 512, 1);
IJ.run(imp, "RGB Color", "");
IJ.run(imp, "Radial Gradient", "");
IJ.run(imp, "8-bit", "");
IJ.run(imp, "Divide...", "value=2");

r = 4
c = 256
dc = 30
n = 8

for i in range(n):
  imp.setRoi(OvalRoi(c-i*dc,c-i*dc,r,r));
  IJ.run(imp, "Multiply...", "value=2.0000");

# Line
imp.setRoi(80,50,int(3/2*c),4);
IJ.run(imp, "Multiply...", "value=2.0000");

# Circle
imp.setRoi(OvalRoi(int(c/2),int(c/2+c),50,50));
IJ.run(imp, "Multiply...", "value=2.0000");

imp.setRoi(OvalRoi(int(c/2+c),int(c/2+c),50,50));
IJ.setBackgroundColor(0, 0, 0);
IJ.run(imp, "Clear", "slice");

imp.show();
