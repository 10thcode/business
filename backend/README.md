# Backend API

This API provides functionality for managing businesses and their products.

## Important files

- **[`api/models.py`](https://github.com/10thcode/business/blob/main/backend/api/models.py)**: Defines database models.

- **[`api/serializers.py`](https://github.com/10thcode/business/blob/main/backend/api/serializers.py)**: Defines classes to serialize and deserialize data.

- **[`api/views.py`](https://github.com/10thcode/business/blob/main/backend/api/views.py)**: Defines fuctions to handel HTTP requests.

- **[`api/urls.py`](https://github.com/10thcode/business/blob/main/backend/api/urls.py)**: Maps api url endpoints to their corresponding handlers.

- **[`backend/settings.py`](https://github.com/10thcode/business/blob/main/backend/backend/settings.py)**: Django settings for the backend api project.

- **[`requirements.txt`](https://github.com/10thcode/business/blob/main/backend/requirements.txt)**: Backend API project dependencies.


## Features

- **RESTful API Standard:** Follows REST principles for resource management.
- **Business Management:** Allows creating, reading, updating, and deleting business entities.
- **Product Management:** Facilitates management of products within businesses, including CRUD operations.
- **Notification System:** Integrates a robust system to manage user notifications, supporting creation, retrieval, and status updates.
- **Scalable Architecture:** Designed to handle multiple businesses and products efficiently.
- **Comprehensive Error Handling:** Provides clear and consistent error messages for client and server errors.
- **JSON Responses:** All responses are in JSON format for easy integration with frontend applications.
- **Modular Endpoints:** Segregated endpoints for businesses and products to ensure clean and maintainable code.

## Setup
### Prerequisites

- [Python 3.x](https://www.python.org/)
- [SQLite 3](https://sqlite.org/) For development

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:10thcode/business.git
   cd invoice/backend
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Make and apply migrations:
    ```bash
    python manage.py makemigrations && python manage.py migrate 
    ```


### Running the Application

1. Start the Django application:
    ```bash
    python manage.py runserver 
    ```

2. The application will run on http://127.0.0.1:8000/


## API Endpoints

### Businesses

#### Get All Businesses

`GET /api/v1/businesses`
- **Description:** Retrieve a list of all businesses.
- **Response:** A JSON array of business objects.

#### Get A Businesses

`GET /api/v1/businesses/{businessId}`
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON object representing the business.

#### Create a Business

`POST /api/v1/businesses/`
- **Description:** Create a new business.
- **Request Body:** A JSON object containing the business details.
- **Response:** A JSON object representing the created business.

#### Update a Business

`PUT api/v1/businesses/{businessId}/`
- **Description:** Update an existing business by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the updated business details.
- **Response:** A JSON object representing the updated business.

#### Delete a Business

`DELETE api/v1/businesses/{businessId}/`
- **Description:** Delete a business by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business


### Business Hours

#### Get All Business Hours

`GET /api/v1/businesses/{businessId}/hours`
- **Description:** Retrieve a list of business hours.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON array of business hour objects.

#### Get Business Hour Details

`GET /api/v1/businesses/{businessId}/hours/{hourId}`
- **Description:** Retrieve details of a specific business hour by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **hourId** (string) - ID of the business hour
- **Response:** A JSON object representing the business hour.

#### Add a Business Hour

`POST /api/v1/businesses/{businessId}/hours/`
- **Description:** Create a new business hour.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the business hour details.
- **Response:** A JSON object representing the created business hour.

#### Update a Business Hour

`PUT /api/v1/businesses/{businessId}/hours/{hourId}/`
- **Description:** Update an existing business hour by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **hourId** (string) - ID of the business hour
- **Request Body:** A JSON object containing the updated business hour details.
- **Response:** A JSON object representing the updated business hour.

#### Delete a Business Hour

`DELETE /api/v1/businesses/{businessId}/hours/{hourId}/`
- **Description:** Delete a business hour by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **hourId** (string) - ID of the business hour.


### Business Images

#### Get All Business Images

`GET /api/v1/businesses/{businessId}/images`
- **Description:** Retrieve a list of all business images.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON array of all business image objects.

#### Get a Business Image

`GET /api/v1/businesses/{businessId}/images/{imageId}`
- **Description:** Retrieve details of a specific business image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **imageId** (string) - ID of the business image
- **Response:** A JSON object representing the business image.

#### Add a Business Image

`POST /api/v1/businesses/{businessId}/images/`
- **Description:** Add a new business image.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the business image details.
- **Response:** A JSON object representing the added business image.

#### Update a Business Image

`PUT /api/v1/businesses/{businessId}/images/{imageId}/`
- **Description:** Update an existing business image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **imageId** (string) - ID of the business image
- **Request Body:** A JSON object containing the updated business image details.
- **Response:** A JSON object representing the updated business image.

#### Delete a Business Image

`DELETE /api/v1/businesses/{businessId}/images/{imagesId}/`
- **Description:** Delete a business image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **imageId** (string) - ID of the business image


### Business Favorites

#### Get All Business Favorites

`GET /api/v1/businesses/{businessId}/favorites`
- **Description:** Retrieve a list of all business favorites.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON array of all business favorite objects.

#### Get a Business Favorite

`GET /api/v1/businesses/{businessId}/favorites/{favoriteId}`
- **Description:** Retrieve details of a specific business favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **favoriteId** (string) - ID of the business favorite
- **Response:** A JSON object representing the business favorite.

#### Add a Business Favorite

`POST /api/v1/businesses/{businessId}/favorite/`
- **Description:** Add a new business favorite.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the business favorite details.
- **Response:** A JSON object representing the added business favorite.

#### Update a Business Favorite

`PUT /api/v1/businesses/{businessId}/favorites/{favoriteId}/`
- **Description:** Update an existing business favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **favoriteId** (string) - ID of the business favorite
- **Request Body:** A JSON object containing the updated business favorite details.
- **Response:** A JSON object representing the updated business favorite.

#### Delete a Business Favorite

`DELETE /api/v1/businesses/{businessId}/favorites/{favoriteId}/`
- **Description:** Delete a business favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **favoriteId** (string) - ID of the business favorite


### Business Reviews

#### Get All Business Reviews

`GET /api/v1/businesses/{businessId}/reviews`
- **Description:** Retrieve a list of all business reviews.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON array of all business reviews objects.

#### Get a Business Review

`GET /api/v1/businesses/{businessId}/reviews/{reviewId}`
- **Description:** Retrieve details of a specific business review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **reviewId** (string) - ID of the business review
- **Response:** A JSON object representing the business review.

#### Add a Business Review

`POST /api/v1/businesses/{businessId}/reviews/`
- **Description:** Add a new business review.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the business review details.
- **Response:** A JSON object representing the added business review.

#### Update a Business Review

`PUT /api/v1/businesses/{businessId}/reviews/{reviewId}/`
- **Description:** Update an existing business review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **reviewId** (string) - ID of the business review
- **Request Body:** A JSON object containing the updated business review details.
- **Response:** A JSON object representing the updated business review.

#### Delete a Business Review

`DELETE /api/v1/businesses/{businessId}/review/{reviewId}/`
- **Description:** Delete a business review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **reviewId** (string) - ID of the business review


### Business Products

#### Get All Business Products

`GET /api/v1/businesses/{businessId}/products`
- **Description:** Retrieve a list of all business product.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Response:** A JSON array of all product objects.

#### Get a Business Product

`GET /api/v1/businesses/{businessId}/product/{productId}`
- **Description:** Retrieve details of a specific product by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Response:** A JSON object representing the product.

#### Add a Product to a Business

`POST /api/v1/businesses/{businessId}/products/`
- **Description:** Add a new product to a business.
- **Parameters:**
    - **businessId** (string) - ID of the business
- **Request Body:** A JSON object containing the product details.
- **Response:** A JSON object representing the added product.

#### Update a Business Product

`PUT /api/v1/businesses/{businessId}/products/{productId}/`
- **Description:** Update an existing product by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Request Body:** A JSON object containing the updated product details.
- **Response:** A JSON object representing the updated product.

#### Delete a Business Product

`DELETE /api/v1/businesses/{businessId}/product/{productId}/`
- **Description:** Delete a business product by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product


### Product Images

#### Get All Product Images

`GET /api/v1/businesses/{businessId}/products/{productId}/images`
- **Description:** Retrieve a list of all product images.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Response:** A JSON array of all product images objects.

#### Get a Product Image

`GET /api/v1/businesses/{businessId}/product/{productId}/images/{imageId}`
- **Description:** Retrieve details of a specific product image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **imageId** (string) - ID of the image
- **Response:** A JSON object representing the product image.

#### Add a Product Image

`POST /api/v1/businesses/{businessId}/products/{productId}/images/`
- **Description:** Add a new product image.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Request Body:** A JSON object containing the product image details.
- **Response:** A JSON object representing the added product image.

#### Update a Product Image

`PUT /api/v1/businesses/{businessId}/products/{productId}/images/{imageId}/`
- **Description:** Update an existing product image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **imageId** (string) - ID of the image
- **Request Body:** A JSON object containing the updated product image details.
- **Response:** A JSON object representing the updated product image.

#### Delete a Product Image

`DELETE /api/v1/businesses/{businessId}/product/{productId}/images/{imageId}/`
- **Description:** Delete a business product image by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **imageId** (string) - ID of the image


### Product Favorites

#### Get All Product Favorites

`GET /api/v1/businesses/{businessId}/products/{productId}/favorites`
- **Description:** Retrieve a list of all product favorites.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Response:** A JSON array of all product favorites objects.

#### Get a Product Favorite

`GET /api/v1/businesses/{businessId}/product/{productId}/favorites/{favoriteId}`
- **Description:** Retrieve details of a specific product favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **favoriteId** (string) - ID of the favorite
- **Response:** A JSON object representing the product favorite.

#### Add a Product Favorite

`POST /api/v1/businesses/{businessId}/products/{productId}/favorites/`
- **Description:** Add a new product favorite.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Request Body:** A JSON object containing the product favorite details.
- **Response:** A JSON object representing the added product favorite.

#### Update a Product Favorite

`PUT /api/v1/businesses/{businessId}/products/{productId}/favorite/{favoriteId}/`
- **Description:** Update an existing product favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **favoriteId** (string) - ID of the favorite
- **Request Body:** A JSON object containing the updated product favorite details.
- **Response:** A JSON object representing the updated product favorite.

#### Delete a Product Favorite

`DELETE /api/v1/businesses/{businessId}/product/{productId}/favorites/{favoriteId}/`
- **Description:** Delete a business product favorite by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **favoriteId** (string) - ID of the favorite


### Product Reviews

#### Get All Product Reviews

`GET /api/v1/businesses/{businessId}/products/{productId}/reviews`
- **Description:** Retrieve a list of all product reviews.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Response:** A JSON array of all product review objects.

#### Get a Product Review

`GET /api/v1/businesses/{businessId}/product/{productId}/reviews/{reviewId}`
- **Description:** Retrieve details of a specific product review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **reviewId** (string) - ID of the review
- **Response:** A JSON object representing the product review.

#### Add a Product Review

`POST /api/v1/businesses/{businessId}/products/{productId}/reviews/`
- **Description:** Add a new product review.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
- **Request Body:** A JSON object containing the product review details.
- **Response:** A JSON object representing the added product review.

#### Update a Product Review

`PUT /api/v1/businesses/{businessId}/products/{productId}/reviews/{reviewId}/`
- **Description:** Update an existing product review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **reviewId** (string) - ID of the review
- **Request Body:** A JSON object containing the updated product review details.
- **Response:** A JSON object representing the updated product review.

#### Delete a Product Favorite

`DELETE /api/v1/businesses/{businessId}/product/{productId}/reviews/{reviewId}/`
- **Description:** Delete a business product review by its ID.
- **Parameters:**
    - **businessId** (string) - ID of the business
    - **productId** (string) - ID of the product
    - **favoriteId** (string) - ID of the review

### Notifications

#### Get Notifications

`GET /api/v1/notifications`
- **Description:** Retrieve a list of all notifications.
- **Response:** A JSON array of all notification objects.

#### Get a Nofication details

`GET /api/v1/notifications/{notificationId}`
- **Description:** Retrieve details of a specific notification by its ID.
- **Parameters:**
    - **notificationId** (string) - ID of the notification.
- **Response:** A JSON object representing the notification.

#### Add a Notification

`POST /api/v1/notifications/`
- **Description:** Add a new notification.
- **Request Body:** A JSON object containing the notification details.
- **Response:** A JSON object representing the added notification.

#### Update a Notification

`PUT /api/v1/notifications/{notificationId}/`
- **Description:** Update an existing notification by its ID.
- **Parameters:**
    - **notificationId** (string) - ID of the notification.
- **Request Body:** A JSON object containing the updated notification details.
- **Response:** A JSON object representing the updated notification.

#### Delete a Notification

`DELETE /api/v1/notifications/{notificationId}/`
- **Description:** Delete a notification by its ID.
- **Parameters:**
    - **notificationId** (string) - ID of the notification.


### User Notifications

#### Get User Notifications

`GET /api/v1/users/{userId}/notifications`
- **Description:** Retrieve a list of all user notifications.
- **Parameters:**
    - **userId** (string) - ID of the user.
- **Response:** A JSON array of all user notification objects.

#### Get a User Nofication details

`GET /api/v1/users/{userId}/notifications/{notificationId}`
- **Description:** Retrieve details of a specific user notification by its ID.
- **Parameters:**
    - **userId** (string) - ID of the user.
    - **notificationId** (string) - ID of the notification.
- **Response:** A JSON object representing the user notification.

#### Add a User Notification

`POST /api/v1/users/{userId}/notifications/`
- **Description:** Add a new user notification.
- **Parameters:**
    - **userId** (string) - ID of the user.
- **Request Body:** A JSON object containing the user notification details.
- **Response:** A JSON object representing the added user notification.

#### Update a User Notification

`PUT /api/v1/users/{userId}/notifications/{notificationId}/`
- **Description:** Update an existing user notification by its ID.
- **Parameters:**
    - **userId** (string) - ID of the user.
    - **notificationId** (string) - ID of the notification.
- **Request Body:** A JSON object containing the updated user notification details.
- **Response:** A JSON object representing the updated user notification.

#### Delete a Notification

`DELETE /api/v1/users/{userId}/notifications/{notificationId}/`
- **Description:** Delete a user notification by its ID.
- **Parameters:**
    - **userId** (string) - ID of the user.
    - **notificationId** (string) - ID of the notification.


## Error Handling

The API uses standard HTTP status codes to indicate the success or failure of a request. Common status codes include:

- `200 OK:` The request was successful.
- `201 Created:` A new resource was created successfully.
- `400 Bad Request:` The request was invalid or cannot be served.
- `401 Unauthorized:` The request requires authentication.
- `403 Forbidden:` The server understood the request but refuses to authorize it.
- `404 Not Found:` The requested resource could not be found.
- `405 No Content:` The requested resource was deleted.
- `500 Internal Server Error:` An error occurred on the server.

In case of an error, the response body will contain a JSON object with an error key providing more details.

## Contributing
1. Fork the repository.

2. Create a new branch: `git checkout -b feature-branch-name`.

3. Make your changes and commit them: `git commit -m 'Add some feature'`.

4. Push to the branch: `git push origin feature-branch-name`.

5. Submit a pull request.
