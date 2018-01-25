from django.conf.urls import url
from .views import (
    ControlIndex,
    ControlActions
)


urlpatterns = [
    url(r'^$', ControlIndex.as_view()),
    url(r'^actions/$', ControlActions.as_view())
]
