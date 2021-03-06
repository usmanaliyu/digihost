

from django.db import models
from django.conf import settings
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering =['name']
        verbose_name = 'category'

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Article(models.Model):
    meta_description=models.TextField(blank=False)
    keywords = models.CharField(max_length=1000, blank=False)
    popular = models.CharField(max_length=50, blank=True, choices=(('true','True'),('false','False')))
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1,)
    preview_image = models.ImageField(upload_to='upload/',blank=True)
    tags = TaggableManager()
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    summary = models.TextField(max_length=1000, blank=True)
    title_body1 = models.TextField(max_length=1000, blank=True)
    title_body2 = models.TextField(max_length=1000, blank=True)
    title_body3 = models.TextField(max_length=1000, blank=True)


    sub1 = models.CharField(max_length=200, blank=True)
    sub1_child1 = models.CharField(max_length=500, blank=True)
    sub1_child1_body = models.TextField(max_length=1000, blank=True)
    sub1_child1_body2 = models.TextField(max_length=1000, blank=True)
    sub1_child1_body3 = models.TextField(max_length=1000, blank=True)
    sub1_child1_image = models.ImageField(upload_to='upload',blank=True)
    sub1_child2 = models.CharField(max_length=500, blank=True)
    sub1_child2_body = models.TextField(max_length=1000, blank=True)
    sub1_child2_body2 = models.TextField(max_length=1000, blank=True)
    sub1_child2_body3 = models.TextField(max_length=1000, blank=True)
    sub1_child2_image = models.ImageField(upload_to='upload', blank=True)
    sub1_child3 = models.CharField(max_length=500, blank=True)
    sub1_child3_body = models.TextField(max_length=1000, blank=True)
    sub1_child3_body2 = models.TextField(max_length=1000, blank=True)
    sub1_child3_body3 = models.TextField(max_length=1000, blank=True)
    sub1_child3_image = models.ImageField(upload_to='upload', blank=True)
    sub1_child4 = models.CharField(max_length=500, blank=True)
    sub1_child4_body = models.TextField(max_length=1000, blank=True)
    sub1_child4_body2 = models.TextField(max_length=1000, blank=True)
    sub1_child4_body3 = models.TextField(max_length=1000, blank=True)
    sub1_child4_image = models.ImageField(upload_to='upload', blank=True)
    sub1_child5 = models.CharField(max_length=500, blank=True)
    sub1_child5_body = models.TextField(max_length=1000, blank=True)
    sub1_child5_body2 = models.TextField(max_length=1000, blank=True)
    sub1_child5_body3 = models.TextField(max_length=1000, blank=True)
    sub1_child5_image = models.ImageField(upload_to='upload', blank=True)
    blockquote1 = models.TextField(max_length=500, blank=True)


    l_1_1=models.CharField(max_length=1000,blank=True)
    l_1_1_body=models.TextField(max_length=5000, blank=True)
    l_1_2=models.CharField(max_length=1000,blank=True)
    l_1_2_body=models.TextField(max_length=5000, blank=True)
    l_1_3=models.CharField(max_length=1000,blank=True)
    l_1_3_body=models.TextField(max_length=5000, blank=True)
    l_1_4=models.CharField(max_length=1000,blank=True)
    l_1_4_body=models.TextField(max_length=5000, blank=True)
    l_1_5=models.CharField(max_length=1000,blank=True)
    l_1_5_body=models.TextField(max_length=5000, blank=True)
    l_1_6=models.CharField(max_length=1000,blank=True)
    l_1_6_body=models.TextField(max_length=5000, blank=True)
    l_1_7=models.CharField(max_length=1000,blank=True)
    l_1_7_body=models.TextField(max_length=5000, blank=True)
    l_1_8=models.CharField(max_length=1000,blank=True)
    l_1_8_body=models.TextField(max_length=5000, blank=True)
    l_1_9=models.CharField(max_length=1000,blank=True)
    l_1_9_body=models.TextField(max_length=5000, blank=True)
    l_1_10=models.CharField(max_length=1000,blank=True)
    l_1_10_body=models.TextField(max_length=5000, blank=True)


    sub2 = models.CharField(max_length=200, blank=True)
    sub2_child1 = models.CharField(max_length=500, blank=True)
    sub2_child1_body = models.TextField(max_length=1000, blank=True)
    sub2_child1_body2 = models.TextField(max_length=1000, blank=True)
    sub2_child1_body3 = models.TextField(max_length=1000, blank=True)
    sub2_child1_image = models.ImageField(upload_to='upload',blank=True)
    sub2_child2 = models.CharField(max_length=500, blank=True)
    sub2_child2_body = models.TextField(max_length=1000, blank=True)
    sub2_child2_body2 = models.TextField(max_length=1000, blank=True)
    sub2_child2_body3 = models.TextField(max_length=1000, blank=True)
    sub2_child2_image = models.ImageField(upload_to='upload', blank=True)
    sub2_child3 = models.CharField(max_length=500, blank=True)
    sub2_child3_body = models.TextField(max_length=1000, blank=True)
    sub2_child3_body2 = models.TextField(max_length=1000, blank=True)
    sub2_child3_body3 = models.TextField(max_length=1000, blank=True)
    sub2_child3_image = models.ImageField(upload_to='upload', blank=True)
    sub2_child4 = models.CharField(max_length=500, blank=True)
    sub2_child4_body = models.TextField(max_length=1000, blank=True)
    sub2_child4_body2 = models.TextField(max_length=1000, blank=True)
    sub2_child4_body3 = models.TextField(max_length=1000, blank=True)
    sub2_child4_image = models.ImageField(upload_to='upload', blank=True)
    sub2_child5 = models.CharField(max_length=500, blank=True)
    sub2_child5_body = models.TextField(max_length=1000, blank=True)
    sub2_child5_body2 = models.TextField(max_length=1000, blank=True)
    sub2_child5_body3 = models.TextField(max_length=1000, blank=True)
    sub2_child5_image = models.ImageField(upload_to='upload', blank=True)
    blockquote2 = models.TextField(max_length=500, blank=True)

    sub3 = models.CharField(max_length=200, blank=True)
    sub3_child1 = models.CharField(max_length=500, blank=True)
    sub3_child1_body = models.TextField(max_length=1000, blank=True)
    sub3_child1_body2 = models.TextField(max_length=1000, blank=True)
    sub3_child1_body3 = models.TextField(max_length=1000, blank=True)
    sub3_child1_image = models.ImageField(upload_to='upload',blank=True)
    sub3_child2 = models.CharField(max_length=500, blank=True)
    sub3_child2_body = models.TextField(max_length=1000, blank=True)
    sub3_child2_body2 = models.TextField(max_length=1000, blank=True)
    sub3_child2_body3 = models.TextField(max_length=1000, blank=True)
    sub3_child2_image = models.ImageField(upload_to='upload', blank=True)
    sub3_child3 = models.CharField(max_length=500, blank=True)
    sub3_child3_body = models.TextField(max_length=1000, blank=True)
    sub3_child3_body2 = models.TextField(max_length=1000, blank=True)
    sub3_child3_body3 = models.TextField(max_length=1000, blank=True)
    sub3_child3_image = models.ImageField(upload_to='upload', blank=True)
    sub3_child4 = models.CharField(max_length=500, blank=True)
    sub3_child4_body = models.TextField(max_length=1000, blank=True)
    sub3_child4_body2 = models.TextField(max_length=1000, blank=True)
    sub3_child4_body3 = models.TextField(max_length=1000, blank=True)
    sub3_child4_image = models.ImageField(upload_to='upload', blank=True)
    sub3_child5 = models.CharField(max_length=500, blank=True)
    sub3_child5_body = models.TextField(max_length=1000, blank=True)
    sub3_child5_body2 = models.TextField(max_length=1000, blank=True)
    sub3_child5_body3 = models.TextField(max_length=1000, blank=True)
    sub3_child5_image = models.ImageField(upload_to='upload', blank=True)
    blockquote3 = models.TextField(max_length=500, blank=True)


    sub4 = models.CharField(max_length=200, blank=True)
    sub4_child1 = models.CharField(max_length=500, blank=True)
    sub4_child1_body = models.TextField(max_length=1000, blank=True)
    sub4_child1_body2 = models.TextField(max_length=1000, blank=True)
    sub4_child1_body3 = models.TextField(max_length=1000, blank=True)
    sub4_child1_image = models.ImageField(upload_to='upload',blank=True)
    sub4_child2 = models.CharField(max_length=500, blank=True)
    sub4_child2_body = models.TextField(max_length=1000, blank=True)
    sub4_child2_body2 = models.TextField(max_length=1000, blank=True)
    sub4_child2_body3 = models.TextField(max_length=1000, blank=True)
    sub4_child2_image = models.ImageField(upload_to='upload', blank=True)
    sub4_child3 = models.CharField(max_length=500, blank=True)
    sub4_child3_body = models.TextField(max_length=1000, blank=True)
    sub4_child3_body2 = models.TextField(max_length=1000, blank=True)
    sub4_child3_body3 = models.TextField(max_length=1000, blank=True)
    sub4_child3_image = models.ImageField(upload_to='upload', blank=True)
    sub4_child4 = models.CharField(max_length=500, blank=True)
    sub4_child4_body = models.TextField(max_length=1000, blank=True)
    sub4_child4_body2 = models.TextField(max_length=1000, blank=True)
    sub4_child4_body3 = models.TextField(max_length=1000, blank=True)
    sub4_child4_image = models.ImageField(upload_to='upload', blank=True)
    sub4_child5 = models.CharField(max_length=500, blank=True)
    sub4_child5_body = models.TextField(max_length=1000, blank=True)
    sub4_child5_body2 = models.TextField(max_length=1000, blank=True)
    sub4_child5_body3 = models.TextField(max_length=1000, blank=True)
    sub4_child5_image = models.ImageField(upload_to='upload', blank=True)
    blockquote4 = models.TextField(max_length=500, blank=True)

    sub5 = models.CharField(max_length=200, blank=True)
    sub5_child1 = models.CharField(max_length=500, blank=True)
    sub5_child1_body = models.TextField(max_length=1000, blank=True)
    sub5_child1_body2 = models.TextField(max_length=1000, blank=True)
    sub5_child1_body3 = models.TextField(max_length=1000, blank=True)
    sub5_child1_image = models.ImageField(upload_to='upload',blank=True)
    sub5_child2 = models.CharField(max_length=500, blank=True)
    sub5_child2_body = models.TextField(max_length=1000, blank=True)
    sub5_child2_body2 = models.TextField(max_length=1000, blank=True)
    sub5_child2_body3 = models.TextField(max_length=1000, blank=True)
    sub5_child2_image = models.ImageField(upload_to='upload', blank=True)
    sub5_child3 = models.CharField(max_length=500, blank=True)
    sub5_child3_body = models.TextField(max_length=1000, blank=True)
    sub5_child3_body2 = models.TextField(max_length=1000, blank=True)
    sub5_child3_body3 = models.TextField(max_length=1000, blank=True)
    sub5_child3_image = models.ImageField(upload_to='upload', blank=True)
    sub5_child4 = models.CharField(max_length=500, blank=True)
    sub5_child4_body = models.TextField(max_length=1000, blank=True)
    sub5_child4_body2 = models.TextField(max_length=1000, blank=True)
    sub5_child4_body3 = models.TextField(max_length=1000, blank=True)
    sub5_child4_image = models.ImageField(upload_to='upload', blank=True)
    sub5_child5 = models.CharField(max_length=500, blank=True)
    sub5_child5_body = models.TextField(max_length=1000, blank=True)
    sub5_child5_body2 = models.TextField(max_length=1000, blank=True)
    sub5_child5_body3 = models.TextField(max_length=1000, blank=True)
    sub5_child5_image = models.ImageField(upload_to='upload', blank=True)
    blockquote5 = models.TextField(max_length=500, blank=True)



    pub_date = models.DateTimeField(auto_now_add=True)




    l_2_1=models.CharField(max_length=1000,blank=True)
    l_2_1_body=models.TextField(max_length=5000, blank=True)
    l_2_2=models.CharField(max_length=1000,blank=True)
    l_2_2_body=models.TextField(max_length=5000, blank=True)
    l_2_3=models.CharField(max_length=1000,blank=True)
    l_2_3_body=models.TextField(max_length=5000, blank=True)
    l_2_4=models.CharField(max_length=1000,blank=True)
    l_2_4_body=models.TextField(max_length=5000, blank=True)
    l_2_5=models.CharField(max_length=1000,blank=True)
    l_2_5_body=models.TextField(max_length=5000, blank=True)
    l_2_6=models.CharField(max_length=1000,blank=True)
    l_2_6_body=models.TextField(max_length=5000, blank=True)
    l_2_7=models.CharField(max_length=1000,blank=True)
    l_2_7_body=models.TextField(max_length=5000, blank=True)
    l_2_8=models.CharField(max_length=1000,blank=True)
    l_2_8_body=models.TextField(max_length=5000, blank=True)
    l_2_9=models.CharField(max_length=1000,blank=True)
    l_2_9_body=models.TextField(max_length=5000, blank=True)
    l_2_10=models.CharField(max_length=1000,blank=True)
    l_2_10_body=models.TextField(max_length=5000, blank=True)

    source1 = models.CharField(max_length=1000,blank=True)
    source2 = models.CharField(max_length=1000,blank=True)
    source3 = models.CharField(max_length=1000,blank=True)
    source4 = models.CharField(max_length=1000,blank=True)
    source5 = models.CharField(max_length=1000,blank=True)
    source6 = models.CharField(max_length=1000,blank=True)
    source7 = models.CharField(max_length=1000,blank=True)
    source8 = models.CharField(max_length=1000,blank=True)
    source9 = models.CharField(max_length=1000,blank=True)
    source10 = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.title

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



    def get_absolute_url(self):
        return reverse('detail',args=[self.slug])
