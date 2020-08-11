from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,create_engine,exists
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# 用户表
class User(Base):
    __tablename__ = 'User'
    name = Column(String(32), primary_key=True)
    email = Column(String(32))
    # 使用hash加密算法对密码进行了加密
    pwd = Column(String(100))


sqlite_url = 'sqlite:///data.db?check_same_thread=False'
# 创建引擎
engine = create_engine(sqlite_url)

# 创建表
Base.metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
