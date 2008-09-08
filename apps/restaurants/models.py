from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.sites.models import Site

class Neighborhood(models.Model):
	name		= models.CharField(_('name'), max_length=100)
	slug		= models.SlugField(_('slug'), max_length=50, unique=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	
	# GeoDjango
	poly		= models.PolygonField(blank=True, null=True)
	objects		= models.GeoManager()
	
	site		= models.ForeignKey(Site)
	
	def __unicode__(self):
		return u"%s" % self.name
	
	class Meta:
		verbose_name		= _('neighborhood')
		verbose_name_plural	= _('neighborhoods')
		db_table			= 'restaurant_neighborhoods'
	
	@permalink
	def get_absolute_url(self):
		return ('neighborhood_detail', None, {
			'slug':	self.slug,
		})

class Restaurant(models.Model):
	name		= models.CharField(_('name'), max_length=200)
	slug		= models.CharField(_('slug'), max_length=50, unique=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	
	# Address
	num			= models.IntegerField(_('street number'))
	street		= models.CharField(_('street name'), max_length=100)
	suite		= models.CharField(_('suite'), max_length=4, blank=True, null=True)
	city		= models.CharField(_('city'), max_length=20)
	province	= models.CharField(_('province'), max_length=10)
	postal_code	= models.CharField(_('postal code'), max_length=7)
	country		= models.CharField(_('country'), max_length=15)
	neighorhood	= models.ForeignKey(Neighborhood)
	
	# GeoDjango
	point		= models.PointField(blank=True, null=True)
	objects		= models.GeoManager()
	
	site		= models.ForeignKey(Site)
	
	def __unicode__(self):
		return u"%s" % self.name
	
	class Meta:
		verbose_name		= _('restaurant')
		verbose_name_plural	= _('Restaurants')
		db_table			= 'restaurants'
	
	@permalink
	def get_absolute_url(self):
		return ('restaurant_detail', None, {
			'slug':	self.slug,
		})
