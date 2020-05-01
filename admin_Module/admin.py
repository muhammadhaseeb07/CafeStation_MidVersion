from django.contrib import admin
from .models import Institute, InstituteOwner, DebitCard
# Register your models here.

admin.site.register(DebitCard)
admin.site.register(InstituteOwner)
admin.site.register(Institute)

