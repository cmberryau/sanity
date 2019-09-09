from django.urls import path

from sanity.views import MostBasicView

# register namespace for urls
app_name = 'sanity'

urlpatterns = [
    path('', MostBasicView.as_view()),
]