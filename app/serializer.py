from .model import Category,TurkishWord,EnglishWord
from flask_marshmallow import Marshmallow

marshmallow=Marshmallow()

class CategorySerializer(marshmallow.Schema):
    class Meta:
        model=Category
        fields=("id","turkish_name","english_name")

class NestedEnglishWordSerializer(marshmallow.Schema):
    class Meta:
        model=EnglishWord
        fields=("id","word")

class TurkishWordSerializer(marshmallow.Schema):
    class Meta:
        model=TurkishWord
        fields=("id","english_words","category","word")
    category=marshmallow.Nested(CategorySerializer)
    english_words=marshmallow.Nested(NestedEnglishWordSerializer(many=True))

class NestedTurkishWordSerializer(marshmallow.Schema):
    class Meta:
        model=TurkishWord
        fields=("id","word")

class EnglishWordSerializer(marshmallow.Schema):
    class Meta:
        model=EnglishWord
        fields=("id","turkish_words","word","category")
    category=marshmallow.Nested(CategorySerializer)
    turkish_words=marshmallow.Nested(NestedTurkishWordSerializer(many=True))