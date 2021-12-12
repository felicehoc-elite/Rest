# core / views.py

from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .serializers import RecipeSerializer
from .models import Recipe


class RecipeViewSet(viewsets.ModelViewSet) : 
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

def polls_list(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def telegram_groups(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def add_community(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def payment_gateway_setup(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def discord_servers(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def discord_page(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def courses(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def example_course(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def premium(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def dashboard(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def dashboard_statistics(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def dashboard_cancellations(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def dashboard_payouts(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def dashboard_charity(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
def terms_of_servicem(request):
	polls = Recipe.objects.all()
	data = {"results": list(polls.values("name", "ingredients", "difficulty"))}
	return JsonResponse(data)
