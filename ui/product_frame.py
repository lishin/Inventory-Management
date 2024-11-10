# ui/product_frame.py

import wx
from models.product_model import ProductModel
from utils.helpers import show_message

class ProductFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='商品管理', size=(600, 400))
        panel = wx.Panel(self)

        # 商品列表
        self.product_list = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.product_list.InsertColumn(0, 'ID', width=50)
        self.product_list.InsertColumn(1, '名称', width=150)
        self.product_list.InsertColumn(2, '类别', width=100)
        self.product_list.InsertColumn(3, '规格', width=100)
        self.product_list.InsertColumn(4, '单位', width=80)
        self.product_list.InsertColumn(5, '价格', width=80)
        self.product_list.InsertColumn(6, '库存', width=80)

        # 加载商品数据
        self.load_products()

        # 按钮
        add_btn = wx.Button(panel, label='新增')
        edit_btn = wx.Button(panel, label='编辑')
        delete_btn = wx.Button(panel, label='删除')

        add_btn.Bind(wx.EVT_BUTTON, self.on_add)
        edit_btn.Bind(wx.EVT_BUTTON, self.on_edit)
        delete_btn.Bind(wx.EVT_BUTTON, self.on_delete)

        # 布局
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(add_btn, flag=wx.RIGHT, border=10)
        hbox.Add(edit_btn, flag=wx.RIGHT, border=10)
        hbox.Add(delete_btn)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.product_list, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

    def load_products(self):
        self.product_list.DeleteAllItems()
        product_model = ProductModel()
        products = product_model.get_all_products()
        for product in products:
            index = self.product_list.InsertItem(self.product_list.GetItemCount(), str(product[0]))
            self.product_list.SetItem(index, 1, product[1])
            self.product_list.SetItem(index, 2, product[2] if product[2] else "")
            self.product_list.SetItem(index, 3, product[3] if product[3] else "")
            self.product_list.SetItem(index, 4, product[4] if product[4] else "")
            self.product_list.SetItem(index, 5, str(product[5]))
            self.product_list.SetItem(index, 6, str(product[6]))
        product_model.close()

    def on_add(self, event):
        dlg = ProductDialog(self, "新增商品")
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.get_data()
            product_model = ProductModel()
            product_model.add_product(**data)
            product_model.close()
            self.load_products()
            show_message('新增成功！')
        dlg.Destroy()

    def on_edit(self, event):
        selected = self.product_list.GetFirstSelected()
        if selected == -1:
            show_message('请先选择一个商品。', '提示', wx.OK | wx.ICON_WARNING)
            return
        product_id = int(self.product_list.GetItemText(selected))
        product = {
            'product_id': product_id,
            'name': self.product_list.GetItem(selected, 1).GetText(),
            'category': self.product_list.GetItem(selected, 2).GetText(),
            'specification': self.product_list.GetItem(selected, 3).GetText(),
            'unit': self.product_list.GetItem(selected, 4).GetText(),
            'price': float(self.product_list.GetItem(selected, 5).GetText()),
            'stock_quantity': int(self.product_list.GetItem(selected, 6).GetText())
        }

        dlg = ProductDialog(self, "编辑商品", product)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.get_data()
            product_model = ProductModel()
            product_model.update_product(product_id, **data)
            product_model.close()
            self.load_products()
            show_message('编辑成功！')
        dlg.Destroy()

    def on_delete(self, event):
        selected = self.product_list.GetFirstSelected()
        if selected == -1:
            show_message('请先选择一个商品。', '提示', wx.OK | wx.ICON_WARNING)
            return
        product_id = int(self.product_list.GetItemText(selected))
        confirm = wx.MessageBox(f'确定要删除商品 ID {product_id} 吗？', '确认删除',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if confirm == wx.YES:
            product_model = ProductModel()
            product_model.delete_product(product_id)
            product_model.close()
            self.load_products()
            show_message('删除成功！')

class ProductDialog(wx.Dialog):
    def __init__(self, parent, title, product=None):
        super().__init__(parent, title=title, size=(350, 400))
        self.product = product
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # 名称
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='名称：')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.name_tc = wx.TextCtrl(panel)
        hbox1.Add(self.name_tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 类别
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='类别：')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.category_tc = wx.TextCtrl(panel)
        hbox2.Add(self.category_tc, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 规格
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='规格：')
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        self.specification_tc = wx.TextCtrl(panel)
        hbox3.Add(self.specification_tc, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 单位
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='单位：')
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        self.unit_tc = wx.TextCtrl(panel)
        hbox4.Add(self.unit_tc, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 价格
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st5 = wx.StaticText(panel, label='价格：')
        hbox5.Add(st5, flag=wx.RIGHT, border=8)
        self.price_tc = wx.TextCtrl(panel)
        hbox5.Add(self.price_tc, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 库存
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st6 = wx.StaticText(panel, label='库存：')
        hbox6.Add(st6, flag=wx.RIGHT, border=8)
        self.stock_tc = wx.TextCtrl(panel)
        hbox6.Add(self.stock_tc, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # 按钮
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        ok_btn = wx.Button(panel, label='确定', id=wx.ID_OK)
        close_btn = wx.Button(panel, label='取消', id=wx.ID_CANCEL)
        hbox7.Add(ok_btn)
        hbox7.Add(close_btn, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox7, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        if self.product:
            self.name_tc.SetValue(self.product['name'])
            self.category_tc.SetValue(self.product['category'])
            self.specification_tc.SetValue(self.product['specification'])
            self.unit_tc.SetValue(self.product['unit'])
            self.price_tc.SetValue(str(self.product['price']))
            self.stock_tc.SetValue(str(self.product['stock_quantity']))

    def get_data(self):
        return {
            'name': self.name_tc.GetValue(),
            'category': self.category_tc.GetValue(),
            'specification': self.specification_tc.GetValue(),
            'unit': self.unit_tc.GetValue(),
            'price': float(self.price_tc.GetValue()) if self.price_tc.GetValue() else 0.0,
            'stock_quantity': int(self.stock_tc.GetValue()) if self.stock_tc.GetValue() else 0
        }
