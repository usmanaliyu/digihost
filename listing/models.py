from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager
from comments . models import Comment

from django_countries.fields import CountryField
from django_countries import Countries

# Create your models here.


class AfricanCountries(Countries):
    only = [
        'DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV',
        'CF', 'KM', 'CD', 'DJ', 'EG', 'GQ', 'ER',
        'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI',
        'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML',
        'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG',
        'CG', 'RE', 'RW', 'SH', 'ST', 'SN', 'SC',
        'SL',

    ]



class Listing_category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering =['name']
        verbose_name = 'listing_category'

    def get_absolute_url(self):
        return reverse('category_listing', args=[self.slug])

    def __str__(self):
        return self.name

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='listing-logo/', blank=True)
    company_name = models.CharField(max_length=250, blank=False, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    segment = models.ForeignKey(Listing_category, on_delete=models.CASCADE, default=1, )
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)

    street = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100,blank=False)
    country = models.CharField(max_length=200, choices=(
                            ('Algeria', 'Algeria'),
                            ('Angola', 'Angola'),
                            ('Benin', 'Benin'),
                            ('Botswana', 'Botswana'),
                            ('Burkina Faso', 'Burkina Faso'),
                            ('Burundi', 'Burundi'),
                            ('Cameroon', 'Cameroon'),
                            ('Cape Verde', 'Cape Verde'),
                            ('Central African Republic', 'Central African Republic'),
                            ('Comoros', 'Comoros'),
                            ('Democratic Republic of Congo', 'Democratic Republic of Congo'),
                            ('Djibouti', 'Djibouti'),
                            ('Egypt', 'Egypt'),
                            ('Equatorial Guinea', 'Equatorial Guinea'),
                            ('Eritrea', 'Eritrea'),
                            ('Ethiopia', 'Ethiopia'),
                            ('Gabon', 'Gabon'),
                            ('Gambia', 'Gambia'),
                            ('Ghana', 'Ghana'),
                            ('Guinea', 'Guinea'),
                            ('Guinea-Bissau', 'Guinea-Bissau'),
                            ('Ivory Coast', 'Ivory Coast'),
                            ('Kenya', 'Kenya'),
                            ('Lesotho', 'Lesotho'),
                               ('Liberia', 'Liberia'),
                               ('Libya', 'Libya'),
                               ('Madagascar', 'Madagascar'),
                               ('Malawi', 'Malawi'),
                               ('Mali', 'Mali'),
                               ('Mauritania', 'Mauritania'),
                               ('Mauritius', 'Mauritius'),
                               ('Morocco', 'Morocco'),
                               ('Mozambique', 'Mozambique'),
                               ('Namibia', 'Namibia'),
                               ('Niger', 'Niger'),
                               ('Nigeria', 'Nigeria'),
                               ('Republic of the Congo', 'Republic of the Congo'),
                               ('Reunion', 'Reunion'),
                               ('Rwanda', 'Rwanda'),
                               ('Saint Helena', 'Saint Helena'),
                               ('Sao Tome and Principe', 'Sao Tome and Principe'),
                               ('Senegal', 'Senegal'),
                               ('Seychelles', 'Seychelles'),
                               ('Sierra Leone', 'Sierra Leone'),
    ))


    description = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.company_name
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


