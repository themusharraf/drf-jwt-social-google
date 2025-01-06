from urllib.parse import urljoin

import requests
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# if you want to use Authorization Code Grant, use this
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


class GoogleLoginCallback(APIView):
    def get(self, request, *args, **kwargs):
        """Accept callback request from Google OAuth screen.
        Extract code and send a POST request to Google authentication endpoint."""

        code = request.GET.get("code")

        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        token_endpoint_url = "https://oauth2.googleapis.com/token"  # Google token endpoint

        # POST so'rovini yuboring
        response = requests.post(
            url=token_endpoint_url,
            data={
                "code": code,
                "client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
                "client_secret": settings.GOOGLE_OAUTH_CLIENT_SECRET,
                "redirect_uri": settings.GOOGLE_OAUTH_CALLBACK_URL,
                "grant_type": "authorization_code",
            },
        )

        # Xom javobni tekshirish
        print(f"Response Status Code: {response.status_code}")
        # print(f"Response Content: {response.text}")  # Bu yerda xom javobni ko'rasiz

        try:
            return Response(response.json(), status=status.HTTP_200_OK)
        except ValueError:
            # Agar javob JSON bo'lmasa
            return Response(
                {"error": "Failed to decode JSON response", "details": response.text},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )



class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "pages/login.html",
            {
                "google_callback_uri": settings.GOOGLE_OAUTH_CALLBACK_URL,
                "google_client_id": settings.GOOGLE_OAUTH_CLIENT_ID,
            },
        )
