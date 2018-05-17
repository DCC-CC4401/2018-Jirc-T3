from django.urls import include, path
from django.contrib import admin

from .views import landingPage, person, adminPerson
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage.home, name='home'),
    path('person/', include(([
        path('', person.LandingPersonListView.as_view(), name='landing_person'),
    ], 'landingPage'), namespace='person')),
    path('adminPerson/', include(([
        path('', adminPerson.LandingAdminListView.as_view(), name='landing_adminPerson'),
    ], 'landingPage'), namespace='adminPerson')),
]
