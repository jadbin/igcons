from igcons import db
from sqlalchemy import text as _text

# id:                     存储id
# keyword:     str,       关键词
# context:     str,       关键词相关上下文信息
# clause:      str,       条款
# insert_time: timestamp, 关键词入库时间
# flag:        int,      是否研判 / 是否保存
# judge_time:  timestamp, 研判时间
# judge_user:  str,       研判用户


class Announce(db.Model):

    __tablename__ = 'announce'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keyword = db.Column(db.String(255))
    context = db.Column(db.String(255))
    clause = db.Column(db.String(255))
    flag = db.Column(db.Integer, default=0)
    judge_user = db.Column(db.String(255))
    insert_time = db.Column(db.TIMESTAMP, server_default=_text("CURRENT_TIMESTAMP"), default=db.func.now())
    judge_time = db.Column(db.TIMESTAMP, server_default=_text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), default=db.func.now(), onupdate=db.func.now())