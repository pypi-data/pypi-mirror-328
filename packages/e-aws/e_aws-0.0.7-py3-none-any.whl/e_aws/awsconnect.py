from typing import Any
from .awslambda import AWSLambda
from .awsbucket import AWSBucket
from .awssession import AWSSession


class AWSConnect(AWSSession):

    def __init__(self, access_key_id: str = None, secret_access_key: str = None, region: str = None):
        super().__init__(access_key_id, secret_access_key, region)
        self.session = self.session()

    def lambdaF(self, function_name: str, **extra_kwargs: dict[str, Any]) -> AWSLambda:
        """
        Access to lambda functions.

        :param function_name: str
        :param extra_kwargs: additional arguments
        """
        return AWSLambda(function_name, **extra_kwargs).set_session(self.session)

    def bucket(self, name: str, **extra_kwargs: dict[str, Any]) -> AWSBucket:
        """
        Access to bucket

        :param name: str
        :param extra_kwargs: additional arguments
        """
        return AWSBucket(name, **extra_kwargs).set_session(self.session)

    def __enter__(self) -> 'AWSConnect':
        return self

    def __exit__(self, *_):
        pass

if __name__ == "__main__":
    with AWSConnect() as aws:
        aws.bucket('test').get_object("test.pdf")
