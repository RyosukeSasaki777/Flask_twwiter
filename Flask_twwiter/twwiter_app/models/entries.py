from twwiter_app import db
# from datetime import date

class Entry(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return '<Entry id:{} name:{}>'.format(self.id,self.name)    
    
class Entry(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    community_id = db.Column(db.Integer, db.ForeignKey('communities.id'))
    title = db.Column(db.String(50))
    text = db.Column(db.String(255))
    image_url = db.Column(db.String)
    
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
    

class Entry(db.Model):
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
    
