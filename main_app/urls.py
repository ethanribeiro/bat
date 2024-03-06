from django.urls import path
from .templates.main_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bids/', views.bidss_index, name='index'),
    path('bids/<int:bid_id>/', views.bids_detail, name='detail'),
    path('bids/create/', views.BidCreate.as_view(), name='bids_create'),
    path('bids/<int:pk>/update/', views.CatUpdate.as_view(), name='bids_update'),
    path('bids/<int:pk>/delete/', views.CatDelete.as_view(), name='bids_delete'),
]