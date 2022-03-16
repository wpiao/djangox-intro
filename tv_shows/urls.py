from django.urls import path
from .views import TvShowCreateView, TvShowDeleteView, TvShowDetailView, TvShowListView, TvShowUpdateView

urlpatterns = [
    path('', TvShowListView.as_view(), name='tvshow_list'),
    path('<int:pk>/', TvShowDetailView.as_view(), name='tvshow_detail'),
    path('create/', TvShowCreateView.as_view(), name='tvshow_create'),
    path('<int:pk>/update/', TvShowUpdateView.as_view(), name='tvshow_update'),
    path('<int:pk>/delete/', TvShowDeleteView.as_view(), name='tvshow_delete')
]
