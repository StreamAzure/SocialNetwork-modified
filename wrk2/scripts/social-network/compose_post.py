import requests
import random
import os
from datetime import datetime

USERID = 666

charset = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
  'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q',
  'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
  'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5',
  '6', '7', '8', '9', '0']

decset = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

max_user_index = 962

def string_random(length):
    if length > 0:
        return string_random(length - 1) + random.choice(charset)
    else:
        return ""

def dec_random(length):
    if length > 0:
        return dec_random(length - 1) + random.choice(decset)
    else:
        return ""

def generate_request():
    # user_index = random.randint(0, max_user_index - 1)
    user_index = 4
    username = "username_" + str(user_index)
    user_id = str(user_index)
    # text = string_random(256)
    # 获取当前时间
    current_time = datetime.now()
    # 格式化输出，精确到秒
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    text = 'test_stream: ' + formatted_time
    
    # num_user_mentions = random.randint(0, 5)
    # num_urls = random.randint(0, 5)
    # num_media = random.randint(0, 4)
    # media_ids = '['
    # media_types = '['

    # for _ in range(num_user_mentions):
    #     user_mention_id = user_index
    #     while user_mention_id == user_index:
    #         user_mention_id = random.randint(0, max_user_index - 1)
    #     text += " @username_" + str(user_mention_id)

    # for _ in range(num_urls):
    #     text += " http://" + string_random(64)

    # for _ in range(num_media):
    #     media_id = dec_random(18)
    #     media_ids += "\"" + media_id + "\","
    #     media_types += "\"png\","

    # media_ids = media_ids[:-1] + "]"
    # media_types = media_types[:-1] + "]"

    method = "POST"
    url = "http://localhost:8080/wrk2-api/post/compose"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # if num_media:
    #     body = f"username={username}&user_id={user_id}&text={text}&media_ids={media_ids}&media_types={media_types}&post_type=0"
    # else:
    #     body = f"username={username}&user_id={user_id}&text={text}&media_ids=&post_type=0"
    body = f"username={username}&user_id={user_id}&text={text}&media_ids=&post_type=0"

    request = requests.Request(method, url, headers=headers, data=body)
    prepared_request = request.prepare()

    print("---- Request Headers ----")
    for key, value in prepared_request.headers.items():
        print(f"{key}: {value}")

    print("\n---- Request Body ----")
    print(prepared_request.body)

    print('=========================================')

    return requests.Request(method, url, headers=headers, data=body).prepare()

