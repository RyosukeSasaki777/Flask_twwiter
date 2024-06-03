from twwiter_app import db
from sqlalchemy.orm import relationship

class User_Table(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    avatar_url = db.Column(db.String(5000))

    posts = relationship('Post_Table', backref="users")
    
    def __init__(self, id=None, name=None, avatar_url=None):
        self.id = id
        self.name = name
        self.avatar_url = avatar_url
    
    def __repr__(self):
        return '<Entry id:{} name:{} avatar_url:{}>'.format(self.id,self.name,self.avatar_url)    
    
class Post_Table(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'))
    title = db.Column(db.String(50))
    text = db.Column(db.String(255))
    image_url = db.Column(db.String(5000))

    user = relationship('User_Table', back_populates="posts")
    
    def __init__(self, id=None, user_id=None, community_id=None, 
                 title=None, text=None, image_url=None):
        self.id = id
        self.user_id = user_id
        self.community_id = community_id
        self.title = title
        self.text = text
        self.image_url = image_url

    
    def __repr__(self):
        return '<Entry id:{} user_id:{} community_id:{} title:{} text:{} image_url:{}>'.format(self.id,self.user_id,self.community_id,self.title,self.text,self.image_url)    
    

class Comm_Table(db.Model):
    __tablename__='communities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(20))
    descliption = db.Column(db.String(255))
    
    def __init__(self, id=None, user_id=None, name=None, descliption=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.descliption = descliption

    
    def __repr__(self):
        return '<Entry id:{} user_id:{} name:{} descliption:{}>'.format(self.id, self.user_id, self.name, self.descliption)    
    
