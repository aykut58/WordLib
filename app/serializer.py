from .model import Category
from flask_marshmallow import Marshmallow

marshmallow=Marshmallow()

class CategorySerializer(marshmallow.Schema):
    class Meta:
        model=Category
        fields=("id","name")

class WordSerializer(marshmallow.Schema):
    class Meta:
        fields=("id","turkish","english","category")
    category=marshmallow.Nested(CategorySerializer)