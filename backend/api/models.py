"""
Defines database models
"""
from django.db import models
import uuid


class Business(models.Model):
    """
    Business model: Details about a business

    This is where business details are stored when a user
    creates a business.

    A user can create multiple businesses,
    but a business belongs to only one user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=60, blank=True)
    country_code = models.CharField(max_length=3, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to='images/businesses/', blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    long_description = models.CharField(max_length=360, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class BusinessHour(models.Model):
    """
    Business hour model: Details about a business working hour

    This is where details about a working hour
    are stored when a user adds a working to thier business.

    A business can have multiple working hours,
    but a working hour belongs to only one business.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
            Business,
            related_name="business_hours",
            on_delete=models.CASCADE
    )
    day = models.CharField(max_length=30)
    opens_at = models.TimeField()
    closes_at = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class BusinessImage(models.Model):
    """
    Business image: details about an image of a business

    This is where details about a image are stored when a
    user adds an image of their business.

    A business can have multiple image,
    but an image can belongs to only one business.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
            Business,
            related_name="business_images",
            on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/businesses')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class BusinessFavorite(models.Model):
    """
    Business favorite: Details about business favorite

    This where details about a favorite is stored when a user
    mark a business as favorite.

    A business can have multiple business favorite,
    but a favorite can only belong to one business.

    A user can mark many businesses as favorite,
    but a favorite can only belongs to a singe user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
            Business,
            related_name="business_favorites",
            on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class BusinessReview(models.Model):
    """
    Business review: Details about business review

    This is where details about a review is stored when a user
    gives a review about a business.

    A business can have multiple reveiws,
    but a review can only be associated with only one business.

    A user can mark many businesses as favorite,
    but a favorite can only belongs to a singe user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
            Business,
            related_name="business_reviews",
            on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=120)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    """
    Product model: Details about a product.

    This is where details about a product will be stored when
    a user add a product to their business.

    A business can have multiple products,
    but a product can only belongs to one business.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(
            Business,
            related_name="products",
            on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images/products', blank=True)
    short_description = models.CharField(max_length=120, blank=True)
    long_description = models.CharField(max_length=360, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, blank=True)
    negotiable = models.BooleanField(default=False)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    """
    Product image model: Details about an image of a business

    This is where details about a image are stored when a
    user adds an image of their product.

    A product can have multiple images,
    but an image can belongs to only one product.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
            Product,
            related_name="product_images",
            on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='images/products')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProductFavorite(models.Model):
    """
    Product favorite: Details about product favorite

    This where details about a favorite is stored when a user
    mark a product as favorite.

    A business can have multiple products favorite,
    but a favorite can only belong to one product.

    A user can mark many products as favorite,
    but a favorite can only belongs to a singe user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
            Product,
            related_name="product_favorites",
            on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProductReview(models.Model):
    """
    Product review model: Details about product review

    This is where details about a review is stored when a user
    gives a review about a product.

    A product can have multiple reveiws,
    but a review can only be associated with only one product.

    A user can mark many products as favorite,
    but a favorite can only belongs to a singe user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
            Product,
            related_name="product_reviews",
            on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=120)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    """
    Notification model: Details about a notification

    This where details about a notification is stored.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class UserNotification(models.Model):
    """
    User notification model: Details about a user notification

    This is where details about a notification that is sent to
    a user is stored.

    A user can have multiple notifications, and a notification
    can be sent to multiple users.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notification = models.ForeignKey(
            Notification,
            related_name="notifications",
            on_delete=models.CASCADE
    )
    user_id = models.CharField(max_length=120)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
