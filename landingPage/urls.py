from django.urls import include, path
from django.contrib import admin

from .views import landingPage, person, manager
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', landingPage.home, name='home'),

    path('person/', include(([
        path('', person.LandingPersonListView.as_view(), name='landing_person'),
    ], 'landingPage'), namespace='person')),

    path('manager/', include(([
        path('', manager.LandingManagerListView.as_view(), name='landing_manager'),
    ], 'landingPage'), namespace='manager')),
]
