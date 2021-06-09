from django.urls import path
from .views import IllnessListView,IllnessDetailView,IllnessSearchDetailView,DrugListView,DrugDetailView,DrugSearchDetailView


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

path('illness',IllnessListView.as_view(),name="illness-list"),  
path('illness/<int:pk>',IllnessDetailView.as_view(),name="illness-detail"),  
path('illness/<str:search_term>',IllnessSearchDetailView.as_view(),name="searched-illness"), 

path('drug',DrugListView.as_view(),name="drug-list"),  
path('drug/<int:pk>',DrugDetailView.as_view(),name="drug-detail"),  
path('drug/<str:search_term>',DrugSearchDetailView.as_view(),name="searched-drug"), 

]

urlpatterns = format_suffix_patterns(urlpatterns)
