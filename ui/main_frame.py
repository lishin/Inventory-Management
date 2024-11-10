# ui/main_frame.py

import wx
from config import SYSTEM_NAME, ROLES
from ui.product_frame import ProductFrame
from ui.charts import SalesChartFrame

class MainFrame(wx.Frame):
    def __init__(self, user):
        super().__init__(None, title=SYSTEM_NAME, size=(800, 600))
        self.user = user  # 当前登录用户

        # 创建菜单栏
        menu_bar = wx.MenuBar()

        # 基础资料菜单
        basic_menu = wx.Menu()
        product_item = basic_menu.Append(wx.ID_ANY, '商品管理')
        # 可以添加更多基础资料菜单项
        menu_bar.Append(basic_menu, '基础资料')

        # 报表菜单
        report_menu = wx.Menu()
        sales_chart_item = report_menu.Append(wx.ID_ANY, '销售趋势图')
        menu_bar.Append(report_menu, '报表')

        # 数据备份菜单
        backup_menu = wx.Menu()
        backup_item = backup_menu.Append(wx.ID_ANY, '数据备份')
        restore_item = backup_menu.Append(wx.ID_ANY, '数据恢复')
        menu_bar.Append(backup_menu, '数据备份与恢复')

        # 设置菜单栏
        self.SetMenuBar(menu_bar)

        # 绑定菜单事件
        self.Bind(wx.EVT_MENU, self.on_product_manage, product_item)
        self.Bind(wx.EVT_MENU, self.on_sales_chart, sales_chart_item)
        self.Bind(wx.EVT_MENU, self.on_backup, backup_item)
        self.Bind(wx.EVT_MENU, self.on_restore, restore_item)

        # 创建状态栏
        status_bar = self.CreateStatusBar()
        status_bar.SetStatusText(f'当前用户：{self.user[1]}（{ROLES.get(self.user[3], "未知角色")}）')

    def on_product_manage(self, event):
        # 检查权限
        if self.user[3] not in ['admin', 'purchaser']:
            wx.MessageBox('您无权访问此功能！', '权限不足', wx.OK | wx.ICON_WARNING)
            return
        # 打开商品管理界面
        product_frame = ProductFrame()
        product_frame.Show()

    def on_sales_chart(self, event):
        # 检查权限
        if self.user[3] not in ['admin', 'salesperson', 'finance']:
            wx.MessageBox('您无权访问此功能！', '权限不足', wx.OK | wx.ICON_WARNING)
            return
        # 打开销售趋势图界面
        chart_frame = SalesChartFrame()
        chart_frame.Show()

    def on_backup(self, event):
        # 检查权限
        if self.user[3] != 'admin':
            wx.MessageBox('您无权访问此功能！', '权限不足', wx.OK | wx.ICON_WARNING)
            return
        # 执行备份操作
        from controllers.backup_controller import BackupController
        backup_controller = BackupController()
        backup_path = backup_controller.backup_database()
        wx.MessageBox(f'备份成功！备份文件路径：{backup_path}', '备份成功', wx.OK | wx.ICON_INFORMATION)

    def on_restore(self, event):
        # 检查权限
        if self.user[3] != 'admin':
            wx.MessageBox('您无权访问此功能！', '权限不足', wx.OK | wx.ICON_WARNING)
            return
        # 打开文件选择对话框
        with wx.FileDialog(self, "选择备份文件", wildcard="Database files (*.db)|*.db",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # 用户取消

            # 获取选择的文件路径
            backup_file = fileDialog.GetPath()

        # 执行恢复操作
        from controllers.backup_controller import BackupController
        backup_controller = BackupController()
        success = backup_controller.restore_database(backup_file)
        if success:
            wx.MessageBox('恢复成功！请重启应用程序以应用更改。', '恢复成功', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('恢复失败！备份文件不存在。', '恢复失败', wx.OK | wx.ICON_ERROR)
