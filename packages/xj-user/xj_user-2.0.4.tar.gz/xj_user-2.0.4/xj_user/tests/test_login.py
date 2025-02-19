# encoding: utf-8
"""
@project: djangoModel->test_login
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 自带的单元测试
@created_time: 2023/4/18 22:06
"""

from django.test import TestCase

from ..services.user_service import UserService


class TestLogin(TestCase):
    username = "gaodt"
    password = "123456"
    platform = "镖行天下在线工作平台"

    # def setUp(self):
    #     self.username = "gaodt"
    #     self.password = "123456"
    #     self.platform = "镖行天下在线工作平台"

    # def test_login(self):
    #     """正确测试"""
    #     account_serv, error_text = UserService.check_account(self.username)
    #     assert error_text is None
    #     user_id = account_serv['user_id']
    #     auth_serv, error_text = UserService.check_login(
    #         user_id=user_id,
    #         password=self.password,
    #         account=self.username,
    #         platform=self.platform
    #     )
    #
    #     assert error_text is None
    #
    # def test_with_out_username(self):
    #     """错误操作测试"""
    #     self.username = ""
    #     account_serv, error_text = UserService.check_account(self.username)
    #     assert error_text is None
    #     user_id = account_serv['user_id']
    #     auth_serv, error_text = UserService.check_login(
    #         user_id=user_id,
    #         password=self.password,
    #         account=self.username,
    #         platform=self.platform
    #     )
    #     assert error_text is None
