import requests


class TestPytestDemo:

    def test_get_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        # 发起请求
        response = requests.get(f"{base_url}/posts/1")
        # 断言
        assert response.status_code == 200
        assert response.json()['userId'] == 1
        assert response.json()['id'] == 1

    def test_post_demo(self):
        base_url = "https://jsonplaceholder.typicode.com"
        requests_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
        }
    # 发起请求
        response = requests.post(f"{base_url}/posts", json=requests_data)  # 使用 json 参数

    # 断言
        assert response.status_code == 201
        print(response.json())  # 输出响应内容，供调试

        assert response.json()['userId'] == 1  # 确保 userId 是整数
        assert isinstance(response.json()['id'], int)  # 确保 id 是整数
