from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

"""
Urls overview in form "url name: short description":

 * login: log in form
 * logout: log out view
 * logout_successfull: the page after successful log out
 * registration_register: sign up form
 * registration_complete: the page after successful registration
 * activation_required: the page with activation remainder
        which shows after filling the registration form
 * password_reset: form for password reset by anonymous user
 * password_change: form for password change by loged in user
 * password_change_done: page after success password change
 * email_change: form for email change
 * email_change_done: the page after success email change
"""

app_name = 'auth'
urlpatterns = [
    # Log in, log out
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^logout/successful/$', views.logout_successful,
        name='logout_successful'),

    # Registration
    url(r'^registration/$', views.registration,
        name='registration_register'),
    url(r'^activation/required/$',
        TemplateView.as_view(template_name='account/activation_required.html'),
        name='activation_required'),
    url(r'^registration/complete/$',
        TemplateView.as_view(template_name='account/registration_complete.html'),
        name='registration_complete'),

    # Password management
    url(r'^password/reset/$', views.password_reset,
        name='password_reset'),
    url(r'^password/change/$', views.password_change,
        name='password_change'),
    url(r'^password/change/done/$', views.password_change_done,
        name='password_change_done'),

    # Email management
    url(r'^email/change/$', views.email_change, name='email_change'),
    url(r'^email/change/done/$', views.email_change_done,
        name='email_change_done'),
]
