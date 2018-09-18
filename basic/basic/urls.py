"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from basicpro.views import *
from basicpro import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
router = routers.SimpleRouter()
schema_view = get_swagger_view(title='Registration API')
router.register(r'signup', views.SignUpViewSet, 'signup')
#router.register(r'get_all_users', views.SignUpViewSet, 'get_all_users$')
# all_signup = SignUpViewSet.as_view({
#    'post': 'register'
# })

# get_all_users = SignUpViewSet.as_view({
#    'get': 'get_all_users'
# })

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'^schema_view', schema_view),
    url(r'^', include(router.urls))
]
# urlpatterns += format_suffix_patterns([
#    url(r'^signup$', all_signup, name='all_signup'),
#    #url(r'^get_all_users$',get_all_users, name='get_all_users'),
#
#
# ])