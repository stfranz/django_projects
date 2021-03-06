from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
    url(r'^hello/', 'hello', name='hello'),
    url(r'^article/(\d+)/', 'view_article', name='article'),
    url(r'^crudops/', 'crudops', name='crudops'),
    url(r'^datamanipulation/', 'datamanipulation', name='datamanipulation'),
)