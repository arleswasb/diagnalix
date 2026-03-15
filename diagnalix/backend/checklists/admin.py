from django.contrib import admin
from .models import Category, MedicalCard, ChecklistItem

class ChecklistItemInline(admin.TabularInline):
    model = ChecklistItem
    extra = 1

@admin.register(MedicalCard)
class MedicalCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    inlines = [ChecklistItemInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

