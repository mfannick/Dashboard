from django.contrib import admin
from .models import Profile,Question,Answer,Vote,Approved,Category
from django import template
from django.db.models import Count

# Register your models here.
    
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image','email']
    list_filter=['user']

class QuestionAdmin(admin.ModelAdmin):
    list_display=['user','title','content','snippet','category','countCategory']
    # def countCategory(self,obj,category):
    #     return Count(self.model.filter(category=category))
    # countCategory.short_description = 'count'
    def countCategory(self, obj):
        question=obj.category
        print(obj)
        print(Question.objects.filter(category=question).count()) 
    countCategory.short_description = 'count'
    

class AnswerAdmin(admin.ModelAdmin):
    list_display=['user','question','answer']

class VoteAdmin(admin.ModelAdmin):
    list_display=['name','vote']

class ApprovedAdmin(admin.ModelAdmin):
    list_display=['name','approve','score']

admin.site.register(Category)   
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Vote,VoteAdmin)
admin.site.register(Approved,ApprovedAdmin)
