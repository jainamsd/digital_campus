from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import controller

urlpatterns = [
        path('', controller.home),
        path('login/', controller.login),
        path('logininsert1/', controller.logininsert1),
        path('logout/', controller.logout),
        path('student_inquiry/', controller.student_inquiry),
        path('afterlogin/', controller.afterlogin),

        path('Offer_letter_Certificate/', controller.Offer_letter_Certificate),
        path('Leave_for_Internship/', controller.Leave_for_Internship),
        path('gen_recipt/', controller.gen_recipt),
        path('gne_certificate/', controller.gne_certificate),
        path('Experience_Certificate/', controller.Experience_Certificate),
        path('generae_certificatedata/', controller.generae_certificatedata),
        path('CANDCPLUS/', controller.CANDCPLUS),
        path('devlopment/', controller.devlopment),
        path('htmlandcss/', controller.htmlandcss),
        path('javalangdecription/', controller.javalangdecription),
        path('pythonlang/', controller.pythonlang),
        path('nodejs/', controller.nodejs),

]
