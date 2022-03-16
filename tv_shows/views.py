from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import TvShow


class TvShowListView(ListView):
    template_name = 'tv_shows/tvshow_list.html'
    model = TvShow


class TvShowDetailView(DetailView):
    template_name = 'tv_shows/tvshow_detail.html'
    model = TvShow


class TvShowCreateView(CreateView):
    template_name = 'tv_shows/tvshow_create.html'
    model = TvShow
    fields = ['name', 'rating', 'rater']


class TvShowUpdateView(UpdateView):
    template_name = 'tv_shows/tvshow_update.html'
    model = TvShow
    fields = ['name', 'rating', 'rater']


class TvShowDeleteView(DeleteView):
    template_name = 'tv_shows/tvshow_delete.html'
    model = TvShow
    success_url = reverse_lazy('tvshow_list')
