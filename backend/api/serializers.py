"""
Serialize and deserialize database models data.
"""
from rest_framework import serializers
from api.models import *


class BusinessSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize business model data
    """
    favorites_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = "__all__"

    def get_favorites_count(self, obj):
        """
        Gets number of favorites
        """
        return obj.business_favorites.count()

    def get_reviews_count(self, obj):
        """
        Gets number of reviews
        """
        return obj.business_reviews.count()


class BusinessHourSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize business hour model data
    """
    business = serializers.PrimaryKeyRelatedField(
        queryset=Business.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = BusinessHour
        fields = '__all__'


class BusinessImageSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize business image model data
    """
    business = serializers.PrimaryKeyRelatedField(
        queryset=Business.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = BusinessImage
        fields = '__all__'


class BusinessFavoriteSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize business favorite model data
    """
    business = serializers.PrimaryKeyRelatedField(
        queryset=Business.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = BusinessFavorite
        fields = '__all__'


class BusinessReviewSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize business review model data
    """
    business = serializers.PrimaryKeyRelatedField(
        queryset=Business.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = BusinessReview
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize product model data
    """
    business = serializers.PrimaryKeyRelatedField(
        queryset=Business.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )
    favorites_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_favorites_count(self, obj):
        """
        Gets number of favorites
        """
        return obj.product_favorites.count()

    def get_reviews_count(self, obj):
        """
        Gets number of reviews
        """
        return obj.product_reviews.count()


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize product image model data
    """
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductFavoriteSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize product favorite model data
    """
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = ProductFavorite
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize product review model data
    """
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        pk_field=serializers.UUIDField(format='hex')
    )

    class Meta:
        model = ProductReview
        fields = '__all__'


class UserNotificationSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize user notification model data
    """
    class Meta:
        model = UserNotification
        fields = '__all__'


class ProjectRatingSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize project ratings
    """
    class Meta:
        model = ProjectRating
        fields = '__all__'
