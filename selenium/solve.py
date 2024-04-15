# https://github.com/2captcha/2captcha-python

import sys
import os
from twocaptcha import TwoCaptcha
def solveRecaptcha(sitekey,url):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('APIKEY_2CAPTCHA', 'e77869c49f2583851b523d97db8029ef')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print("ERROR",e)

    else:
        return result