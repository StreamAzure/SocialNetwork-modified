from compose_post import generate_request as compost_post_req
from read_user_timeline import generate_request as read_user_timeline_req
import requests
import concurrent.futures
from datetime import datetime

def send_request(request):
    response = requests.Session().send(request)
    return response.text

# 使用 ThreadPoolExecutor 并行发送请求
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # 使用 submit() 函数提交任务，将 send_request 函数和对应的 request 传递进去
    compost_req, text_formatted_time = compost_post_req()
    read_req = read_user_timeline_req()

    future1 = executor.submit(send_request, compost_req)
    future2 = executor.submit(send_request, read_req)

    # 获取结果
    response1 = future1.result()
    response2 = future2.result()

# 处理响应

print(f'Response from compost_req: {response1}')
print(f'Response from read_req: {response2}')
print('=========================================')

# 检查是否能读取到前一个请求写入的 post
if text_formatted_time in response2:
    print("读取到刚刚提交的post")
else:
    print("未能读取刚刚提交的post！")

# 获取当前时间
current_time = datetime.now()

# 格式化输出，精确到秒
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current Time: {formatted_time}")