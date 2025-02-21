# --- render code block -----
from databloom._core.postgres_core import PostgresqlBase

class palantir2(PostgresqlBase):
    def __init__(self, get_credential_from_server) -> None:
        self.credential = get_credential_from_server()
# --- render code block -----
