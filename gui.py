#!/usr/bin/env python3.6

import math
import random
import wx

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.splitter = wx.SplitterWindow(self)
        self.panel1 = wx.Panel(self.splitter)
        self.panel2 = wx.Panel(self.splitter)
        
        self.seedInput = wx.TextCtrl(self.panel2, wx.ID_ANY)
        self.generateBtn = wx.Button(self.panel2, wx.ID_ANY, 'Generate')
        self.randomizeBtn = wx.Button(self.panel2, wx.ID_ANY, 'Randomize')

        self.randomizeBtn.Bind(wx.EVT_BUTTON, self.randomizeSeed)
        self.generateBtn.Bind(wx.EVT_BUTTON, self.generate)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.AddStretchSpacer(100)
        hbox.Add(self.seedInput)
        hbox.Add(self.generateBtn)
        hbox.Add(self.randomizeBtn)
        hbox.AddStretchSpacer(100)
    
        self.panel2.SetSizer(hbox)

        self.splitter.SetSashGravity(.8)
        self.splitter.SplitHorizontally(self.panel1, self.panel2)

        self.randomizeSeed()

    def randomizeSeed(self, event = None):
        value = (int)(random.random() * 100_000)
        self.seedInput.SetValue((str)(value))

    def getSeed(self):
        seed = self.seedInput.GetValue()
        while len(seed) == 0:
            self.randomizeSeed()
            seed = self.seedInput.GetValue()

        return seed

    def generate(self, event = None):
        random.seed(self.getSeed())

        w, h = self.panel1.GetClientSize()
        x = w / 2;
        y = h;
        angle = -math.pi / 2
        length = (int)(y * random.randint(20, 30) / 100.0)
        thickness = 5

        dc = wx.ClientDC(self.panel1)
        dc.Clear()
        
        self.renderTree(dc, x, y, length, thickness, angle)

    def renderTree(self, dc, x, y, length, thickness, angle):
        pen = dc.GetPen()
        pen.SetWidth(thickness)

        dc.SetPen(pen)

        x1 = (int)(x + length * math.cos(angle))
        y1 = (int)(y + length * math.sin(angle))

        dc.DrawLine(x, y, x1, y1)

        for _branch in [1] * random.randrange(2,6):
            scale = random.randint(60, 80) / 100.0
            new_length = length * scale
            new_thickness = thickness * scale
            
            if new_length > 4:
                new_angle = angle + random.randint(-61, 60) * -math.pi / 180.0

                self.renderTree(dc, x1, y1, new_length, new_thickness, new_angle)



class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'Random Tree')
        frame.SetMinClientSize(wx.Size(300, 400))
        frame.Center()
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()

