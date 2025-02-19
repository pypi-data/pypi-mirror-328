# encoding: utf-8
"""
@project: djangoModel->config
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/8/4 19:24
"""


# 用户令牌的密钥配置
JWT_AUTH = {
    'JWT_SECRET_KEY': '@zxmxy2021!',
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 'JWT_ALLOW_REFRESH': True,
}

# 用户令牌的过期时间配置
EXPIRE_TIME = {
    "DAY": 7,
    "SECOND": 0,
}