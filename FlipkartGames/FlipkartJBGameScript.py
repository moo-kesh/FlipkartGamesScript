import requests
import time

secure_cookie_fetch = ''
ff_current_day_uri = ''
list_of_ids = ['SP-GFMyd-1604071867909',
               'cfbb204716f372571b327681b5b9d809',
               'sZhT51d8XEeB8kHuDH4gCRfb4Zz6Z29o4bFMaspjEVkvIVyrELonaqdEXpH2C0GlULHXvjfABb98PIoJ/FtheQ==',
               'd1t13Pz8iPz8/dz8/Pz8/cHUYbwb+32BYK9fMqWooU4Zx872iQlpYh3Y0CDi2o06Ti9d7v4xgimF3RaenEahdGHJ08w==',
               'x4wuP7iUNL',
               'VIC08BA71AB3B3473FA508E85F35C4EF47.TOKFF9625F0D4BE4CE1BA1F19BB20F57B28.1604082563.LI',
               '551iX4p5i-MlPNEG4nJFgjTDcJu2NpM6o3v1ahmOtuQcRTvHeYkVjaT1VCalRbdR96oTMZ0S01DXtlZhaVtKBQ==']

# list_of_ids = ['SP-GFMyd-1604071867909', 'cfbb204716f372571b327681b5b9d809', 'sZhT51d8XEeB8kHuDH4gCRfb4Zz6Z29o4bFMaspjEVkvIVyrELonaqdEXpH2C0GlULHXvjfABb98PIoJ/FtheQ==',
#                'd1t13Pz8iPz8/dz8/Pz8/cHUYbwb+32BYK9fMqWooU4Zx872iQlpYh3Y0CDi2o06Ti9d7v4xgimF3RaenEahdGHJ08w==', 'x4wuP7iUNL', 'VIC08BA71AB3B3473FA508E85F35C4EF47.TOKFF9625F0D4BE4CE1BA1F19BB20F57B28.1604082563.LI', '551iX4p5i-MlPNEG4nJFgjTDcJu2NpM6o3v1ahmOtuQcRTvHeYkVjaT1VCalRbdR96oTMZ0S01DXtlZhaVtKBQ==']


print(list_of_ids)


def game_init(visitid, secure_token, sn, secure_cookie, campaignid, txnid):
    burp0_url = "https://2.rome.api.flipkart.net:443/1/games/platform/gameInit"
    burp0_headers = {"Content-Type": "application/json", "Connection": "Keep-Alive", "User-Agent": "okhttp/3.14.4",
                     "X-Visit-Id": "{}".format(visitid) + "-" + str(int(time.time() * 1000)),
                     "secureToken": "{}".format(secure_token),
                     "X-User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; T5524 Build/OPM7.181205.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.125 Mobile Safari/537.36 FKUA/Retail/1190707/Android/Mobile (Smartron/T5524/" + "{}".format(
                         visitid) + ")",
                     "sn": "{}".format(sn),
                     "Accept-Encoding": "gzip",
                     "secureCookie": "{}".format(secure_cookie)}
    burp0_json = {"campaignId": "{}".format(campaignid), "txnId": "{}".format(txnid)}
    result = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    if result.status_code == 200:
        global secure_cookie_fetch
        secure_cookie_fetch = result.headers.get('secureCookie')
        return True
    else:
        return False


def game_start(campaignid, tokenid):
    game_start_url = "https://2.games3p.api.flipkart.net:443/games-external-jumpjump/GameStart"
    game_start_headers = {"Content-Type": "application/json", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                          "User-Agent": "okhttp/3.14.4"}
    game_start_json = {"campaignId": "{}".format(campaignid),
                       "tokenId": "{}".format(tokenid),
                       "retryAttemptNumber": 0}
    result = requests.post(game_start_url, headers=game_start_headers, json=game_start_json)

    if result.status_code == 200:
        print("ok")
        return True
    else:
        return False


def game_complete(campaignid, tokenid):
    gc_url = "https://2.games3p.api.flipkart.net:443/games-external-jumpjump/GameComplete"
    gc_headers = {"Content-Type": "application/json", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                  "User-Agent": "okhttp/3.14.4"}
    gc_json = {"campaignId": "{}".format(campaignid),
               "tokenId": "{}".format(tokenid),
               "retryAttemptNumber": 0,
               "score": 212, "timeSpent": 232.125,
               }
    result = requests.post(gc_url, headers=gc_headers, json=gc_json)
    if result.status_code == 200:
        json = result.json()
        global ff_current_day_uri
        ff_current_day_uri = json["responseData"]["mysteryBox"]["landingUrl"]["originalUrl"]
        return True
    else:
        return False


def fetch_rewards(visitid, secure_token, sn):
    fr_url = "https://2.rome.api.flipkart.net:443/4/page/fetch"
    fr_headers = {"Content-Type": "application/json", "Connection": "Keep-Alive", "User-Agent": "okhttp/3.14.4",
                  "X-Visit-Id": "{}".format(visitid) + "-" + str(int(time.time() * 1000)),
                  "secureToken": "{}".format(secure_token),
                  "X-User-Agent": "Mozilla/5.0 (Linux; Android 10; Nokia 6.1 Build/QQ3A.200805.001) FKUA/Retail/1190707/Android/Mobile (HMD Global/Nokia 6.1/{}".format(
                      visitid),
                  "sn": "{}".format(sn),
                  "Accept-Encoding": "gzip",
                  "secureCookie": "{}".format(secure_cookie_fetch)}
    fr_json = {"locationContext": None,
               "pageContext": {"fetchAllPages": False, "fetchSeoData": False, "networkSpeed": 212,
                               "pageHashKey": None, "pageNumber": 1, "paginatedFetch": False,
                               "paginationContextMap": None, "slotContextMap": None, "trackingContext": None},
               "pageUri": "{}".format(ff_current_day_uri), "requestContext": None}
    result = requests.post(fr_url, headers=fr_headers, json=fr_json)
    if result.status_code == 200:
        return True
    else:
        False


print('Initialising Game........')
if game_init(list_of_ids[1], list_of_ids[2], list_of_ids[5], list_of_ids[3], list_of_ids[0], list_of_ids[4]):
    print('Game Successfully initialised !')
    time.sleep(5)
    if game_start(list_of_ids[0], list_of_ids[6]):
        print('Game has been Started !')
        time.sleep(5)
        if game_complete(list_of_ids[0], list_of_ids[6]):
            print('Game successfully completed !')
            print('Fetching your rewards.........')
            time.sleep(5)
            if fetch_rewards(list_of_ids[1], list_of_ids[2], list_of_ids[5]):
                print('Reward successfully added your account.')
                print('Open Flipkart App to ckeck your Rewards')
            else:
                print('Failed to fetch rewards!')
                print('Unexpected Error!')
        else:
            print('Failed!')
    else:
        print('Operation Failed !')
else:
    print('oops something went wrong !')
