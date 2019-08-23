# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from django.views.generic.base import RedirectView
# from RestAPI import views
# urlpatterns = [
#     # Dummy route. Can be removed.
#     url(r'^/', RedirectView.as_view(url='https://hackerrank.com', permanent=False)),
#     url(r'^weather/$', views.WeatherList.as_view(), name='weather-list'),
#     url(r'^weather/(?P<pk>[0-9]+)/$', views.WeatherDetail.as_view(), name='weather-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework.routers import DefaultRouter
from RestAPI.views import WeatherViewSet

router = DefaultRouter()
router.register(prefix='weather', viewset=WeatherViewSet)

urlpatterns = router.urls