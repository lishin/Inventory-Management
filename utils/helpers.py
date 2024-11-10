import wx

def show_message(message, title='提示', style=wx.OK | wx.ICON_INFORMATION):
    dlg = wx.MessageDialog(None, message, title, style)
    dlg.ShowModal()
    dlg.Destroy()
