
import wx
class Mywin(wx.Frame): 
   def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (400,580))  
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      self.combobox = wx.ComboBox(panel, choices = ["Option 1", "Option 2", "Option 42 long long long..."], pos = (120,50), name="Aaa",)
      self.rb2 = wx.RadioButton(panel,33, label = 'radio button1',pos = (120,100)) 
      self.rb2 = wx.RadioButton(panel,22, label = 'radio button2',pos = (120,120)) 
      self.btn = wx.Button(panel,-1,"click Me") 
      vbox.Add(self.btn,0) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClicked) 
      

      self.tbtn = wx.ToggleButton(panel , -1, "click to on")  
      self.tbtn.Bind(wx.EVT_TOGGLEBUTTON,self.OnToggle) 
      hbox = wx.BoxSizer(wx.HORIZONTAL) 
      vbox.Add(hbox,1) 
      panel.SetSizer(vbox)
      
      #self.t1 = wx.TextCtrl(panel,pos=(120,500))
      
        
      self.Centre() 
      self.Show() 
      self.Fit()  
      self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)
      sizer = wx.GridBagSizer(5, 5)

      self.st1 = wx.StaticText(panel, label='Convert Fahrenheit temperature to Celsius',pos=(120,160))
      #sizer.Add(st1, pos=(120, 140), span=(1, 2), flag=wx.ALL, border=15)

      self.st2 = wx.StaticText(panel, label='Fahrenheit:',pos=(120,180))
      #sizer.Add(st2, pos=(120, 150), flag=wx.ALL | wx.ALIGN_CENTER, border=15)
        
      self.sc = wx.SpinCtrl(panel, value='0',pos=(200,180))
      self.sc.SetRange(-459, 1000)

      sizer.Add(self.sc, pos=(120, 160), flag=wx.ALIGN_CENTER)

      self.st3 = wx.StaticText(panel, label='Celsius:',pos=(120,250))
      #sizer.Add(st3, pos=(120, 170), flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

      self.celsius = wx.StaticText(panel, label='',pos=(190,250))
      #sizer.Add(self.celsius, pos=(120, 180), flag=wx.ALL, border=15)

      computeButton = wx.Button(panel, label='Compute',pos=(120,300))
      computeButton.SetFocus()
      #sizer.Add(computeButton, pos=(120, 190), flag=wx.ALIGN_RIGHT|wx.TOP, border=30)

      closeButton = wx.Button(panel, label='Close',pos=(250,300))
      #sizer.Add(closeButton, pos=(120, 200), flag=wx.ALIGN_LEFT|wx.TOP, border=30)

      computeButton.Bind(wx.EVT_BUTTON, self.OnCompute)
      closeButton.Bind(wx.EVT_BUTTON, self.OnClose)


      self.SetTitle('wx.SpinCtrl')
      self.Centre()
  
   def OnRadiogroup(self, e): 
       
       rb = e.GetEventObject() 
       print (rb.GetLabel(),' is clicked from Radio Group') 
   def OnClicked(self, event): 
      btn = event.GetEventObject().GetLabel() 
      print("Label of pressed button = ",btn)
   
   def OnToggle(self,event): 
      state = event.GetEventObject().GetValue() 
		
      if state == True: 
         print("Toggle button state off") 
         event.GetEventObject().SetLabel("click to off") 
      else: 
         print(" Toggle button state on") 
         event.GetEventObject().SetLabel("click to on") 

   def OnCompute(self, e): #fahrenheit celcius dönüşümü

        fahr = self.sc.GetValue() 
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))
   def OnClose(self, e):

        self.Close(True)
   

app = wx.App() 
Mywin(None,  'Button demo') 
app.MainLoop()
