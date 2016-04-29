from flask_marshmallow import Marshmallow
from models import User, Puppy

ma = Marshmallow()


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

user_schema = UserSchema()


class PuppySchema(ma.ModelSchema):
    class Meta:
        model = Puppy

puppy_schema = PuppySchema()
puppies_schema = PuppySchema(many=True)
