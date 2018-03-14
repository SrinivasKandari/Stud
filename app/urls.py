from django.conf.urls import url
from . import views
app_name = 'app'
urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^users/',views.use,name="users")
]


# <!-- {{form.as_p}}
# {% csrf_token %}
# <input id='but' type="submit" name="submit" class ='btn btn-outline-primary btn-lg lg' value="Register"> -->
