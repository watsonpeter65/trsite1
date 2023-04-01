from django.contrib import admin


from .models import provider
from .models import prov_addresses
from .models import job
from .models import shifts
from .models import courses
from .models import state
from .models import region
from .models import quals
from .models import adverts
from .models import editor








# Register your models here. 
 
admin.site.register(provider)
admin.site.register(prov_addresses)
admin.site.register(job)
admin.site.register(shifts)
admin.site.register(courses)
admin.site.register(state)
admin.site.register(region)
admin.site.register(quals)
admin.site.register(adverts)
admin.site.register(editor)


