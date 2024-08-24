
from django.urls import path
from . import views
urlpatterns = [
   
    path('<int:category_id>',views.post_by_category,name='post_by_category'),
    # path('comment/',views.comment_input,name='comment_input'),

]
