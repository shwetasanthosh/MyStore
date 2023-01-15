from rest_framework import serializers
from api.models import Products, Carts, Reviews
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    category = serializers.CharField()
    image = serializers.ImageField()


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password", "email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CartSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    products = serializers.CharField(read_only=True)
    date = serializers.CharField(read_only=True)

    class Meta:
        model = Carts
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    products = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Reviews
        fields = "__all__"
