# @Desc: { 项目响应码模块 }
class USER_RERROR:
    USER_IS_NOT_EXIST = {"code": 20000001, 'msg': "user is not exist", 'data': None}
    USER_OR_PASSWORD_ERROR = {"code": 20000002, "msg": "user or password error", 'data': None}
    USER_AND_PASSWORD_IS_REQUIRED = {'code': 20000003, 'msg': "user and password is required", 'data': None}
    USERNAME_IS_EMPTY = {'code': 20000004, 'msg': "Username Is Empty", 'data': None}
    PASSWORD_IS_EMPTY = {'code': 20000005, 'msg': "Password Is Empty", 'data': None}
    USER_PASSWORD_UPDATE_FAILED = {'code': 20000006, 'msg': "User Password Update Failed", 'data': None}
    USER_IS_EXIST = {'code': 20000007, 'msg': "User Is arly Exist", 'data': None}
    PASSWORD_IS_WEAK = {'code': 20000008, 'msg': "Passsord Is Weak", 'data': None}
    EMAIL_IS_ILLEGAL = {'code': 20000009, 'msg': "Illegal Email Address", 'data': None}
    CREATE_USER_FAILED = {'code': 20000010, 'msg': "Create User Failed", 'data': None}