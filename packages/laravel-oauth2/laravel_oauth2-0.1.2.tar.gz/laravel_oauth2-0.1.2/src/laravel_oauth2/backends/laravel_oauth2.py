from social_core.backends.oauth import BaseOAuth2
from django.conf import settings


class LaravelOAuth2(BaseOAuth2):
    """
    Laravel OAuth2 authentication backend
    """
    global_settings = settings.FEATURES.get("CUSTOM_OAUTH_PARAMS", {})

    name = global_settings.get("BACKEND_NAME", "laravel-oauth2")
    
    DEFAULT_SCOPE = global_settings.get("DEFAULT_SCOPE", ["api"])
    
    skip_email_verification = True
    
    def get_setting(self, param: str, default=""):
        """
        Retrieve value from Django settings. If absent, search for it in the provider's configuration.
        """
        return self.global_settings.get(param, self.setting(param)) or default

    def get_user_details(self, response):
        """Retorna os detalhes do usuário autenticado no Laravel"""
        fullname, first_name, last_name = self.get_user_names(response.get("name"))
        return {
            "username": response.get("email"),
            "email": response.get("email"),
            "fullname": fullname,
            "first_name": first_name,
            "last_name": last_name
        }
    
    def user_data(self, access_token, *args, **kwargs):
        """
        Grab user profile information from SSO.
        """

        params, headers = None, None

        if self.get_setting("USER_DATA_REQUEST_METHOD", "GET") == "GET":
            headers = {"Authorization": "Bearer {}".format(access_token)}
        else:
            params = {"access_token": access_token}

        data = self.request_access_token(
            f'{self._base_url()}{self.get_setting("USER_DATA_URL")}',
            params=params,
            headers=headers,
            method=self.get_setting("USER_DATA_REQUEST_METHOD", "GET"),
        )

        if isinstance(data, list):
            data = data[0]

        if data.get("success") and "user" in data:
            data = data["user"]
        elif "data" in data:
            data = data["data"]

        data["access_token"] = access_token
        data.pop("password", None)

        return data