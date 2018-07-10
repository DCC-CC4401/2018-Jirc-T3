from django.urls import include, path
from django.contrib import admin

from .views import landingPage, person, manager
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landingPage.home, name='home'),

    path('person/', include(([
        path('', person.LandingPersonListView.as_view(), name='landing_person'),
        path('perfil/', person.ProfilePersonView.as_view(), name='profile_person'),
        path('perfil/update/pass', person.change_password, name='profile_person_change_pass'),
    ], 'landingPage'), namespace='person')),

    path('manager/', include(([
        path('', manager.LandingManagerListView.as_view(), name='landing_manager'),
    ], 'landingPage'), namespace='manager')),
    path('manager/horario/', manager.testing_horario, name='testing_horario'),
]
