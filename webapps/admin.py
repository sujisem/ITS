from django.contrib import admin
from webapps.models import Answers,Question,Replies,Session,Stdintxn,Student

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass
@admin.register(Replies)
class RepliesAdmin(admin.ModelAdmin):
    pass

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass

@admin.register(Stdintxn)
class StdintxnAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass




"""     # list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity']
admin.site.register(Answers)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Replies)
admin.site.register(Session)
admin.site.register(Stdintxn)
admin.site.register(Student)
"""
