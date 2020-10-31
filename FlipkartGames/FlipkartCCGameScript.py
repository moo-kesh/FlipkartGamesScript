import requests
import time
import random

stage = 1
list_of_ids = []
score_list = [3010.5000493050054, 6010.2000493050054, 10210.6000493050054, 14985.3000493050085, 19854.400048325057,
              26147.902048325027, 36458.29004930900227, 45256.17004930900218, 56215.23004930900211,
              72245.10004930900289,
              87215.11104930900730, 101258.27004930900227, 121458.17304930900159, 135269.14704930900367,
              152359.25804930900110, 174256.14504930900753]

list_of_ids.append('arcade-crazy_cannon-campaign-1603792367130')
list_of_ids.append(input('Enter TokenId : ')+'-'+str(int(time.time()*1000)))
list_of_ids.append(input('Enter Device Id : '))


def start_game(level, device_id, token_id, campaign_id):
    url = "https://2.games.flipkart.net:443/app/1/game/CCArcade/ccGamePlay"
    headers = {"Content-Type": "application/json", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
               "User-Agent": "okhttp/3.14.4"}
    json = {"campaignId": "{}".format(campaign_id), "campaignType": "SIMULTANEOUS_CRAZY_CANNON",
            "gameName": "ARCADE_CRAZY_CANNON", "gameType": "CRAZY_CANNON",
            "gunValue": {"gunFirePower": 6.900000095367432, "gunSpeed": 23}, "league": "BRONZE",
            "retryAttemptNumber": 0, "stage": level,
            "userContext": {"channel": "ANDROID", "deviceId": "{}".format(device_id),
                            "tokenId": "{}".format(token_id)}}

    result_of_request = requests.post(url, headers=headers, json=json)

    if result_of_request.status_code == 200:
        return True
    elif result_of_request.status_code == 400:
        print("Something went wrong !")
        print("Please check input details again")
        return False
    else:
        print("Unknown Error")
        return False


def submit_score(level, deviceid, tokenid, campaignid, score):
    url2 = "https://2.games.flipkart.net:443/app/1/game/CCArcade/ccStageSummary"
    headers2 = {"Content-Type": "application/json", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.14.4"}
    json2 = {"campaignId": "{}".format(campaignid),
             "campaignType": "SIMULTANEOUS_CRAZY_CANNON", "gameName": "ARCADE_CRAZY_CANNON",
             "gameType": "CRAZY_CANNON", "gunValue": {"gunFirePower": 6.900000095367432, "gunSpeed": 23},
             "league": "BRONZE", "retryAttemptNumber": 0, "score": score, "stage": level,
             "stageCompleted": True,
             "userContext": {"channel": "ANDROID", "deviceId": "{}".format(deviceid),
                             "tokenId": "{}".format(tokenid)}}
    result_of_submit_score = requests.post(url2, headers=headers2, json=json2)

    if result_of_submit_score.status_code == 200:
        result_json = result_of_submit_score.json()
        print('Level {} completed'.format(level))
        print("Gems Earned : ", result_json["gemsSection"]["gemsEarned"])
        print("Total Gems : ", result_json["gemsSection"]["gemsTotal"])
        return True
    else:
        print('Error!')
        return False


def random_score(score):
    randomised_score = random.uniform(score-700, score+500)
    return randomised_score


while True:

    if start_game(stage, list_of_ids[2], list_of_ids[1], list_of_ids[0]):
        print('Playing Level {}'.format(stage))
        time.sleep(5)
        if submit_score(stage, list_of_ids[2], list_of_ids[1], list_of_ids[0], random_score(score_list[stage - 1])):
            print("OK")
            time.sleep(5)
    else:
        print('Operation Failed!')
        exit()
    if stage == 16:
        print('Game completed!')
        exit()

    stage = stage + 1
