# core / urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import polls_list, telegram_groups, add_community, payment_gateway_setup, discord_servers, discord_page, courses, example_course, premium, dashboard, dashboard_statistics, dashboard_cancellations, dashboard_payouts, dashboard_charity, terms_of_servicem

# router = DefaultRouter()
# router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path("index/", polls_list, name="polls_list"),
    path("telegram-groups/", telegram_groups, name="telegram-groups"),
    path("add-community/", add_community, name="add-community"),
    path("payment-gateway-setup/", payment_gateway_setup, name="payment-gateway-setup"),
    path("discord-servers/", discord_servers, name="discord-servers"),
    path("discord-page/", discord_page, name="discord-page"),
    path("courses/", courses, name="courses"),
    path("example-course/", example_course, name="example-course"),
    path("premium/", premium, name="premium"),
    path("dashboard/", dashboard, name="dashboard"),
    path("dashboard-statistics/", dashboard_statistics, name="dashboard-statistics"),
    path("dashboard-cancellations/", dashboard_cancellations, name="dashboard-cancellations"),
    path("dashboard-payouts/", dashboard_payouts, name="dashboard-payouts"),
    path("dashboard-charity/", dashboard_charity, name="dashboard-charity"),
    path("terms-of-service/", terms_of_servicem, name="terms-of-service"),
]