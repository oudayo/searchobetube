from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from api import views

urlpatterns = [
    # path("courses/", views.CourseList.as_view()),
    # path("courses/<str:title>/", views.CourseDetail.as_view()),
    path("courses/", views.SearchResultsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)