import requests
import random
import string

# Load environment variables
max_user_index = 962

def string_random(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def dec_random(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def compose_post():
    print("compose_post……")
    user_index = random.randint(0, max_user_index - 1)
    username = f"username_{user_index}"
    user_id = str(user_index)
    text = string_random(256)
    num_user_mentions = random.randint(0, 5)
    num_urls = random.randint(0, 5)
    num_media = random.randint(0, 4)
    media_ids = '['
    media_types = '['

    for _ in range(num_user_mentions):
        user_mention_id = random.randint(0, max_user_index - 1)
        while user_index == user_mention_id:
            user_mention_id = random.randint(0, max_user_index - 1)
        text += f" @username_{user_mention_id}"

    for _ in range(num_urls):
        text += f" http://{string_random(64)}"

    for _ in range(num_media):
        media_id = dec_random(18)
        media_ids += f'"{media_id}",'
        media_types += '"png",'

    media_ids = media_ids[:-1] + "]"
    media_types = media_types[:-1] + "]"

    url = "http://localhost:8080/wrk2-api/post/compose"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    if num_media:
        body = f"username={username}&user_id={user_id}&text={text}&media_ids={media_ids}&media_types={media_types}&post_type=0"
    else:
        body = f"username={username}&user_id={user_id}&text={text}&media_ids=&post_type=0"

    response = requests.post(url, headers=headers, data=body)
    return response.text

def read_user_timeline():
    print("read_user_timeline……")
    user_id = str(random.randint(0, max_user_index - 1))
    start = str(random.randint(0, 100))
    stop = str(int(start) + 10)

    args = f"user_id={user_id}&start={start}&stop={stop}"
    url = f"http://localhost:8080/wrk2-api/user-timeline/read?{args}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.get(url, headers=headers)
    return response.text

def read_home_timeline():
    print("read_home_timeline……")
    user_id = str(random.randint(0, max_user_index - 1))
    start = str(random.randint(0, 100))
    stop = str(int(start) + 10)

    args = f"user_id={user_id}&start={start}&stop={stop}"
    url = f"http://localhost:8080/wrk2-api/home-timeline/read?{args}"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.get(url, headers=headers)
    return response.text

def make_request():
    read_home_timeline_ratio = 0.05
    read_user_timeline_ratio = 0.05
    compose_post_ratio = 0.90

    coin = random.random()
    if coin < read_home_timeline_ratio:
        return read_home_timeline()
    elif coin < read_home_timeline_ratio + read_user_timeline_ratio:
        return read_user_timeline()
    else:
        return compose_post()

# Assuming you have the necessary setup to run the requests
while(True):
    response = make_request()
    # print(response)
