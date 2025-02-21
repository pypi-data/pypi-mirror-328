import os

from sais.autotrain.dataservice.config.const import NOTIFY_AUTH_TOKEN


class EnvVarCredentialsProvider:
    def __init__(self):
        self.token = self.__get_credentials()

    def __get_credentials(self):
        bearer_token = os.getenv(NOTIFY_AUTH_TOKEN)
        # 暂时注掉，不强制认证
        # if not bearer_token:
        #     raise ValueError(f'{NOTIFY_AUTH_TOKEN} should not be null or empty.')
        return f'Bearer {bearer_token}'
