from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
	url(r'^hello/', 'hello', name = 'hello'),
	url(r'^morning/', 'morning', name = 'morning'),
	url(r'^param/(\d+)/', 'param', name = 'param'),
	url(r'^date/(\d{2})/(\d{4})/', 'date_display', name = 'date'),
	url(r'^today/', 'today', name = 'today'),
	url(r'^crudops/', 'crudops', name = 'crudops'),
)

