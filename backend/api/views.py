"""
Defines methods to handle HTTP requests
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serializers import *


@api_view(["GET", "POST"])
def business_list(request, format=None):
    """
    Handle HTTP requests for /businesses endpoint

    GET: gets all businesses
    POST: add a business
    """
    if request.method == "GET":
        category = request.query_params.get('category')
        name = request.query_params.get('name')
        user = request.query_params.get('user')

        if user:
            businesses = Business.objects.filter(user_id=user)
        elif category and name:
            businesses = Business\
                    .objects\
                    .filter(category=category)\
                    .filter(name__contains=name)
        elif category:
            businesses = Business.objects.filter(category=category)
        elif name:
            businesses = Business.objects.filter(name__contains=name)
        else:
            businesses = Business.objects.all()

        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def business_details(request, business_id, format=None):
    """
    Handel HTTP requests for /businesses/<business_id> endpoint.

    GET: gets a business
    PUT: updates a business
    DELETE: deletes a business
    """
    user = request.query_params.get('user')
    try:
        if user:
            business = Business.objects.get(id=business_id, user_id=user)
        else:
            business = Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessSerializer(business)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BusinessSerializer(
                business,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def business_hour_list(request, business_id, format=None):
    """
    Handles HTTP requests for /businesses/<business_id>/hours

    GET: gets all business working hours
    POST: add business working hour
    """
    try:
        Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        business_hours = BusinessHour.objects.filter(business=business_id)
        serializer = BusinessHourSerializer(business_hours, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BusinessHourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def business_hour_details(
        request,
        business_id,
        hour_id,
        formar=None
):
    """
    Handel HTTP requests to the
    /businesses/<business_id>/hours/<hour_id> endpoint.

    GET: gets a business working hour
    PUT: updates a business working hour
    DELETE: deletes a business working hour
    """
    try:
        business_hour = BusinessHour\
                .objects\
                .filter(business=business_id)\
                .get(id=hour_id)
    except BusinessHour.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessHourSerializer(business_hour)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BusinessHourSerializer(
                business_hour,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        business_hour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def business_image_list(request, business_id, format=None):
    """
    Handle HTTP requests for /businesses/<business_id>/images endpoint.

    GET: gets business images
    POST: adds an image to a business
    """
    try:
        Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        business_images = BusinessImage.objects.filter(business=business_id)
        serializer = BusinessImageSerializer(business_images, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BusinessImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def business_image_details(request, business_id, image_id, format=None):
    """
    Handel HTTP request for
    /businesses/<business_id>/images/<image_id> endpoint.

    GET: gets a business image
    PUT: update a business image
    DELET: deletes a business image
    """
    try:
        business_image = BusinessImage\
                .objects\
                .filter(business=business_id)\
                .get(id=image_id)
    except BusinessImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessImageSerializer(business_image)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BusinessImageSerializer(
                business_image,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        business_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def business_favorite_list(request, business_id, format=None):
    """
    Handle HTTP requests for /businesses/<business_id>/favorites endpoint

    GET: gets all business favorites
    POST: add a business as favorite
    """
    user = request.query_params.get('user')
    try:
        Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        if user:
            try:
                business_favorites = BusinessFavorite\
                        .objects\
                        .filter(business=business_id, user_id=user)
            except BusinessFavorite.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            business_favorites = BusinessFavorite\
                .objects\
                .filter(business=business_id)
        serializer = BusinessFavoriteSerializer(business_favorites, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BusinessFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def business_favorite_details(request, business_id, favorite_id, format=None):
    """
    Handle HTTP request for
    /businesses/<business_id>/favorites/<favorite_id> endpoint.

    GET: gets details about a business favorite
    PUT: updates details about a business favorite
    DELETE: deletes a business favorite
    """
    try:
        business_favorite = BusinessFavorite\
                .objects\
                .filter(business=business_id)\
                .get(id=favorite_id)
    except BusinessFavorite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessFavoriteSerializer(business_favorite)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BusinessFavoriteSerializer(
                business_favorite,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        business_favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def business_review_list(request, business_id, format=None):
    """
    Handle HTTP requests for /businesses/<business_id>/reviews endpoint

    GET: gets all business reviews
    POST: add a business as reviews
    """
    try:
        Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        business_reviews = BusinessReview.objects.filter(business=business_id)
        serializer = BusinessReviewSerializer(business_reviews, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BusinessReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def business_review_details(request, business_id, review_id, format=None):
    """
    Handle HTTP request for
    /businesses/<business_id>/reviews/<review_id> endpoint.

    GET: gets details about a business review
    PUT: updates details about a business review
    DELETE: deletes a business review
    """
    try:
        business_review = BusinessReview\
                .objects\
                .filter(business=business_id)\
                .get(id=review_id)
    except BusinessReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BusinessReviewSerializer(business_review)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BusinessReviewSerializer(
                business_review,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        business_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def product_list(request, business_id, format=None):
    """
    Handle HTTP requests to /businesses/<business_id>/products endpoint

    GET: gets all products
    POST: add a product
    """
    user = request.query_params.get('user')
    try:
        if user:
            Business.objects.get(id=business_id, user_id=user)
        else:
            Business.objects.get(id=business_id)
    except Business.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        products = Product.objects.filter(business=business_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_details(request, business_id, product_id, format=None):
    """
    Handel HTTP requests to the
    /businesses/<business_id>/products/<product_id> endpoint.

    GET: gets a product
    PUT: updates a product
    DELETE: deletes a product
    """
    user = request.query_params.get('user')
    try:
        if user:
            product = Product\
                    .objects\
                    .filter(business=business_id, business__user_id=user)\
                    .get(id=product_id)
        else:
            product = Product\
                    .objects\
                    .filter(business=business_id)\
                    .get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductSerializer(
                product,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def product_image_list(request, business_id, product_id, format=None):
    """
    Handle HTTP requests for
    /businesses/<business_id>/products/<product_id>/images endpoint.

    GET: gets product images
    POST: adds an image of a product
    """
    if request.method == "GET":
        product_images = ProductImage\
                .objects\
                .filter(product=product_id)
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_image_details(
        request,
        business_id,
        product_id,
        image_id,
        format=None
):
    """
    Handel HTTP request for
    /businesses/<business_id>/products/<product_id>/images/<image_id> endpoint.

    GET: gets a product image
    PUT: update a product image
    DELET: deletes a product image
    """
    try:
        product_image = ProductImage\
                .objects\
                .filter(product=product_id)\
                .get(id=image_id)
    except ProductImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductImageSerializer(product_image)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductImageSerializer(
                product_image,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        product_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def product_favorite_list(request, business_id, product_id, format=None):
    """
    Handle HTTP requests for
    /businesses/<business_id>/products/<product_id>/favorites endpoint

    GET: gets all product favorites
    POST: add a product as favorite
    """
    user = request.query_params.get('user')
    if request.method == "GET":
        if user:
            try:
                product_favorites = ProductFavorite\
                        .objects\
                        .filter(product_id=product_id, user_id=user)
            except ProductFavorite.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            product_favorites = ProductFavorite\
                .objects\
                .filter(product=product_id)

        serializer = ProductFavoriteSerializer(product_favorites, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductFavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_favorite_details(
        request,
        business_id,
        product_id,
        favorite_id,
        format=None
):
    """
    Handle HTTP request for
    /businesses/<business_id>/products/<product_id>/favorites/<favorite_id>
    endpoint.

    GET: gets details about a product favorite
    PUT: updates details about a product favorite
    DELETE: deletes a product favorite
    """
    try:
        product_favorite = ProductFavorite\
                .objects\
                .filter(product=product_id)\
                .get(id=favorite_id)
    except ProductFavorite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductFavoriteSerializer(product_favorite)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductFavoriteSerializer(
                product_favorite,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        product_favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def product_review_list(request, business_id, product_id, format=None):
    """
    Handle HTTP requests for
    /businesses/<business_id>/products/<product_id>/reviews endpoint

    GET: gets all product reviews
    POST: add a product as reviews
    """
    if request.method == "GET":
        product_reviews = ProductReview\
                .objects\
                .filter(product=product_id)
        serializer = ProductReviewSerializer(product_reviews, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_review_details(
        request,
        business_id,
        product_id,
        review_id,
        format=None
):
    """
    Handle HTTP request for
    /businesses/<business_id>/products/<product_id>
    /reviews/<review_id> endpoint.

    GET: gets details about a product review
    PUT: updates details about a product review
    DELETE: deletes a product review
    """
    try:
        product_review = ProductReview\
                .objects\
                .filter(product=product_id)\
                .get(id=review_id)
    except ProductReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductReviewSerializer(product_review)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = ProductReviewSerializer(
                product_review,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        product_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def user_notification_list(request, user_id, format=None):
    """
    Handle HTTP requests for /users/<user_id>/notifications

    GET: gets all users notifications
    POST: add a user notification
    """
    if request.method == "GET":
        user_notifications = UserNotification\
                .objects\
                .filter(user_id=user_id).order_by('-created_at')
        serializer = UserNotificationSerializer(user_notifications, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = UserNotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_notification_details(
        request,
        user_id,
        user_notification_id,
        format=None):
    """
    Handle HTTP requests for
    /user-notifications/<user_notification_id> endpoint.

    GET: gets a user notification
    PUT: updates a user notification
    DELETE: deletes a user notification
    """
    try:
        user_notification = UserNotification\
                .objects\
                .get(id=user_notification_id)
    except UserNotification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserNotificationSerializer(user_notification)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = UserNotificationSerializer(
                user_notification,
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        user_notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def user_favorite_product_list(request, user_id, format=None):
    """
    Handle HTTP requests for /users/<user_id>/favorites/products

    GET: gets all products that a user has added as their favorite
    """
    if request.method == "GET":
        product_favorites = ProductFavorite\
                .objects\
                .filter(user_id=user_id)
        products = [pf.product for pf in product_favorites]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def user_favorite_business_list(request, user_id, format=None):
    """
    Handle HTTP requests for /users/<user_id>/favorites/businesses

    GET: gets all businesses that a user has added as their favorite
    """
    if request.method == "GET":
        business_favorites = BusinessFavorite\
                .objects\
                .filter(user_id=user_id)
        businesses = [bf.business for bf in business_favorites]
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def project_ratings(request, format=None):
    """
    Handle HTTP requests for /ratings

    GET: gets ratings
    POST: add rating
    """
    if request.method == "GET":
        project_rating = ProjectRating.objects.all()
        serializer = ProjectRatingSerializer(project_rating, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ProjectRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
