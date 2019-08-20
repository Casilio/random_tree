#!/usr/bin/env python3.6

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

    def generate(self, event = None):
        w, h = self.panel1.GetClientSize()

        dc = wx.ClientDC(self.panel1)
        dc.Clear()
        dc.DrawLine(0, 0, w, h)

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

