import os 
import requests
from django.shortcuts import redirect
from django.http import JsonResponse
from drf_keycloak_auth.authentication import (
    KeycloakSessionAuthentication,
)
from drf_keycloak_auth.keycloak import get_keycloak_openid

import logging

log = logging.getLogger("LoginRequiredMiddleware")


class LoginRequiredMiddleware:
    """Middleware that forces authentication using DRF authentication"""

    def __init__(self, get_response):
        self.get_response = get_response
        self.authenticator = KeycloakSessionAuthentication()  # Use DRF authentication
        self.keycloak_openid = get_keycloak_openid()  # Initialize KeycloakOpenID

    def __call__(self, request):

        if "text/html" in request.headers.get("Accept", "").lower():
            code = request.GET.get("code")
            base_url = f"{request.scheme}://{request.get_host()}"

            if not code:
                login_url = self.keycloak_openid.auth_url(redirect_uri=base_url)
                return redirect(login_url)

            # If code exists, exchange it for the tokens
            try:
                # Exchange code for tokens

                token_url = os.path.join(
                    f"{self.keycloak_openid.connection.base_url}",
                    "realms",
                    f"{self.keycloak_openid.realm_name}",
                    "protocol/openid-connect/token"
                )

                response = requests.post(
                    token_url,
                    data={
                        "client_id": self.keycloak_openid.client_id,
                        "client_secret": self.keycloak_openid.client_secret_key,
                        "code": code,
                        "grant_type": "authorization_code",
                        "redirect_uri": base_url,
                    },
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json",
                    },
                )

                if response.status_code == 200:
                    tokens = response.json()
                    access_token = tokens.get("access_token")

                    # Optionally, use the access token to authenticate the user
                    user = self.authenticator.authenticate_credentials(
                        access_token
                    )
                    request.user = user  # Assign authenticated user to request object

                else:
                    raise Exception(
                        f"Failed to get tokens from Keycloak: {response.text}"
                    )

            except Exception as e:
                log.error(f"Error during authentication: {str(e)}")  # Log any errors
                return JsonResponse({"error": "Authentication failed"}, status=401)

        # Continue with the request handling
        response = self.get_response(request)
        return response
