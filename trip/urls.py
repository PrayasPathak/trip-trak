from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("dashboard/", views.trips_list, name="trip-list"),
    path("dashboard/trip/create/", views.TripCreateView.as_view(), name="trip-create"),
    path(
        "dashboard/trip/<str:pk>/",
        views.TripDetailView.as_view(),
        name="trip-detail",
    ),
    path(
        "dashboard/trip/<str:pk>/update/",
        views.TripUpdateView.as_view(),
        name="trip-update",
    ),
    path(
        "dashboard/trip/<str:pk>/delete/",
        views.TripDeleteView.as_view(),
        name="trip-delete",
    ),
    path("dashboard/note/", views.NoteListView.as_view(), name="note-list"),
    path("dashboard/note/create/", views.NoteCreateView.as_view(), name="note-create"),
    path(
        "dashboard/note/<str:pk>/", views.NoteDetailView.as_view(), name="note-detail"
    ),
    path(
        "dashboard/note/<str:pk>/update/", views.NoteUpdateView.as_view(), name="note-update"
    ),
    path(
        "dashboard/note/<str:pk>/delete/", views.NoteDeleteView.as_view(), name="note-delete"
    ),
]
