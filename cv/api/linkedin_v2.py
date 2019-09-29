from linkedin_v2 import linkedin as lin

# from hackzurich.settings import LINKEDIN_ID, LINKEDIN_SECRET
LINKEDIN_ID = '779u3cu8a069wz'
LINKEDIN_SECRET = 'bcDwGS7N3GxcuiYD'

authentication = lin.LinkedInAuthentication(LINKEDIN_ID, LINKEDIN_SECRET, 'http://localhost:8080/code')

print(authentication.authorization_url)
application = lin.LinkedInApplication(authentication)
# print(authentication.get_access_token())
