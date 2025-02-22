import requests
import jwt
import time
from urllib.parse import urlencode


class EizenSDK:
    def __init__(
        self,
        username: str,
        password: str,
        base_url: str = "https://backend.eizen.ai/analytics/v1",
        keycloak_base_url: str = "https://keycloak.analytics.eizen.ai",
        client_id: str = "analytics-service",
    ):
        self.username = username
        self.__password = password
        self.base_url = base_url
        self.keycloak_base_url = keycloak_base_url
        self.client_id = client_id
        self.__tenant_id = None
        self.__access_token = None
        self.__refresh_token = None
        self.__fetch_new_tokens()  # Fetch tokens on initialization
        self.__get_tenant_id()

    def __fetch_new_tokens(self):
        """Fetch a new access and refresh token using username & password."""
        url = f"{self.keycloak_base_url}/realms/Analytics/protocol/openid-connect/token"
        data = {
            "grant_type": "password",
            "client_id": self.client_id,
            "username": self.username,
            "password": self.__password,
        }

        response = requests.post(
            url,
            data=urlencode(data),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code == 200:
            tokens = response.json()
            self.__access_token = tokens["access_token"]
            self.__refresh_token = tokens["refresh_token"]
        else:
            raise Exception(f"Failed to retrieve tokens: {response.text}")

    def __refresh_access_token(self):
        """Refresh the access token using the refresh token."""
        if not self.__refresh_token or self.__is_token_expired(self.__refresh_token):
            self.__fetch_new_tokens()  # If refresh token expired, get new tokens
            return

        url = f"{self.keycloak_base_url}/realms/Analytics/protocol/openid-connect/token"
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": self.__refresh_token,
        }

        response = requests.post(
            url,
            data=urlencode(data),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        if response.status_code == 200:
            tokens = response.json()
            self.__access_token = tokens["access_token"]
            self.__refresh_token = tokens.get("refresh_token", self.__refresh_token)
        else:
            self.__fetch_new_tokens()  # If refresh fails, fetch new tokens

    def __is_token_expired(self, token: str) -> bool:
        """Check if a JWT token is expired."""
        try:
            payload = jwt.decode(token, options={"verify_signature": False})
            return payload["exp"] < time.time()
        except Exception:
            return True  # If token is invalid, assume expired

    def __make_request(self, method: str, url: str, **kwargs):
        """Handles API requests and refreshes token if needed."""
        if self.__is_token_expired(self.__access_token):
            self.__refresh_access_token()

        headers = kwargs.get("headers", {})
        headers["Authorization"] = f"Bearer {self.__access_token}"
        kwargs["headers"] = headers

        response = requests.request(method, url, **kwargs)

        if response.status_code == 401:
            self.__refresh_access_token()
            headers["Authorization"] = f"Bearer {self.__access_token}"
            response = requests.request(method, url, **kwargs)

        if response.status_code != 200:
            raise Exception(f"Request failed ({response.status_code}): {response.text}")

        return response.json()

    def __get_tenant_id(self):
        url = f"{self.base_url}/user"
        self.__tenant_id = self.__make_request(
            "GET", url, params={"email": self.username}
        )["tenantId"]

    def get_analytics(self):
        url = f"{self.base_url}/analytics/tenant/{self.__tenant_id}"
        analytics = self.__make_request("GET", url)
        return [{"id": i["id"], "name": i["name"]} for i in analytics]

    def get_analytic_zones(self, analytic_id: int):
        url = f"{self.base_url}/zone/analytics/{analytic_id}"
        zones = self.__make_request("GET", url)
        return [{"id": i["id"], "name": i["name"]} for i in zones]

    def get_zone_sources(self, zone_id: int):
        url = f"{self.base_url}/source/zone/{zone_id}"
        sources = self.__make_request("GET", url)
        return [{"id": i["id"], "name": i["name"]} for i in sources]

    def get_analytic_sources(self, analytic_id: int):
        url = f"{self.base_url}/source/analytics/{analytic_id}"
        sources = self.__make_request("GET", url)
        return [{"id": i["id"], "name": i["name"]} for i in sources["sources"]]

    def get_source_details(self, source_id: int):
        url = f"{self.base_url}/source/{source_id}"
        return self.__make_request("GET", url)

    def get_source_summary(self, source_id: int):
        url = f"{self.base_url}/videos/summary/{source_id}"
        return self.__make_request("GET", url)
