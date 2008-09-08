from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User

from restaurant_review.apps.restaurants.models import Restaurant

class Review(models.Model):
	title			= models.CharField(_('title'), max_length=200, blank=True, null=True)
	
