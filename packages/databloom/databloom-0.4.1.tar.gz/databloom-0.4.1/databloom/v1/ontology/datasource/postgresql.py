import databloom._dynamic.source.postgresql as db
from databloom._core import ApiClient 

class Postgres:
    """
    data source type is mysql
    """
    def __init__(self, sdk_domain: str, api_token: str) -> None:
        self.api_client = ApiClient(sdk_domain, api_token)

        ## ----render code block-----
        self.palantir = db.palantir2(self.__get_credential_from_sdk)
        ## ----render code block----
    
    def __get_credential_from_sdk(self):
        # call sdk api server here
        credential_info = self.api_client.get_credential()
        print("credential_info", credential_info)
        return credential_info