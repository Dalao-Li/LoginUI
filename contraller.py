from werkzeug.security import generate_password_hash, check_password_hash

from models import *


def register(name, pwd, email):
    if find_info(name) is not False:
        return -1
    session.add(User(name=name, email=email, pwd=generate_password_hash(pwd)))
    session.commit()
    session.close()
    if find_info(name) is False:
        return 0
    return 1


# 登录
def login(name, pwd):
    # 表示用户不存在
    if find_info(name) is False:
        return -1
    user = session.query(User).filter(User.name == name).first()
    # 若哈希密码与明文密码相对应
    if check_password_hash(user.pwd, pwd):
        return 1
    return 0


# 查询信息
def find_info(name):
    # 清空缓存
    session.commit()
    user = session.query(User).filter(User.name == name).all()
    return True if user else False
