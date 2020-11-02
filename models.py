from app import db, marshmallow

class Sub(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @classmethod
    def get_sub(cls, subid):
        sub = Sub.query.get(subid)
        if sub == None:
            return "Not Found"
        return sub_schema.jsonify(sub)

    @classmethod
    def get_subs(cls):
        subs = Sub.query.all()
        return subs_schema.jsonify(subs)

    @classmethod
    def create_sub(cls, name, description):
        new_sub = Sub(name, description)
        try:
            db.session.add(new_sub)
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception("Session Rollback")
        return sub_schema.jsonify(new_sub)

    @classmethod
    def update_sub(cls, subid, name=name, description=description):
        sub = Sub.query.get(subid)
        if name != None:
            sub.name = name
        if description != None:
            sub.description = description
        db.session.commit()
        return sub_schema.jsonify(sub)


    @classmethod
    def delete_sub(cls, subid):
        sub = Sub.query.get(subid)
        db.session.delete(sub)
        db.session.commit()
        return sub_schema.jsonify(sub)






class SubSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'description')

sub_schema = SubSchema()
subs_schema = SubSchema(many=True)

if __name__ == 'models':
    db.create_all()

