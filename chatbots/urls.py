from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('chatbot', views.customer_care),
    path('onboarding', views.onboarding),
    path('onboarding_bot', views.onboarding_bot),
    path('tax-expert', views.TEI),
    path('tax_expert_bot', views.Tax_Expert_Individuals)

]