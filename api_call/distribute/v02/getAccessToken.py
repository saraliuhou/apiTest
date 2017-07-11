# -*- coding: utf-8 -*-
from cof.http import Http
import requests
import json

class GetAccessToken(Http):
    def getAdminToken(self, username):
        body = {

        }
        response = self.post("/api/v1/oauth/token", body)
        return response

    def getUserToken(self, phone):
        body = {

        }
        response = self.post("/api/v1/oauth/token", body)
        return response



if __name__ == "__main__":
    GetAccessToken = GetAccessToken()
    response = GetAccessToken.getUserToken("88889876123")
    print(json.loads(response['data'])['access_token'])