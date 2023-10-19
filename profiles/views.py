from django.shortcuts import render
from .models import Profile


def index(request):
    """View function for home page of site.
    Args:
        request (HttpRequest): The request object used to generate this response.
    Returns:
        HttpResponse: The response object.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """View function for details page of site
    Args:
        request (HttpRequest): The request object used to generate this response.
        username (str): The username of the profile to display.
    Returns:
        HttpResponse: The response object.
    """

    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)


# custom 404 view
def handler_404(request, exception):
    """View function for 404 page of site
    Args:
        request (HttpRequest): The request object used to generate this response.
        exception (Exception): The exception that was raised.
    Returns:
        HttpResponse: The response object.
    """
    return render(request, "404.html", status=404)


# custom 500 view
def server_error(request):
    """View function for 500 page of site
    Args:
        request (HttpRequest): The request object used to generate this response.
    Returns:
        HttpResponse: The response object.
    """
    return render(request, "500.html")
