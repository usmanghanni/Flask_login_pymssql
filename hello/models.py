from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id,email,name,password):
        self.id = id
        self.name = name
        self.email=email
        self.password = password
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name)
