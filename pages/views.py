from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request,  "home.html")
def signIn(request):
    return TemplateResponse(request,  "sign_in.html")
