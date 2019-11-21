from django.contrib import admin
from .models import Profile,Question,Answer,Vote,Approved,Category
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image','email']
    list_filter=['user']

class QuestionAdmin(admin.ModelAdmin):
    list_display=['user','title','content','snippet']
    
class AnswerAdmin(admin.ModelAdmin):
    list_display=['user','question','answer']

class VoteAdmin(admin.ModelAdmin):
    list_display=['name','vote']

class ApprovedAdmin(admin.ModelAdmin):
    list_display=['name','approve','score']

    
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Category)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Vote,VoteAdmin)
admin.site.register(Approved,ApprovedAdmin)