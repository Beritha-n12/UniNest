from django.urls import path
from .views import BuildingListCreateView, RoomListCreateView

urlpatterns = [
    path('buildings/', BuildingListCreateView.as_view(), name='building-list-create'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
]
