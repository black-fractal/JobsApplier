import json

# ff = open('sample_skillCategory.txt', 'r')
# x = json.loads(ff.read())
# y = x['included']
# skills = []
# for z in y:
#     if 'name' in z:
#         skills.append(z['name'])
#
# print(skills)

# ff = open('sample_profileView.txt', 'r')
# x = json.loads(ff.read())
from voyager import get_info

x = get_info("kamcpp")
# y = x['included']
# y = x
# skills = []
# for z in y:
#     print(z)
    # if 'schoolName' in z:
    #     skills.append(z['schoolName'])

# skills = list(dict.fromkeys(skills))
# print(skills)
