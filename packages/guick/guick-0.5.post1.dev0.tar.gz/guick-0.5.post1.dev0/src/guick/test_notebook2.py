import wx

class LogPanel(wx.Panel):
    """A panel containing a shared log in a StaticBox."""
    def __init__(self, parent):
        super().__init__(parent)
        
        box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Log Output"), wx.VERTICAL)
        self.log_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        
        box_sizer.Add(self.log_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(box_sizer)

    def log_message(self, message):
        """Appends a message to the log."""
        self.log_ctrl.AppendText(message + "\n")

def build_gui(parent):
    panel = wx.Panel(parent)
    main_boxsizer = wx.BoxSizer(wx.VERTICAL)

    sb = wx.StaticBox(panel, label="Required Parameters")
    font = wx.Font(wx.FontInfo(10).Bold())
    sb.SetFont(font)

    required_boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
    main_boxsizer.Add(required_boxsizer, flag=wx.EXPAND | wx.ALL, border=10)

    required_gbs = wx.GridBagSizer(vgap=1, hgap=5)

    # First row
    static_text1 = wx.StaticText(panel, label="Parameter 1")
    required_gbs.Add(static_text1, (0, 0), flag=wx.ALIGN_CENTER_VERTICAL)

    entry1 = wx.TextCtrl(panel, style=wx.TE_RICH,)
    entry1.SetValue("test")
    entry1.SetMinSize((100, -1))
    required_gbs.Add(entry1, (0, 1), flag=wx.EXPAND)

    # Second row
    static_text2 = wx.StaticText(panel, label="Parameter 2")
    required_gbs.Add(static_text2, (1, 0), flag=wx.ALIGN_CENTER_VERTICAL)

    entry2 = wx.TextCtrl(panel, style=wx.TE_RICH)
    entry2.SetValue("test")
    required_gbs.Add(entry2, (1, 1), flag=wx.EXPAND)

    required_gbs.AddGrowableCol(1)
    required_boxsizer.Add(required_gbs, 1, wx.EXPAND | wx.ALL, 10)

    # Add button inside box sizer
    ok_button = wx.Button(panel, label="Ok")
    required_boxsizer.Add(ok_button, flag=wx.ALIGN_RIGHT | wx.ALL, border=10)

    required_boxsizer.SetSizeHints(panel)
    panel.SetSizerAndFit(main_boxsizer)
    panel.SetSizeHints(-1, -1)
    panel.Fit()

    return panel

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Notebook with Shared Log")
        
        self.panel = wx.Panel(self, style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # GUI Panel
        gui_panel = build_gui(self.panel)
        vbox.Add(gui_panel, 1, wx.EXPAND | wx.ALL, 10)

        # Shared log panel
        self.log_panel = LogPanel(self.panel)
        vbox.Add(self.log_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.panel.SetSizerAndFit(vbox)
        self.Fit()

        self.CreateStatusBar()
        self.SetStatusText("")
        self.Centre()
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

