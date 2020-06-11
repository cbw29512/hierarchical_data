from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from project.models import Tree

admin.site.register(Tree, MPTTModelAdmin)
