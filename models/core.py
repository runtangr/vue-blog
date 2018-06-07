
from ext import db
from models.mixin import BaseMixin


class Article(BaseMixin, db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(20), default='')
    brief = db.Column(db.String(100), default='')
    tag = db.Column(db.String(10), default='')
    content = db.Column(db.String(3000), default='')

