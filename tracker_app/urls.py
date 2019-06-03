from django.conf.urls import url
from tracker_app.views import logout, login, register,home

urlpatterns = [
    # url(r'^$', index, name="=index_link"),
    url(r'logout/$', logout, name="logout_link"),
    url(r'login/$', login, name="login_link"),
    url(r'register/$', register, name="register_link"),
]
