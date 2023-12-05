from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from.models import Grade,Subject,Book,Chapter

@admin.register(Grade)
class GradeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','grade']

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','subject']

@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','book']

