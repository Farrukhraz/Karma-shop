from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse, urlencode

import requests
from social_core.exceptions import AuthForbidden


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != "vk-oauth2":
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]
    print(data)

    user_profile = user.shopuserprofile

    sex = data['sex']
    if sex:
        user_profile.gender = user_profile.MALE if sex == 2 else user_profile.FEMALE

    bdate = data['bdate']
    if bdate:
        date_format = '%d.%m.%Y'
        try:
            converted_bdate = datetime.strptime(bdate, date_format)
            user_age = datetime.now().year - converted_bdate.year
        except ValueError:
            # user has hidden his age
            user_age = None

        if user_age is None or user_age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        else:
            user.age = user_age

    about_user = data['about']
    if about_user:
        user_profile.about_me = about_user

    user.save()
