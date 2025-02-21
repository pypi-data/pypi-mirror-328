# --- render code block -----
from databloom._core.mysql_core import MysqlBase

class production_db(MysqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.credential = get_credential_from_server()
# --- render code block -----
