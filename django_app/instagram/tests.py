from django.test import Client
from django.test import LiveServerTestCase


class IndexTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_user_is_not_authenticated_redirect_to_signup(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/member/signup/')

    def test_user_is_authenticated_redirect_to_post_list(self):
        # 유저를 로그인 시킨다
        # 이후 root url('/')의 response를 받아온다
        # 해당 response가 /post/로 잘 redirect되는지 확인
        pass
