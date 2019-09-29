import requests
import json


def get_info(username):
    base_url = "https://linkedin.com/voyager/api/identity/profiles/"

    url_profile_view = base_url + username + "/profileView"
    url_skill_category = base_url + username + "/skillCategory?includeHiddenEndorsers=true"
    cookies = {
        "JSESSIONID": "ajax:3728772902792983764",
        "bcookie": "v=2&5faeb745-36ac-4f24-8775-f8d6faa6c3df",
        "bscookie": "v=1&20190928193611a3645ba6-d030-4c44-8b67-14c9a1ea823eAQFZ-cD3kkDadPvlO0z6kxKDbDJkaiwy",
        "lidc": "b=VB79:g=2034:u=22:i=1569699427:t=1569703077:s=AQHLh7MFBbJzkS6Oz9YBqMS29HrL0PCe",
        "li_at": "AQEDASajj8MDkzd8AAABbXlgI6IAAAFtnWynok4AOMuMO9q35uoJj2j66Ci-0nBwQZsoj2L48RrdYdVK9ogXf67CWuIT6aAHKAsHqsPg2lzbTfJIlHxIhUKIVA-gMb6wXJK-zhd3yNESy1R1pbZFfdFN",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
        "Accept": "application/vnd.linkedin.normalized+json+2.1",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "x-li-lang": "en_US",
        "x-li-track": '{"clientVersion":"1.5.*","osName":"web","timezoneOffset":3.5,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
        "x-li-page-instance": 'urn:li:page:d_flagship3_profile_view_base;2qqHEqGiTWCJN8XjqkDFYA==',
        "csrf-token": "ajax:3728772902792983764",
        "x-restli-protocol-version": "2.0.0",
        "Referer": "https://www.linkedin.com/feed/?trk=guest_homepage-basic_sign-in-submit"
    }

    skill_text = requests.get(url_skill_category, cookies=cookies, headers=headers).text
    education_text = requests.get(url_profile_view, cookies=cookies, headers=headers).text
    skill_json = json.loads(skill_text)['included']
    profile_json = json.loads(education_text)['included']
    skills = []
    educations = []
    occupations = []
    for temp in skill_json:
        if 'name' in temp and temp['name']:
            skills.append(temp['name'])

    for temp in profile_json:
        if 'schoolName' in temp and temp['schoolName']:
            educations.append(temp['schoolName'])

    educations = list(dict.fromkeys(educations))

    ###
    for x in skill_json:
        if 'occupation' in x and x['occupation']:
            occupations.append(x['occupation'])
    for x in profile_json:
        if 'occupation' in x and x['occupation']:
            occupations.append(x['occupation'])

    occupations = list(dict.fromkeys(occupations))

    ###
    # for x in skill_json:
    #     print(x)
        # if 'occupation' in x:
        #     occupations.append(x['occupation'])
    # for x in profile_json:
    #     print(x)
        # if 'occupation' in x:
            # occupations.append(x['occupation'])

    return {"skills": skills, "educations": educations, "experiences": occupations}
