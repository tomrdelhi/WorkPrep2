from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^(?P<transaction_id>[0-9]+)/$', views.get_by_ID, name="GetTransactionByID"),
	url(r'^(?P<transaction_id>[0-9]+)/(?P<attribute_name>.+)/$', views.show_attribute, name="ShowAttribute"),		
				]