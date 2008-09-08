from django.contrib import admin

from restaurant_review.apps.restaurants.models import Neighborhood, Restaurant

admin.site.register(Neighborhood)
admin.site.register(Restaurant)