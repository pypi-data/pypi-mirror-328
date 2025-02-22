import requests, json, time, base64
import threading


class ApiClient:
    def __init__(self, base_url, user_name, password):
        self.user_name = user_name
        self.password = password
        self.base_url = base_url
        # 初始化当前令牌和刷新时间
        self.token = None
        self.token_refresh_time = 0

        if not self.base_url.startswith('http'):
            raise Exception('请检查base_url格式是否正确')
        if not self.user_name or not self.password:
            raise Exception('请配置正确的用户名和密码')
        # 创建的时候获取令牌
        self.get_access_token()
        # 创建定时器,每一分钟检测一次
        self.token_thread = threading.Thread(target=self.token_thread_func)
        self.token_thread_running = True
        self.token_thread.start()

    def token_thread_func(self):
        while self.token_thread_running:
            self.get_access_token()
            time.sleep(30)

    def get_access_token(self):
        if not self.token or int(time.time()) > self.token_refresh_time:
            headers = {
                'Authorization': 'Basic ' + base64.b64encode(f"{self.user_name}:{self.password}".encode('utf-8')).decode()
            }
            token_result = self.post('/oauth2/token?grant_type=client_credentials', headers=headers)
            self.token = token_result.get('accessToken')
            # 减一分钟，防止网络延迟
            self.token_refresh_time = int(time.time()) + token_result.get('expiresIn') - 60

    @staticmethod
    def handle_response(response):
        response_text = response.text
        if response_text.startswith('{'):
            if response.status_code == 200 and response.json().get('code') == 200:
                return True, response.json().get('data')
        elif response.status_code == 504 or response.status_code == 502:
            # 服务器正在更新,等待一段时间重试
            time.sleep(30)
            return False, {}
        raise Exception('请求异常:', response.text)

    def get(self, request_path, request_body=None):
        if request_body is None:
            request_body = {}
        response = requests.request("GET", url=f"{self.base_url}/api/v1{request_path}",
                                    headers={
                                        'Authorization': 'Bearer ' + self.token
                                    },
                                    params=request_body)
        req_flag, req_data = self.handle_response(response)
        if not req_flag:
            return self.get(request_path, request_body)
        return req_data

    def post(self, request_path, request_body=None, headers=None):
        if request_body is None:
            request_body = {}
        send_headers = {
        }
        if headers:
            send_headers.update(headers)
        else:
            send_headers.update({'Authorization': 'Bearer ' + self.token})
        response = requests.post(url=f"{self.base_url}/api/v1{request_path}", headers=send_headers, data=request_body)
        req_flag, req_data = self.handle_response(response)
        if not req_flag:
            return self.get(request_path, request_body)
        return req_data

    def post_json(self, request_path, request_body=None, headers=None):
        if request_body is None:
            request_body = {}
        send_headers = {
        }
        if headers:
            send_headers.update(headers)
        else:
            send_headers.update({'Authorization': 'Bearer ' + self.token})
        response = requests.post(url=f"{self.base_url}/api/v1{request_path}", headers=send_headers, json=request_body)
        req_flag, req_data = self.handle_response(response)
        if not req_flag:
            return self.get(request_path, request_body)
        return req_data

    def close(self):
        self.token_thread_running = False
        self.token_thread.join()
