from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models 	 import provider,prov_addresses,job,shifts,state,region,adverts,editor,courses
from django.conf import settings
import random

# Create your views here.


def index(request):
		
		#shifts_one.update(priority=9)

		job.objects.all().update(used=0)
		adverts.objects.all().update(used=0)
		editor.objects.all().update(used=0)
		courses.objects.all().update(used=0)

#  Shifts 
		shifts_one  = shifts.objects.filter(priority=1)
		shifts_two  = shifts.objects.filter(priority=0)
		shifts_two_list = list(shifts_two)
		random.shuffle(shifts_two_list)
		shifts_list  = list(shifts_one) + shifts_two_list

#   end of shifts


#  start main part of home page

# # row 1  adverts_one_with_providers = []

		left_list  = editor.objects.filter(priority=1)	
		right_list = job.objects.filter(priority=1)	
		right_list = list(right_list) + list(courses.objects.filter(priority=1)	)
		

# row 2
		left_list  = list(left_list) + list(job.objects.filter(priority=2))
		left_list  = left_list + list(courses.objects.filter(priority=2))
		right_list = right_list + list(adverts.objects.filter(priority=1))


# row 3
		left_list  = left_list + list(editor.objects.filter(priority=2))
		right_list = right_list + list(adverts.objects.filter(priority=2))

		#  job randomiser
		job_list = list(job.objects.filter(priority=0))
		random_job = random.choice(job_list)
		random_job.used = 1
		random_job.save()
		right_list.append(random_job)


# row 4   LLR
		#  job randomiser
		job_list = list(job.objects.filter(priority=0))
		random_job = random.choice(job_list)
		random_job.used = "1"
		random_job.save()
		left_list.append(random_job)
	
		#  job randomiser
		job_list = list(job.objects.filter(priority=0))
		random_job = random.choice(job_list)
		random_job.used = "1"
		random_job.save()
		left_list.append(random_job)


		right_list   += adverts.objects.filter(priority=3)




		# left_list_with_providers = []
		# for items in left_list:
		#  	provider = items.prov_unique_idx
		#  	left_list.append({list(items),list(provider)})
		#  	#left_list_with_providers.append({items,provider})

		# #left_list = left_list_with_providers


		# adverts_one_with_providers = []
		# for advert in adverts_one:
		# 	provider = advert.prov_unique_idx
		# 	adverts_one_with_providers.append({'advert': advert, 'provider': provider})

		# adverts_two   = adverts.objects.filter(priority=0)			
		# adverts_two_with_providers = []

		# for advert in adverts_two:
		# 	provider = advert.prov_unique_idx
		# 	adverts_two_with_providers.append({'advert': advert, 'provider': provider})

		# ads_with_prov = 	list(adverts_one_with_providers) + list(adverts_two_with_providers)



		#return render(request, 'index.html', {'ads_with_prov': ads_with_prov ,'shifts_list': shifts_list})

		return render(request, 'index.html', {'left_list': left_list, 'right_list': right_list,'shifts_list': shifts_list})




def testy(request):
	return render (request, 'test.html', {}) 


def training_listing(request):
	context = {'MEDIA_URL': settings.MEDIA_URL}

	return render (request, 'training_listing.html',context) 






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
# 		right_list.append(random_course)

# 		#  adverts randomiser
# 		adverts = list(adverts.objects.filter(priority=0))
# 		random_adverts = random.choice(adverts)
# 		random_adverts.used = "1"
# 		random_adverts.save()
# 		left_list.append(random_adverts)
# 		right_list.append(random_adverts)

# 		#  editor randomiser
# 		editor = list(editor.objects.filter(priority=0))
# 		random_editor = random.choice(editor)
# 		random_editor.used = "1"
# 		random_editor.save()
# 		left_list.append(random_editor)
# 		right_list.append(random_editor)


# 		#  job randomiser
# 		job = list(job.objects.filter(priority=0))
# 		random_job = random.choice(job)
# 		random_job.used = "1"
# 		random_job.save()
# 		left_list.append(random_job)
# 		right_list.append(random_job)


