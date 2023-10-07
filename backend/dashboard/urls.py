from django.urls import path

from .views import MenteeView, ProjectSubmitView

app_name = "dashboard"
urlpatterns = [
    path("mentor/submit/", ProjectSubmitView.as_view(), name="mentor_submit"),
    path("mentee/submit/", MenteeView.as_view(), name="mentee_saved"),
]
