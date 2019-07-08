from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from . models import Article, Category
from comments.forms import CommentForm
from comments.models import Comment
from taggit.models import Tag
from django.core.paginator import Paginator


from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db = settings.REDIS_DB)


# Create your views here.

def home(request):
    instance_list = Article.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(instance_list, 5)
    page = request.GET.get('page')
    instance = paginator.get_page(page)


    content = {
        'instance': instance,
        'categories': categories,


    }
    return render(request, 'blog/home.html', content)



def Articles_list(request):
    instance_list= Article.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(instance_list, 10)
    page = request.GET.get('page')
    instance = paginator.get_page(page)

    content ={
        'instance':instance,
        'categories':categories,
    }
    return render(request,'blog/article_list.html',content)



def list_of_articles_by_category(request, category_slug):

    instance = Article.objects.all()
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        instance = instance.filter(category=category)


    context = {
        'categories':categories,
        'instance':instance,
        'category':category
               }
    return render(request, 'blog/category_list.html',context)





def tagged(request, tags_slug):
    categories = Category.objects.all()
    tag_category = Tag.objects.all()
    instance = Article.objects.all()



    if tags_slug:
        tags = get_object_or_404(Tag, slug=tags_slug)
        instance = instance.filter(tags=tags)


    context = {
        'categories':categories,
        'instance':instance,
        'tag':tags,
        'tag_category':tag_category,


               }
    return render(request, 'blog/tag_list_view.html',context)







def events(request):
    categories = Category.objects.all()

    content={
        'categories':categories,
    }
    return render(request,'blog/events.html',content)










def detail(request,article_slug):
    instance = get_object_or_404(Article,slug=article_slug)
    categories = Category.objects.all()



    similar_posts = instance.tags.similar_objects()[:5]



    total_views = r.incr('instance:{}:views'.format(instance.id))
    r.zincrby('instance_ranking', instance.id, 1)



    initial_data={
        'content_type': instance.get_content_type,
        'object_id': instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        user_data = form.cleaned_data.get('user')
        email_data = form.cleaned_data.get('email')

        parent_obj=None
        try:
            parent_id = request.POST.get('parent_id')
        except:
            parent_id = None


        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user = user_data,
            email=email_data,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,


        )


    comments = instance.comments
    context={
        'title': instance.title,
        'instance':instance,
        'comments': comments,
        'comment_form':form,
        'total_views':total_views,
        'similar_posts':similar_posts,
        'categories':categories,



    }
    return render(request,'blog/detail_view.html',context)


def instance_ranking(request):
    instance_ranking = r.zrange('instance_ranking', 0, -1, desc=True)[:10]
    instance_ranking_ids = [int(id) for id in instance_ranking]
    most_viewed = list(Article.objects.filter(id__in=instance_ranking_ids))
    most_viewed.sort(key=lambda x: instance_ranking_ids.index(x.id))

    return render(request, 'blog/ranking.html',
                  {'section':'instances',
                   'most_viewed': most_viewed})