from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:student_id>',views.detail,name='detail'),
    path('edit_marks/<int:student_id>',views.edit_marks,name='edit_marks'),
    path('delete_student/<int:student_id>',views.delete_student,name='delete_student'),
] 