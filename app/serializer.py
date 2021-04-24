from .model import Word
from flask_marshmallow import Marshmallow

marshmallow=Marshmallow()

class WordSerializer(marshmallow.Schema):
    class Meta:
        model=Word
        fields=("id","turkish","english")