


class ApiClient:
    """
    :param auth: your auth configuration
    """

    def __init__(self, sdk_domain: str, api_token: str) -> None:
        self.sdk_domain = sdk_domain
        self.api_token = api_token        
        pass

    def get_credential(self):
        # call to server
        print("call to sdk server to get credential", self.sdk_domain, self.api_token)
        return {
            "username": "admin",
            "password": "123",
            "db": "db",
            "url": "10.10.101.234",
            "port": 5432
        }

    def check_dependency_version() -> bool:
        return True