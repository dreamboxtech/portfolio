from django.contrib import admin

from .models import (Project, Images, User,
					 UserProfile, Work, Education,
					 Publications, Social
	)
# Register your models here.

admin.site.register(Project)
admin.site.register(Images)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Publications)
admin.site.register(Social)


