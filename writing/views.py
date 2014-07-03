from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from writing.forms import *
from writing.models import *

# Create your views here.

def index(request):
	context = RequestContext(request)

	return render_to_response('doit/index.html', context)

def story(request):
	context= RequestContext(request)
	# print request
	# save new data
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			# return index(request)
		else:
			print form.errors
	else:
		form = ReviewForm()

		# display old data
	text_obj = Review.objects.all()
	pathInfo = request.path_info

	return render_to_response('doit/story.html', {'form': form, 'text': text_obj, 'pathInfo': pathInfo}, context)

def characters(request):
	context= RequestContext(request)
	# print request
	# save new data
	if request.method == 'POST':
		form = CharacterForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			# return index(request)
		else:
			print form.errors

	else:
		form = CharacterForm()

		# display old data
	text_obj = Character.objects.all()
	pathInfo = request.path_info

	return render_to_response('doit/story.html', {'form': form, 'text': text_obj, 'pathInfo': pathInfo}, context)	

def text(request):
	context= RequestContext(request)

	# save new data
	if request.method == 'POST':
		form = TextForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			# return index(request)
		else:
			print form.errors

	else:
		form = TextForm()

		# display old data
	text_obj = Text.objects.all()
	pathInfo = request.path_info

	return render_to_response('doit/story.html', {'form': form, 'text': text_obj, 'pathInfo': pathInfo}, context)

def events(request):
	context= RequestContext(request)

	# save new data
	if request.method == 'POST':
		form = EventForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			# return index(request)
		else:
			print form.errors

	else:
		form = EventForm()

		# display old data
	text_obj = Event.objects.all()
	pathInfo = request.path_info

	return render_to_response('doit/story.html', {'form': form, 'text': text_obj, 'pathInfo': pathInfo}, context)
