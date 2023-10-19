from django.shortcuts import render
from .models import Letting


def index(request):
    """View function for home page of site.
    Args:
        request (HttpRequest): The request object used to generate this response.
    Returns:
        HttpResponse: The response object.
    """

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    print(lettings_list)
    return render(request, "lettings/index.html", context)


def details(request, letting_id):
    """View function for details page of site
    Args:
        request (HttpRequest): The request object used to generate this response.
        letting_id (int): The id of the letting to display.
    Returns:
        HttpResponse: The response object.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/details.html", context)


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
