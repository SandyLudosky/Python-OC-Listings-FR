from django.urls import path
from lettings.views import index, details

app_name = "lettings"
urlpatterns = [
    path("", index, name="index"),
    path("<int:letting_id>/", details, name="letting_details"),
]

handler404 = "lettings.views.handler_404"
handler500 = "lettings.views.server_error"
