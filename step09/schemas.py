from flask_marshmallow import Marshmallow
from models import Puppy

ma = Marshmallow()


class PuppySchema(ma.ModelSchema):
    class Meta:
        model = Puppy

puppy_schema = PuppySchema()
