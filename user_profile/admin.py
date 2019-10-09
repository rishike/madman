from django.contrib import admin
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.html import format_html
# Register your models here.

from .models import Profile, Address

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	
	fields=('name','email','phone_number','gender','profile_pic', 'profile_image','dob','permanent_address','company_address','friends', 'user')
	readonly_fields=['profile_image','user']
	search_fields= ('name',)
	# ordering = ['name']
	list_filter = ('gender', 'permanent_address__city')

	def profile_image(self,obj):
		img_link=settings.STATIC_URL+'img/profile/'+obj.profile_pic.name.split('/')[-1]
		return mark_safe('<img class="img" src="{url}" width="150" height="150" />'.format(
			url=img_link
			))

	profile_image.short_description = 'Image Preview'




admin.site.register([Address])

