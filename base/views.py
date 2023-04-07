from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models 	 import provider,prov_addresses,job,shifts,state,courses,region,adverts,editor
from django.conf import settings
from django.views.generic import TemplateView	
import random

from django.core.mail import EmailMessage
from .forms import jobseekerform

# Create your views here.


from .forms import jobseekerform
from .models import courses, provider


from django.core.mail import EmailMessage



def courseenquire(request, section_id):
    form = jobseekerform()
    courses_queryset = courses.objects.filter(course_unique_idx=section_id)
    provider_queryset = provider.objects.filter(prov_unique_idx=section_id)
    context = {
        'form': form,
        'courses': courses_queryset,
        'provider': provider_queryset,
    }
    
    if request.method == 'POST':
        form = jobseekerform(request.POST)
        if form.is_valid():
            # Send email
            subject = 'New personal details form submission'
            message = 'Name: {}\nEmail: {}\nPhone number: {}'.format(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['phone_number']
            )
            
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email='sender@example.com',
                to=['watsonpeter65@gmail.com'],
                cc=['peter.watson.avocado@gmail.com'],
            )
            email.send()

    return render(request, 'courseenquire.html', context)




def index(request):
		# Define the variables to access the model objects
		job_objects = job.objects
		adverts_objects = adverts.objects
		editor_objects = editor.objects
		courses_objects = courses.objects

		# Update the used attribute for all the model objects
		job_objects.all().update(used=0)
		adverts_objects.all().update(used=0)
		editor_objects.all().update(used=0)
		courses_objects.all().update(used=0)

		#  Shifts
		shifts_one = shifts.objects.filter(priority=1)
		shifts_two = shifts.objects.filter(priority=0)
		shifts_two_list = list(shifts_two)
		random.shuffle(shifts_two_list)
		shifts_list = list(shifts_one) + shifts_two_list

		# start main part of home page
		left_list = job.objects.filter(priority=1)
		left_list = list(left_list) + list(courses.objects.filter(priority=1))
		left_list = list(left_list) + list(job.objects.filter(priority=2))
		left_list = list(left_list) + list(courses.objects.filter(priority=2))

		# job randomiser
		job_list = list(job.objects.filter(priority=0, used=0))
		random_job = random.choice(job_list)
		random_job.used = 1
		random_job.save()
		left_list.append(random_job)

		# course randomiser
		courses_queryset = list(courses.objects.filter(priority=0, used=0))
		random_courses = random.choice(courses_queryset)
		random_courses.used = 1
		random_courses.save()
		left_list.append(random_courses)

		# job randomiser
		job_list = list(job.objects.filter(priority=0, used=0))
		random_job = random.choice(job_list)
		random_job.used = 1
		random_job.save()
		left_list.append(random_job)

		# course randomiser
		courses_queryset = list(courses.objects.filter(priority=0, used=0))
		random_course = random.choice(courses_queryset)
		random_course.used = 1
		random_course.save()
		left_list.append(random_course)

		# job randomiser
		job_list = list(job.objects.filter(priority=0, used=0))
		random_job = random.choice(job_list)
		random_job.used = 1
		random_job.save()
		left_list.append(random_job)

		return render(request, 'index.html', {'left_list': left_list, 'shifts_list': shifts_list})



def testy(request):
	return render (request, 'test.html', {}) 


def training_listing(request):
	# context = {'MEDIA_URL': settings.MEDIA_URL}

	course_list = courses.objects.order_by('start_date')


	return render (request, 'training_listing.html',{'course_list': course_list})





def jobs_browse(request):
	if request.method == 'GET':
		# Get all the states from the database
		states = state.objects.all()
		return render(request, 'jobs_browse.html', {'states': states})
	elif 'state' in request.POST:
		selected_state    = request.POST['state']
		selected_state_id = request.POST['state']
		regions           = region.objects.filter(state_id=selected_state_id)
		# Render the regions as a dropdown list in the template
		return render(request, 'jobs_browse.html', 
			{'regions': regions , 'selected_state': selected_state})
	else:
		selected_region = request.POST['region']
		selected_region_id = request.POST['region']

		#jobs_list = Job.objects.all()
		jobs_list = job.objects.filter(region_id=selected_region_id)
		# Render the items in the template
		return render(request, 'jobs_browse.html', 
			{'jobs_list': jobs_list,  'selected_region': selected_region})

		# 'selected_state': selected_state,







#def shifts_browse(request):

	# #shifts_list = Job.objects.all()
	# 	shifts_one  = shifts.objects.filter(filled_by_us=1)
	# 	shifts_two  = shifts.objects.filter(filled_by_us=1)
	# 	random.shuffle(shifts_two)
	# 	shifts_list  = list(shifts_one) + list(shifts_two)
		
		
	# 	return render(request, 'index.html', {'shifts_list': shifts_list})

	# 	# 'selected_state': selected_state,  {'shifts_one': shifts_one},



def index_back(request):
		
		shifts_one   = shifts.objects.filter(filled_by_us=1)
		shifts_two   = shifts.objects.filter(filled_by_us=0)
		shifts_list  = list(shifts_one) + list(shifts_two)



		#adverts_one   = adverts.objects.filter(priority=1)
		adverts_one   = adverts.objects.filter(priority=1)	
		adverts_one_with_providers = []
		for advert in adverts_one:
			provider = advert.prov_unique_idx
			adverts_one_with_providers.append({'advert': advert, 'provider': provider})

		adverts_two   = adverts.objects.filter(priority=0)			
		adverts_two_with_providers = []

		for advert in adverts_two:
			provider = advert.prov_unique_idx
			adverts_two_with_providers.append({'advert': advert, 'provider': provider})

		ads_with_prov = 	list(adverts_one_with_providers) + list(adverts_two_with_providers)



		return render(request, 'index.html', {'ads_with_prov': ads_with_prov ,'shifts_list': shifts_list})








# 		#  course randomiser
# 		courses = list(course.objects.filter(priority=0))
# 		random_course = random.choice(courses)
# 		random_course.used = "1"
# 		random_course.save()
# 		left_list.append(random_course)
# 		left_list.append(random_course)

# 		#  adverts randomiser
# 		adverts = list(adverts.objects.filter(priority=0))
# 		random_adverts = random.choice(adverts)
# 		random_adverts.used = "1"
# 		random_adverts.save()
# 		left_list.append(random_adverts)
# 		left_list.append(random_adverts)

# 		#  editor randomiser
# 		editor = list(editor.objects.filter(priority=0))
# 		random_editor = random.choice(editor)
# 		random_editor.used = "1"
# 		random_editor.save()
# 		left_list.append(random_editor)
# 		left_list.append(random_editor)


# 		#  job randomiser
# 		job = list(job.objects.filter(priority=0))
# 		random_job = random.choice(job)
# 		random_job.used = "1"
# 		random_job.save()
# 		left_list.append(random_job)
# 		left_list.append(random_job)


