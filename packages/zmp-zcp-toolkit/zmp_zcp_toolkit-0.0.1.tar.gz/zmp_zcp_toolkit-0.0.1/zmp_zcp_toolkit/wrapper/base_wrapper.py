from enum import Enum
import logging
import os

from httpx import AsyncClient, BasicAuth, Client

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

_TIMEOUT = os.getenv("HTTPX_DEFAULT_TIMEOUT", 10)


class AuthenticationType(str, Enum):
    """Authentication type model"""

    NONE = "None"
    BASIC = "Basic"
    BEARER = "Bearer"


class BaseAPIWrapper:
    def __init__(
        self,
        server: str,
        /,
        *,
        headers: dict | None = None,
        cookies: dict | None = None,
        auth_type: AuthenticationType | None = AuthenticationType.NONE,
        username: str | None = None,
        password: str | None = None,
        bearer_token: str | None = None,
        tls_verify: bool | None = False,
        timeout: int | None = _TIMEOUT,
    ):
        self._server = server
        self._headers = headers if headers is not None else {}
        self._cookies = cookies if cookies is not None else {}
        self._auth_type = auth_type
        self._username = username
        self._password = password
        self._bearer_token = bearer_token
        self._tls_verify = tls_verify
        self._timeout = timeout

        self._auth = None
        if auth_type == AuthenticationType.BASIC:
            if not username or not password:
                raise ValueError(
                    "Username and password are required for Basic authentication"
                )
            self._auth = BasicAuth(username=username, password=password)
        elif auth_type == AuthenticationType.BEARER:
            if not bearer_token:
                raise ValueError("Bearer token is required for Bearer authentication")

        if self._headers.get("Content-Type") is None:
            self._headers.update({"Content-Type": "application/json"})

        if (
            self._auth_type == AuthenticationType.BEARER
            and self._bearer_token is not None
        ):
            self._headers.update({"Authorization": f"Bearer {self._bearer_token}"})

    @property
    def async_client(self) -> AsyncClient:
        return AsyncClient(
            auth=self._auth,
            base_url=self._server,
            headers=self._headers,
            cookies=self._cookies,
            verify=self._tls_verify,
            timeout=self._timeout,
        )

    @property
    def client(self) -> Client:
        return Client(
            auth=self._auth,
            base_url=self._server,
            headers=self._headers,
            cookies=self._cookies,
            verify=self._tls_verify,
            timeout=self._timeout,
        )
