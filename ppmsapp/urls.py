from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.home,name='home'),
    path('Eadmin/',views.Eadmin,name='Eadmin'),
    path('Euser/',views.Euser,name='Euser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signuppage/',views.signuppage,name='signuppage'),
    
    path('uprofile/',views.uprofile,name='uprofile'),
    path('add_report',views.add_report,name='add_report'),
    path('edit_report/<int:od>',views.edit_report,name='edit_report'),
    path('add_category',views.add_category,name='add_category'),
    
    path('edit_category/<int:od>',views.edit_category,name='edit_category'),
    path('showreport',views.showreport,name='showreport'),
    path('show_category',views.show_category,name='show_category'),
    path('show_user',views.show_user,name='show_user'),
    
    path('Login/',views.Login,name='Login'),
    path('Signup/',views.Signup,name='Signup'),
    path('Logout/',views.Logout,name='Logout'),
    path('eprofile/',views.eprofile,name='eprofile'),
    
    path('a_report',views.a_report,name='a_report'),
    path('e_report/<int:od>',views.e_report,name='e_report'),
    path('deletecust/<int:od>',views.deletecust,name='deletecust'),
    path('delete_report/<int:od>',views.delete_report,name='delete_report'),
    path('a_category',views.a_category,name='a_category'),
    path('e_category/<int:od>',views.e_category,name='e_category'),
    
    path('tleave/',views.tleave,name='tleave'),
    path('aleave/',views.aleave,name='aleave'),
    path('show_leave/',views.show_leave,name='show_leave'),
    path('delete_leave/<int:od>',views.delete_leave,name='delete_leave'),
    
    path('register/',views.register,name='register'),
    path('show_register/',views.show_register,name='show_register'),
    path('tregister/',views.tregister,name='tregister'),
    path('delete_register/<int:od>',views.delete_register,name='delete_register'),
    
    # path('ask-leave', views.ask_leave_view,name='ask-leave'),
    # path('leave-history', views.leave_history_view,name='leave-history'),
]
