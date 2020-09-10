from django.urls import path

from . import views

urlpatterns = [
    path('sign_in', views.sign_in, name="sign_in"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('forgot_password', views.forgot_password, name="forgot_password"),
    path('terms_of_use', views.terms_of_use, name="terms_of_use"),
    path('sign_up_steps', views.sign_up_steps, name="sign_up_steps"),

    path('my_instructor_profile_view', views.my_instructor_profile_view, name="my_instructor_profile_view"),
    path('instructor_dashboard', views.instructor_dashboard, name="instructor_dashboard"),
    path('about_us', views.about_us, name="about_us"),
    path('our_blog', views.our_blog, name="our_blog"),
    path('press', views.press, name="press"),
    path('help', views.help, name="help"),
    path('coming_soon', views.coming_soon, name="coming_soon"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('career', views.career, name="career"),
    path('create_new_course', views.create_new_course, name="create_new_course"),
    path('instructor_messages', views.instructor_messages, name="instructor_messages "),
    

]