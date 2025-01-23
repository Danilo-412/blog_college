from django.uris import path
from .viems import *


urlpatterns = [
    path('hello world/' , hello_world , name = 'hello wold')

]