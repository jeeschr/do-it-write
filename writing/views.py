from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

from writing.forms import ReviewForm
from writing.models import Review

# Create your views here.

def index(request):
	context = RequestContext(request)

	return render_to_response('doit/index.html', context)



def story(request):
	context= RequestContext(request)

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

	return render_to_response('doit/story.html', {'form': form, 'text': text_obj}, context)


