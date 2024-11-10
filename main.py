# main.py

import wx
from ui.login import LoginFrame
from models.database import initialize_db
from models.user_model import UserModel

def main():
    # 初始化数据库
    initialize_db()

    # 创建默认管理员用户（如果不存在）
    user_model = UserModel()
    admin = user_model.get_user_by_username('admin')
    if not admin:
        user_model.create_user('admin', 'admin123', 'admin')
        print('默认管理员账户已创建：用户名：admin，密码：admin123')
    user_model.close()

    app = wx.App()
    login_frame = LoginFrame()
    login_frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
