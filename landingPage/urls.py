from django.urls import include, path

from .views import landingPage, person, admin
urlpatterns = [
    path('', landingPage.home, name='home'),
    path('person/', include(([
        path('', person.LandingPersonListView.as_view(), name='landing_person'),
    ], 'landingPage'), namespace='person')),
]