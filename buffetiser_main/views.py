from django.http import HttpResponse


# Create your views here.
def main(request):
    text = "<h1>Buffetiser Unchained!</h1>"
    return HttpResponse(text)


def config(request):
    text = "<h1>Buffetiser Unchained Config!</h1>"
    return HttpResponse(text)


def help(request):
    text = "<h1>Buffetiser Unchained Help!</h1>"
    return HttpResponse(text)