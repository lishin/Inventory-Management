# ui/login.py

import wx
from models.user_model import UserModel
from utils.security import verify_password
from ui.main_frame import MainFrame

class LoginFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, title='用户登录', size=(400, 300))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # 用户名
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='用户名：')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.username_tc = wx.TextCtrl(panel)
        hbox1.Add(self.username_tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 密码
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='密码：')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.password_tc = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        hbox2.Add(self.password_tc, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 登录按钮
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        login_btn = wx.Button(panel, label='登录')
        login_btn.Bind(wx.EVT_BUTTON, self.on_login)
        hbox3.Add(login_btn)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER|wx.TOP, border=20)

        panel.SetSizer(vbox)

    def on_login(self, event):
        username = self.username_tc.GetValue()
        password = self.password_tc.GetValue()

        user_model = UserModel()
        user = user_model.get_user_by_username(username)
        if user and verify_password(password, user[2]):  # user[2] 为 password_hash
            wx.MessageBox('登录成功！', '提示', wx.OK | wx.ICON_INFORMATION)
            user_model.update_last_login(user[0])
            # 打开主界面
            self.Close()
            main_frame = MainFrame(user)
            main_frame.Show()
        else:
            wx.MessageBox('用户名或密码错误！', '错误', wx.OK | wx.ICON_ERROR)
        user_model.close()
