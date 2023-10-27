from .base import BaseModel


class MyPlex(BaseModel):
    def __init__(
        self,
        authToken: str = None,
        username: str = None,
        mappingState: str = None,
        mappingError: str = None,
        signInState: str = None,
        publicAddress: str = None,
        publicPort: float = None,
        privateAddress: str = None,
        privatePort: float = None,
        subscriptionFeatures: str = None,
        subscriptionActive: bool = None,
        subscriptionState: str = None,
        **kwargs,
    ):
        """
        Initialize MyPlex
        Parameters:
        ----------
            authToken: str
            username: str
            mappingState: str
            mappingError: str
            signInState: str
            publicAddress: str
            publicPort: float
            privateAddress: str
            privatePort: float
            subscriptionFeatures: str
            subscriptionActive: bool
            subscriptionState: str
        """
        if authToken is not None:
            self.authToken = authToken
        if username is not None:
            self.username = username
        if mappingState is not None:
            self.mappingState = mappingState
        if mappingError is not None:
            self.mappingError = mappingError
        if signInState is not None:
            self.signInState = signInState
        if publicAddress is not None:
            self.publicAddress = publicAddress
        if publicPort is not None:
            self.publicPort = publicPort
        if privateAddress is not None:
            self.privateAddress = privateAddress
        if privatePort is not None:
            self.privatePort = privatePort
        if subscriptionFeatures is not None:
            self.subscriptionFeatures = subscriptionFeatures
        if subscriptionActive is not None:
            self.subscriptionActive = subscriptionActive
        if subscriptionState is not None:
            self.subscriptionState = subscriptionState


class GetMyPlexAccountResponse(BaseModel):
    def __init__(self, MyPlex: MyPlex = None, **kwargs):
        """
        Initialize GetMyPlexAccountResponse
        Parameters:
        ----------
            MyPlex: MyPlex
        """
        if MyPlex is not None:
            self.MyPlex = MyPlex
