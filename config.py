# config.py

import os

# 数据库文件路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'inventory.db')

# 备份文件路径
BACKUP_DIR = os.path.join(BASE_DIR, 'data', 'backups')

# 系统参数
SYSTEM_NAME = '进销存管理系统'

# 权限设置
ROLES = {
    'admin': '管理员',
    'purchaser': '采购员',
    'salesperson': '销售员',
    'warehouse': '仓库管理员',
    'finance': '财务人员'
}

# 加密密钥（用于备份文件加密）
ENCRYPTION_KEY = 'your-encryption-key-here'
