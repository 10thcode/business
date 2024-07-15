import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MyBusiness from '../views/MyBusiness.vue'
import MyProduct from '../views/MyProduct.vue'
import Business from '../views/Business.vue'
import Product from '../views/Product.vue'
import AddProduct from '../views/AddProduct.vue'
import AddBusiness from '../views/AddBusiness.vue'
import EditBusiness from '../views/EditBusiness.vue'
import EditProduct from '../views/EditProduct.vue'
import BusinessImages from '../views/BusinessImages.vue'
import BusinessReviews from '../views/BusinessReviews.vue'
import ProductReviews from '../views/ProductReviews.vue'
import ProductImages from '../views/ProductImages.vue'
import Explore from '../views/Explore.vue'
import Favorites from '../views/Favorites.vue'
import Notifications from '../views/Notifications.vue'
import Documentation from '../views/Documentation.vue'
import Account from '../views/Account.vue'
import Logout from '../views/Logout.vue'
import Login from '../views/Login.vue'
import NotFound from '../views/NotFound.vue'
import Error from '../views/Error.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior (to, from, savedPosition) {
    return { top: 0}
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/businesses/:businessId',
      name: 'myBusiness',
      component: MyBusiness
    },
    {
      path: '/businesses/:businessId/images',
      name: 'businessImages',
      component: BusinessImages
    },
    {
      path: '/businesses/:businessId/edit',
      name: 'editBusiness',
      component: EditBusiness
    },
    {
      path: '/businesses/:businessId/products/:productId',
      name: 'myProduct',
      component: MyProduct
    },
    {
      path: '/businesses/:businessId/products/:productId/images',
      name: 'productImages',
      component: ProductImages
    },
    {
      path: '/businesses/:businessId/products/:productId/edit',
      name: 'editProduct',
      component: EditProduct
    },
    {
      path: '/businesses/:businessId/products/add',
      name: 'addProduct',
      component: AddProduct
    },
    {
      path: '/businesses/add',
      name: 'addBusiness',
      component: AddBusiness
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: Favorites
    },
    {
      path: '/explore',
      name: 'explore',
      component: Explore
    },
    {
      path: '/explore/businesses/:businessId',
      name: 'business',
      component: Business
    },
    {
      path: '/explore/businesses/:businessId/reviews',
      name: 'businessReviews',
      component: BusinessReviews
    },
    {
      path: '/explore/businesses/:businessId/products/:productId',
      name: 'product',
      component: Product
    },
    {
      path: '/explore/businesses/:businessId/products/:productId/reviews',
      name: 'productReviews',
      component: ProductReviews
    },
    {
      path: '/notifications',
      name: 'notifications',
      component: Notifications
    },
    {
      path: '/docs',
      name: 'documentation',
      component: Documentation
    },
    {
      path: '/account',
      name: 'account',
      component: Account
    },
    {
      path: '/account/logout',
      name: 'logout',
      component: Logout
    },
    {
      path: '/account/login',
      name: 'login',
      component: Login
    },
    { path: '/error', 
      name: "error",
      component: Error
    },
    { path: '/:pathMatch(.*)*', 
      name: "notFound",
      component: NotFound
    },
  ]
})

export default router
