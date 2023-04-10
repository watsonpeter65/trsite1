from django.db import models    
    # Create your models here.
    # dont forget to update admin py
    
    
    
class state(models.Model):  
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=50)
    
def __str__(self):  
    return self. state_name
     
class region(models.Model): 
    region_id = models.AutoField(primary_key=True)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE, related_name='region', to_field='state_id')
    region_name = models.CharField(max_length=50)
    
def __str__(self):  
    return self. region_name
    
    
class quals(models.Model):  
    qual_unique_idx = models.BigAutoField(primary_key=True)
    qual_id = models.CharField(max_length=20)
    qual_description = models.CharField(max_length=20)
    
def __str__(self):  
    return self. qual_description
    
class provider(models.Model):   
    prov_unique_idx = models.BigAutoField(primary_key=True)
    short_name = models.CharField(max_length=20)
    
    long_name = models.CharField(max_length=50)
    
    website = models.CharField(max_length=50)
    icon_file  = models.CharField(max_length=20, blank=True)
    banner_file = models.CharField(max_length=20, blank=True)
    
    admin_name = models.CharField(max_length=20, blank=True)
    admin_email = models.EmailField(blank=True)
    admin_office = models.CharField(max_length=20, blank=True)
    admin_cell = models.CharField(max_length=20, blank=True)
    
    billing_name = models.CharField(max_length=20, blank=True)
    billing_email = models.EmailField(blank=True)
    billing_office = models.CharField(max_length=20, blank=True)
    billing_cell = models.CharField(max_length=20, blank=True)
    
def __str__(self):  
    return self. short_name
    
class prov_addresses(models.Model): 
    prov_add_unique_idx = models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='prov_addresses')
    
    prov_addy_no = models.IntegerField()
    address_name= models.CharField(max_length=50, blank=True)
    address_1 = models.CharField(max_length=50, blank=True)
    address_2 = models.CharField(max_length=50, blank=True)
    address_3 = models.CharField(max_length=50, blank=True)
    gps = models.CharField(max_length=20, blank=True)
    
def __str__(self):  
    return self. address_name

    
class shifts(models.Model): 
    shift_unique_idx= models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='shifts')
    shift_title = models.CharField(max_length=70)
    shift_desc  = models.CharField(max_length=200)
    shift_location  = models.CharField(max_length=70)
    duration= models.CharField(max_length=20)
    experience  =  models.CharField(max_length=20)
    ticketsreqd = models.CharField(max_length=120)
    cont_name   = models.CharField(max_length=20)
    cont_email  = models.EmailField()
    cont_cell   = models.CharField(max_length=20)
    start_ad_date   = models.DateField(blank=True, null=True)
    end_ad_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=20, null=True)
    used = models.CharField(max_length=20, null=True)
    expired = models.CharField(max_length=20, null=True)
    filled_by_us= models.CharField(max_length=20, blank=True)
    region  = models.ForeignKey(region, on_delete=models.CASCADE, related_name='shifts')
    
def __str__(self):  
    return self.shift_title
#   --------------------------------------   
#   the pubish models
#   --------------------------------------   
    
class job(models.Model):    
    
    job_unique_idx = models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='job')
    
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)
    topic_type = models.IntegerField(default=1)
    topic_text1  = models.CharField(max_length=200, blank=True)
    topic_text2  = models.CharField(max_length=200, blank=True)
    topic_image= models.CharField(max_length=400, blank=True)
    
    internal_link = models.CharField(max_length=400, blank=True)
    external_link = models.CharField(max_length=400, blank=True)
    
    start_date   = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    expired = models.BooleanField()
    
    adformat = models.IntegerField()
    priority = models.IntegerField(null=True)
    used = models.CharField(max_length=20, null=True)
    
    filled_by_us= models.CharField(max_length=20, blank=True)
    region = models.ForeignKey(region, on_delete=models.CASCADE, related_name='job')
    
    
    job_location  = models.CharField(max_length=120)
    
    experience = models.CharField(max_length=100)
    ticketsreqd  = models.CharField(max_length=100)
    
    cont_name = models.CharField(max_length=40)
    cont_email = models.EmailField()
    cont_cell = models.CharField(max_length=20)
    
    
def __str__(self):  
    return self. job_title


    
class adverts(models.Model):    
    
    adv_Unique_idx = models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='adverts')
    
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)
    topic_type = models.IntegerField(default=2)
    topic_text1  = models.CharField(max_length=200, blank=True)
    topic_text2  = models.CharField(max_length=200, blank=True)
    topic_image= models.CharField(max_length=400, blank=True)
    
    internal_link = models.CharField(max_length=400, blank=True)
    external_link = models.CharField(max_length=400, blank=True)
    
    start_date   = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    expired = models.BooleanField()
    
    adformat = models.IntegerField()
    priority = models.IntegerField(null=True)
    used = models.CharField(max_length=20, null=True)
    
    filled_by_us= models.CharField(max_length=20, blank=True)
    region  = models.ForeignKey(region, on_delete=models.CASCADE, related_name='adverts')
    
def __str__(self):  
    return self.short_name


class courses(models.Model):    
    
    course_unique_idx= models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='courses')
    
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)
    topic_type = models.IntegerField(default=4)
    topic_text1  = models.CharField(max_length=200, blank=True)
    topic_text2  = models.CharField(max_length=200, blank=True)
    topic_image= models.CharField(max_length=400, blank=True)
    
    internal_link = models.CharField(max_length=400, blank=True)
    external_link = models.CharField(max_length=400, blank=True)
    
    start_date   = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    expired = models.BooleanField()
    
    adformat = models.IntegerField()
    priority = models.IntegerField(null=True)
    used     = models.CharField(max_length=20, null=True)
    
    filled_by_us= models.CharField(max_length=20, blank=True)
    region  = models.ForeignKey(region, on_delete=models.CASCADE, related_name='courses')
    
def __str__(self):  
    return self.short_name
    


    
class editor(models.Model): 
    
    editor_unique_idx= models.BigAutoField(primary_key=True)
    prov_unique_idx = models.ForeignKey(provider, on_delete=models.CASCADE, related_name='editor')
    
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=50)
    topic_type = models.IntegerField(default=3)
    topic_text1  = models.CharField(max_length=200, blank=True)
    topic_text2  = models.CharField(max_length=200, blank=True)
    topic_image= models.CharField(max_length=400, blank=True)
    
    internal_link = models.CharField(max_length=400, blank=True)
    external_link = models.CharField(max_length=400, blank=True)
    
    start_date   = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    expired = models.BooleanField()
    
    adformat = models.IntegerField()
    priority = models.IntegerField(null=True)
    used = models.CharField(max_length=20, null=True)
    
    filled_by_us= models.CharField(max_length=20, blank=True)
    region  = models.ForeignKey(region, on_delete=models.CASCADE, related_name='editor')
    
    edit_title  = models.CharField(max_length=200, blank=True)
    edit_text  = models.CharField(max_length=200, blank=True)
    edit_cta   = models.CharField(max_length=200, blank=True)
    
    
def __str__(self):  
    return self.short_name
    
#   --------------------------------------   
#   the forums models
#   --------------------------------------   

from django.db import models

class forum_groups(models.Model):
    group_id    = models.BigAutoField(primary_key=True)
    short_name  = models.CharField(max_length=50)
    group_name  = models.CharField(max_length=50)
    display_order    = models.IntegerField(default=1)
    def __str__(self):
        return self.group_name

class forum_topics(models.Model):

    topic_id    = models.BigAutoField(primary_key=True)
    group   = models.ForeignKey(forum_groups, on_delete=models.CASCADE, related_name='forum_topics')
    display_order   = models.IntegerField(default=1)
    short_name  = models.CharField(max_length=50)
    forum_header    = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

class forum_posts(models.Model):

    post_id = models.BigAutoField(primary_key=True)
    topic   = models.ForeignKey(forum_topics, on_delete=models.CASCADE, related_name='forum_posts')
    post_head   = models.CharField(max_length=50)
    post_body   = models.CharField(max_length=50)
    post_by = models.CharField(max_length=50)
    anonymous   = models.BooleanField(default=0)
    post_date   = models.DateTimeField(auto_now_add=True) # modified field
    post_hide   = models.BooleanField(default=0)
    post_approved   = models.BooleanField(default=0)
    display_order    = models.IntegerField(default=1)


    def __str__(self):
        return self.post_head

