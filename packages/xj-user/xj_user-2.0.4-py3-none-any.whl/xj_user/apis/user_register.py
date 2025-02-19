# _*_coding:utf-8_*_

from pathlib import Path
import re

from django.contrib.auth.hashers import make_password
from django.db.models import Q
import jwt
from rest_framework import response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from main.settings import BASE_DIR
from ..models import *
from ..services.user_detail_info_service import get_short_id
from ..utils.custom_tool import request_params_wrapper
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict

module_dir = Path(__file__).parent.parent
root_config = JDict(JConfig.get_section(str(BASE_DIR) + '/config.ini', 'xj_user', encode='utf-8-sig'))
module_config = JDict(JConfig.get_section(str(module_dir) + '/config.ini', 'xj_user', encode='utf-8-sig'))


# 用户注册
class UserRegister(APIView):
    permission_classes = (AllowAny,)
    model = BaseInfo
    params = None

    @request_params_wrapper
    def post(self, *args, request_params, **kwargs, ):
        if request_params is None:
            request_params = {}
        self.params = request_params  # 返回QueryDict类型
        token = None
        try:
            account = str(self.params.get('account', ''))
            password = str(self.params.get('password', ''))
            platform_code = str(self.params.get('platform_code', ''))
            phone = str(self.params.get('phone', ''))
            fullname = str(self.params.get('fullname', ''))
            # 边界检查
            if not account:
                raise MyApiError("账户名必填", 2001)
            if not password:
                raise MyApiError("密码必填", 2003)
            # if not fullname:
            #     raise MyApiError("姓名必填", 2008)

            # 检查平台是否存在
            platform_set = Platform.objects.filter(platform_code__iexact=platform_code)
            if platform_set.count() == 0:
                raise MyApiError("platform不存在平台名称：" + platform_code, 2009)
            platform_id = platform_set.first().platform_id

            # 账号类型判断
            if re.match(r'(^1[356789]\d{9}$)|(^\+?[78]\d{10}$)', account):
                account_type = 'phone'
            elif re.match(r'^\w+[\w\.\-\_]*@\w+[\.\w]*\.\w{2,}$', account):
                account_type = 'email'
            elif re.match(r'^[A-z\u4E00-\u9FA5]+\w*$', account):
                account_type = 'username'
            else:
                raise MyApiError("账号必须是用户名、手机或者邮箱，用户名不能是数字开头", 2009)
            # 检查账号是否存在
            user_list = None
            # if account_type == 'phone':
            #     user_list = BaseInfo.objects.filter(Q(phone=account))
            # el
            if account_type == 'email':
                user_list = BaseInfo.objects.filter(Q(email=account))
            elif account_type == 'username':
                user_list = BaseInfo.objects.filter(Q(username=account))
            # 账号验重
            # if user_list.count() and account_type == 'phone':
            #     raise MyApiError("手机已被注册: " + account)
            # el
            if user_list.count() and account_type == 'email':
                raise MyApiError("邮箱已被注册: " + account)
            elif user_list.count() and account_type == 'username':
                raise MyApiError("用户名已被注册: " + account)
            # 创建用户
            base_info = {
                # 'platform_uid': round(random.random()*1000000000),
                # 'platform_id': platform_id,
                'username': account if account_type == 'username' else get_short_id(),
                'phone': phone,
                'email': account if account_type == 'email' else '',
                # 'fullname': fullname,
            }
            current_user = BaseInfo.objects.create(**base_info)

            if platform_id:
                platforms_users = PlatformsToUsers.objects.create(**{
                    "platform_id": platform_id,
                    "user_id": current_user.id
                })
                if not platforms_users:
                    return None, "平台写入失败"
            # SECURITY WARNING: keep the secret key used in production secret!
            SECRET_KEY = 'django-insecure-l1$-m!u=!f9&o2$f(cm#dasus&a=5i1#+kh)090_=p%+==%9o1'
            JWT_SECRET_KEY = '@xzm2021!'
            c1 = root_config
            c2 = module_config
            jwt_secret_key = c1.jwt_secret_key or c2.jwt_secret_key or "@zxmxy2021!"
            token = jwt.encode({'account': account}, jwt_secret_key)
            auth = {
                'user_id': current_user.id,
                'password': make_password(password, None, 'pbkdf2_sha1'),
                'plaintext': password,
                'token': token,
            }
            current_auth = Auth.objects.create(**auth)
            res = {
                'err': 0,
                'msg': '注册成功',
                'data': {
                    "user_id": current_user.id,
                    "token": token,
                },
            }

        except SyntaxError:
            res = {
                'err': 4001,
                'msg': '语法错误'
            }
        except LookupError:
            res = {
                'err': 4002,
                'msg': '无效数据查询'
            }
        # 这里 result是一个类的对象，要用result.属性名来返回
        except Exception as valueError:
            res = {
                'err': valueError.err if hasattr(valueError, 'err') else 4000,
                'msg': valueError.msg if hasattr(valueError, 'msg') else valueError.args,
            }
        except:
            res = {
                'err': 4999,
                'msg': '未知错误'
            }
        headers = {"Authorization": token, }
        return response.Response(data=res, status=None, template_name=None, headers=headers, content_type=None)

    # def put(self, request, *args, **kwargs):
    #     self.params = parse_data(request)
    #     detaili_list = DetailInfoService.transform_result(self.params)
    #     detaili = detaili_list[0]
    #     # 添加逻辑
    #     try:
    #         username = str(self.params.get('username', ''))
    #         fullname = str(self.params.get('fullname', ''))
    #         phone = str(self.params.get('phone', ''))
    #         nickname = str(self.params.get('nickname', ''))
    #         password = str(self.params.get('password', ''))
    #         # 用户角色部门绑定
    #         user_role_list = self.params.get('user_role_list', None)
    #         user_group_list = self.params.get('user_group_list', None)
    #
    #         base_info = {}
    #         if username:
    #             base_info['username'] = username
    #             is_exists = BaseInfo.objects.filter(username=username).exists()
    #             if is_exists:
    #                 return util_response('', 7557, "用户名已存在")
    #
    #         if fullname:
    #             base_info['fullname'] = fullname
    #         if nickname:
    #             base_info['nickname'] = nickname
    #         else:
    #             base_info['nickname'] = gen_one_word_digit()
    #         if phone:
    #             base_info['phone'] = phone
    #
    #         current_user = BaseInfo.objects.create(**base_info)
    #
    #         c1 = root_config
    #         c2 = module_config
    #         jwt_secret_key = c1.jwt_secret_key or c2.jwt_secret_key or "@zxmxy2021!"
    #         token = jwt.encode({'account': username}, jwt_secret_key)
    #
    #         if password:
    #             auth = {
    #                 'user_id': current_user.id,
    #                 'password': make_password(password, None, 'pbkdf2_sha1'),
    #                 'plaintext': password,
    #                 'token': token,
    #             }
    #             Auth.objects.create(**auth)
    #
    #         if detaili.get("username"):
    #             del detaili['username']
    #         if detaili.get("fullname"):
    #             detaili['real_name'] = detaili['fullname']
    #             del detaili['fullname']
    #         if detaili.get("nickname"):
    #             del detaili['nickname']
    #         if detaili.get("phone"):
    #             del detaili['phone']
    #         if detaili.get("email"):
    #             del detaili['email']
    #         if detaili.get("user_role_list"):
    #             del detaili['user_role_list']
    #         if detaili.get("user_group_list"):
    #             del detaili['user_group_list']
    #         detaili = DetailInfoService.transform_params(detaili)
    #         detailinfo = DetailInfo.objects.filter(user_id=current_user.id).first()
    #         if detailinfo:
    #             DetailInfo.objects.filter(user_id=current_user.id).update(**detaili)
    #         else:
    #             detaili['user_id'] = current_user.id
    #             DetailInfo.objects.create(**detaili)
    #
    #         # 用户绑定权限和部门
    #         if user_group_list:
    #             UserGroupService.bind_user_group(current_user.id, user_group_list)
    #
    #         if user_role_list:
    #             RoleService.bind_user_role(current_user.id, user_role_list)
    #
    #         res = {
    #             'err': 0,
    #             'msg': '创建成功',
    #             'data': {"user_id": current_user.id},
    #         }
    #
    #     except SyntaxError:
    #         res = {
    #             'err': 4001,
    #             'msg': '语法错误'
    #         }
    #     except LookupError:
    #         res = {
    #             'err': 4002,
    #             'msg': '无效数据查询'
    #         }
    #     except Exception as valueError:
    #         res = {
    #             'err': valueError.err if hasattr(valueError, 'err') else 4000,
    #             'msg': valueError.msg if hasattr(valueError, 'msg') else valueError.args,
    #         }
    #     except:
    #         res = {
    #             'err': 4999,
    #             'msg': '未知错误'
    #         }
    #
    #     return response.Response(data=res, status=None, template_name=None, headers={"Authorization": token},
    #                              content_type=None)


class MyApiError(Exception):
    def __init__(self, message, err_code=4010):
        self.msg = message
        self.err = err_code

    def __str__(self):
        # repr()将对象转化为供解释器读取的形式。可省略
        return repr(self.msg)
