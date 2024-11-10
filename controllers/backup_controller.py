# controllers/backup_controller.py

import os
import shutil
from config import DB_PATH, BACKUP_DIR
import datetime

class BackupController:
    def __init__(self):
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

    def backup_database(self):
        backup_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        backup_path = os.path.join(BACKUP_DIR, backup_filename)
        shutil.copy(DB_PATH, backup_path)
        return backup_path

    def restore_database(self, backup_file):
        if os.path.exists(backup_file):
            shutil.copy(backup_file, DB_PATH)
            return True
        else:
            return False
