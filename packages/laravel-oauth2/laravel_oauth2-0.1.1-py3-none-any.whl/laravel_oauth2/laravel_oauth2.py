from social_core.backends.oauth import BaseOAuth2


class LaravelOAuth2(BaseOAuth2):
    """Laravel OAuth2 authentication backend"""
    name = "laravel"
    
    # URLs do seu servidor Laravel com Passport
    AUTHORIZATION_URL = "https://adm-dev.ciadeestagios.com.br/oauth/authorize"
    ACCESS_TOKEN_URL = "https://adm-dev.ciadeestagios.com.br/oauth/token"
    USER_DATA_URL = "https://adm-dev.ciadeestagios.com.br/api/user"  # Endpoint para obter os dados do usuário autenticado
    
    ACCESS_TOKEN_METHOD = "POST"
    SCOPE_SEPARATOR = ","
    DEFAULT_SCOPE = ["*"]  # Defina os escopos necessários

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
        """Obtém os dados do usuário no Laravel"""
        return self.get_json(self.USER_DATA_URL, headers={
            "Authorization": f"Bearer {access_token}"
        })
