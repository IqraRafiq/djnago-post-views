from django.contrib import admin
from django.urls import path, include
from posts.views import PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='posts'),
    path('^detail/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
