import requests

class OAuthProvider:
    def __init__(self, provider_name, client_id, client_secret, auth_url, token_url, user_info_url, redirect_uri, scope=None):
        """
        Initialize the OAuthProvider class.
        
        provider_name: Name of the provider 
        client_id: OAuth client ID
        client_secret: OAuth client secret
        auth_url: Provider's authorization URL
        token_url: Provider's token exchange URL
        user_info_url: Provider's user information API URL
        redirect_uri: The redirect URI after login
        scope: Scopes requested for OAuth (default is None)
        """
        self.provider_name = provider_name
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.user_info_url = user_info_url
        self.redirect_uri = redirect_uri
        self.scope = scope or "openid email profile"

    def get_auth_url(self):
        #get auth url
        return f"{self.auth_url}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={self.scope}&response_type=code"

    def get_access_token(self, code):
        #get access token.
        headers = {'Accept': 'application/json'}
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

        response = requests.post(self.token_url, headers=headers, data=data)
        response_data = response.json()

        if 'access_token' in response_data:
            return response_data['access_token']
        else:
            raise Exception(f"Failed to retrieve access token: {response_data}")

    def get_user_info(self, access_token):
        #Fetches user information from the OAuth provider's API
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.user_info_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch user info: {response.status_code}, {response.text}")