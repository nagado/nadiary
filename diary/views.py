from django.template import loader
from django.http import HttpResponse
import settings


def index(request):
    template = loader.get_template('main.html')

    return HttpResponse(template.render(request))
