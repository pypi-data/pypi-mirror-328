import wx


class PageOne(wx.Panel):
    def __init__(self, parent, log_panel):
        super().__init__(parent)
        self.log_panel = log_panel

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn = wx.Button(self, label="Log from Page One")
        btn.Bind(wx.EVT_BUTTON, self.on_log)
        
        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)

    def on_log(self, event):
        self.log_panel.log_message("Button clicked from Page One")

class PageTwo(wx.Panel):
    def __init__(self, parent, log_panel):
        super().__init__(parent)
        self.log_panel = log_panel

        sizer = wx.BoxSizer(wx.VERTICAL)
        btn = wx.Button(self, label="Log from Page Two")
        btn.Bind(wx.EVT_BUTTON, self.on_log)

        sizer.Add(btn, 0, wx.ALL, 10)
        self.SetSizer(sizer)

    def on_log(self, event):
        self.log_panel.log_message("Button clicked from Page Two")


class LogPanel(wx.Panel):
    """A panel containing a shared log in a StaticBox."""
    def __init__(self, parent):
        super().__init__(parent)
        
        box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, label="Log Output"), wx.VERTICAL)
        self.log_ctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL, size=(300, 200))
        
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

    # set font for the statictext
    sb.SetFont(font)
    required_boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
    main_boxsizer.Add(required_boxsizer,
        flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)
    required_gbs = wx.GridBagSizer(vgap=1, hgap=5)

    static_text = wx.StaticText(panel, -1)
    size = static_text.GetSize()
    static_text.SetMinSize(size)
    static_text.SetLabel("test")
    required_gbs.Add(static_text, (0, 0))

    entry = wx.TextCtrl(panel, -1, size=(-1, -1), style=wx.TE_RICH)
    entry.SetValue("test")
    ok_button = wx.Button(panel, -1, label="Ok")
    main_boxsizer.Add(
        ok_button,
        flag=wx.BOTTOM | wx.RIGHT | wx.ALIGN_RIGHT,
        border=10,
    )
    required_gbs.Add(entry, flag=wx.EXPAND, pos=(0, 1))

    static_text = wx.StaticText(panel, -1)
    size = static_text.GetSize()
    static_text.SetMinSize(size)
    static_text.SetLabel("test")
    required_gbs.Add(static_text, (1, 0))

    entry = wx.TextCtrl(panel, -1, size=(-1, -1), style=wx.TE_RICH)
    entry.SetValue("test")
    required_gbs.Add(entry, flag=wx.EXPAND, pos=(1, 1))
    required_gbs.AddGrowableCol(1)
    required_boxsizer.Add(required_gbs, 1, wx.EXPAND | wx.ALL, 10)
    required_boxsizer.SetSizeHints(panel)

    panel.SetSizerAndFit(main_boxsizer)
    return panel

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Notebook with Shared Log")
        
        self.panel = wx.Panel(self, -1, style=wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.FULL_REPAINT_ON_RESIZE)
        vbox = wx.BoxSizer(wx.VERTICAL)

        panel = build_gui(self.panel)
        
        
        # Notebook
        vbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)

        # Shared log panel
        self.log_panel = LogPanel(self.panel)
        vbox.Add(self.log_panel, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizerAndFit(vbox)
        self.CreateStatusBar()
        self.SetStatusText("")
        self.Centre()

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

