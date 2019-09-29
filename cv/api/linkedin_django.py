from linkedin_v2 import linkedin as lin


def get_auth_url():
    API_KEY_1 = '771xglr54lroll'
    API_KEY_2 = '779u3cu8a069wz'
    API_SECRET_1 = '4najxXcpYZmwVIJT'
    API_SECRET_2 = 'bcDwGS7N3GxcuiYD'
    RETURN_URL_1 = 'http://kinglife.best/api.php'
    RETURN_URL_2 = 'http://localhost:8000/code'

    authentication = lin.LinkedInAuthentication(API_KEY_2, API_SECRET_2, RETURN_URL_2, permissions=["r_liteprofile", 'r_emailaddress', 'w_member_social'])
    return authentication.authorization_url


def get_auth_access_token(code):
    API_KEY_1 = '771xglr54lroll'
    API_KEY_2 = '779u3cu8a069wz'
    API_SECRET_1 = '4najxXcpYZmwVIJT'
    API_SECRET_2 = 'bcDwGS7N3GxcuiYD'
    RETURN_URL_1 = 'http://kinglife.best/api.php'
    RETURN_URL_2 = 'http://localhost:8000/code'

    authentication = lin.LinkedInAuthentication(API_KEY_2, API_SECRET_2, RETURN_URL_2, permissions=["r_liteprofile", 'r_emailaddress', 'w_member_social'])
    authentication.authorization_code = code
    access_token = authentication.get_access_token()
    try:
        access_token = access_token[0]
    except:
        access_token = ""
    return access_token


def get_application(access_token):
    return lin.LinkedInApplication(token=access_token)
