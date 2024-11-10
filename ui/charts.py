import wx
import wx.lib.plot as wxplot
import numpy as np
from models.sales_model import SalesModel

class SalesChartFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='销售趋势图', size=(600, 400))
        panel = wx.Panel(self)

        # 获取销售数据
        sales_model = SalesModel()
        data = sales_model.get_sales_data_by_date()
        sales_model.close()

        if not data:
            wx.MessageBox('暂无销售数据。', '提示', wx.OK | wx.ICON_INFORMATION)
            self.Close()
            return

        # 准备数据
        dates = [d[0] for d in data]
        amounts = [d[1] for d in data]

        # 转换为 numpy 数组
        x = np.arange(len(dates))
        y = np.array(amounts)

        # 创建折线图数据
        plot_data = wxplot.PolyLine(list(zip(x, y)), legend='销售额', colour='blue', width=2)

        # 创建绘图窗口
        client = wxplot.PlotCanvas(panel)
        client.SetBackgroundColour('white')
        client.Draw(wxplot.PlotGraphics([plot_data], '销售趋势', '日期', '销售额'))

        # 设置属性
        client.xSpec = (list(range(len(dates))), dates)  # 设置X轴刻度和标签
        client.enableLegend = True  # 启用图例

        # 布局
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(client, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(vbox)
