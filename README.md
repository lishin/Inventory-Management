# Inventory-Management
### 项目名称：**进销存管理系统**

### 项目概述：
该项目是一个基于 **Python** 和 **wxPython** 的桌面应用程序，用于管理企业的进货、销售和库存。其核心功能包括用户管理、商品管理、供应商管理、库存管理、销售报表等。系统适用于中小型企业，用于优化库存和供应链管理。

---

### 功能模块：

#### 1. **用户管理**
- 提供多角色支持：管理员、采购员、销售员、仓库管理员、财务人员。
- 支持用户登录、权限管理。
- 记录用户的登录历史。

#### 2. **商品管理**
- 增删改查商品信息，包括类别、规格、库存、价格等。
- 支持商品的附件（PDF/TXT）管理，方便记录商品说明或技术文档。

#### 3. **供应商管理**
- 增删改查供应商信息。
- 每个供应商可以关联多个商品，形成一对多关系。
- 提供供应商的商品供货明细。

#### 4. **库存管理**
- 实时监控库存状态。
- 支持库存调拨、盘点、调整。
- 提供库存预警功能，设置安全库存。

#### 5. **销售管理**
- 记录销售订单，支持销售退货。
- 生成销售趋势报表，分析销售数据。

#### 6. **报表管理**
- **销售报表**：按时间段显示销售趋势。
- **库存报表**：显示商品的当前库存状态。
- **供应商供货报表**：分析各供应商的商品供货情况。
- 支持报表导出功能（CSV/Excel）。

#### 7. **数据备份与恢复**
- 手动或自动备份数据库，保证数据安全。
- 支持从备份文件恢复数据。

---

### 技术实现：

#### 1. **开发工具**
- **语言**：Python
- **图形界面**：wxPython
- **数据库**：SQLite
- **图表绘制**：wx.lib.plot

#### 2. **项目架构**
- **MVC架构**：分离数据、逻辑和界面层。
  - **Model（数据层）**：处理与数据库的交互，包括用户、商品、供应商等数据模型。
  - **View（视图层）**：基于 wxPython 的图形界面，供用户交互。
  - **Controller（控制层）**：处理业务逻辑，例如用户登录验证、数据关联。

#### 3. **数据结构**
- 用户表（`users`）：存储用户信息和权限。
- 商品表（`products`）：存储商品信息。
- 供应商表（`suppliers`）：存储供应商信息。
- 供应商与商品关系表（`supplier_products`）：管理供应商与商品的关系。
- 销售记录表（`sales`）：记录销售订单信息。

---

### 项目特点：
1. **用户友好**：通过简洁直观的 GUI，用户可以快速访问系统功能。
2. **模块化设计**：便于扩展和维护，可以灵活增加新功能。
3. **数据安全**：支持数据备份与恢复，保障数据可靠性。
4. **报表丰富**：多维度数据分析，帮助企业做出数据驱动的决策。
5. **附件支持**：可为商品添加技术文档或说明文件，便于参考。

---

### 使用场景：
1. **中小型企业**：适合批发、零售、生产等行业，管理库存、供应商和销售。
2. **实验室或研究机构**：用于管理实验材料、设备和供应商。
3. **物流与仓储公司**：管理货物库存及供销流程。

---

### 未来扩展：
1. **多用户联网版**：支持网络同步，适用于多终端环境。
2. **移动应用支持**：开发移动端应用，实现随时随地访问。
3. **外部接口集成**：与 ERP、财务软件对接，实现数据同步。
4. **多语言支持**：为国际化用户提供更好的使用体验。
5. **高级分析功能**：通过数据挖掘和机器学习，提供更深入的业务洞察。

---

