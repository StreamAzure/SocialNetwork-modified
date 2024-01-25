import requests
import random
import os
import time
from compose_post import USERID

time_seed = int(time.time() * 1000)
random.seed(time_seed)
random.random()
random.random()
random.random()

max_user_index = 962

def generate_request():
    # user_id = str(random.randint(0, max_user_index - 1))
    user_id = str(USERID)
    # start = str(random.randint(0, 100))
    start = 0
    stop = str(int(start) + 3)

    args = f"user_id={user_id}&start={start}&stop={stop}"
    method = "GET"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = f"http://localhost:8080/wrk2-api/user-timeline/read?{args}"

    request = requests.Request(method, url, headers=headers)
    prepared_request = request.prepare()

    print("---- Request Headers ----")
    print(prepared_request.path_url)
    for key, value in prepared_request.headers.items():
        print(f"{key}: {value}")

    print('=========================================')

    return requests.Request(method, url, headers=headers).prepare()

# # Example of usage:
# prepared_request = generate_request()
# response = requests.Session().send(prepared_request)
# print(response.text)