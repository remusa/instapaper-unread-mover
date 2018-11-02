import csv
import json
import os
import urllib
import requests

from urllib.parse import urlparse
from urllib.request import urlopen

import oauth2 as oauth

""""
artofmanliness
austinkleon
calnewport
elsyreyes
fourhourworkweek
freecodecamp
jamesaltucher
lifehacker
marksdailyapple
scotthyoung
youarenotsosmart
"""

file_original = "instapaper-export.csv"
filter_term = "fourhourworkweek"
filter_folder = "Unread"
file_input = "input.csv"
file_output = "output-" + filter_folder + "-" + filter_term + ".csv"

INSTAPAPER_KEY = os.getenv('INSTAPAPER_KEY', '0c8a0f75bf004e94bbac21250ad9a78d')  # os.environ.get
INSTAPAPER_SECRET = os.getenv('INSTAPAPER_SECRET', '3f1fd91ee19f4ffaaa7f7c3069d8c8c1')
INSTAPAPER_LOGIN = os.getenv('INSTAPAPER_LOGIN', 'rene.msx@gmail.com')
INSTAPAPER_PASSWORD = os.getenv('INSTAPAPER_PASSWORD', '^bRtcyt%!82R&54^jpXi')


def remove_not_unread():
    with open(file_original, "r", newline="", encoding="utf8") as fin, open(file_input, "w", newline="",
                                                                            encoding="utf8") as fout:

        reader = csv.reader(fin, delimiter=",")
        writer = csv.writer(fout, delimiter=",", quotechar="'")

        for row in reader:
            try:
                for i in row:
                    if i == filter_folder:
                        writer.writerow(row)

            except IndexError:
                print("Error: ", row)


def filter_unread():
    with open(file_input, "r", newline="", encoding="utf8") as fin, open(file_output, "w", newline="",
                                                                         encoding="utf8") as fout:

        reader = csv.reader(fin, delimiter=" ")
        writer = csv.writer(fout, delimiter=" ", quotechar="|")

        for row in reader:
            try:
                if filter_term in row[0]:
                    writer.writerow(row)

            except IndexError:
                print("Error: ", row)


def test():
    consumer_key = INSTAPAPER_KEY
    consumer_secret = INSTAPAPER_SECRET

    access_token_url = 'https://www.instapaper.com/api/1/oauth/access_token'

    consumer = oauth.Consumer(consumer_key, consumer_secret)
    client = oauth.Client(consumer)

    params = {"x_auth_username": INSTAPAPER_LOGIN, "x_auth_password": INSTAPAPER_PASSWORD, "x_auth_mode": 'client_auth'}

    client.set_signature_method = oauth.SignatureMethod_HMAC_SHA1()
    resp, token = client.request(access_token_url, method="POST", body=urllib.parse.urlencode(params))
    access_token = dict(urllib.parse.parse_qsl(token))
    print(access_token)

    url = "https://www.instapaper.com/api/1/bookmarks/list"
    r = requests.get(url)
    print(json.loads(r.content))


def main():
    # remove_not_unread()
    # filter_unread()
    test()


if __name__ == '__main__':
    main()

main()
