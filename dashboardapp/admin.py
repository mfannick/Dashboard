from django.contrib import admin
from .models import Profile,Question,Answer,Vote,Approved,Category
from django import template
from django.db.models import Count


# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category']
    # def count(self,obj):
    #    return Count(obj.category)

    # def countCategory(self, obj):
    #     return obj.category.count('category')
    # countCategory.short_description = 'count'
    list_filter=['category']
    
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','image','email']

class QuestionAdmin(admin.ModelAdmin):
    list_display=['user','title','content','snippet','category','countCategory']
    # def countCategory(self,obj,category):
    #     return Count(self.model.filter(category=category))
    # countCategory.short_description = 'count'
    def countCategory(self, obj):
        return Count(obj.category)
    countCategory.short_description = 'count'
    
    

    

class AnswerAdmin(admin.ModelAdmin):
    list_display=['user','question','answer']

class VoteAdmin(admin.ModelAdmin):
    list_display=['name','vote']

class ApprovedAdmin(admin.ModelAdmin):
    list_display=['name','approve','score']

admin.site.register(Profile,ProfileAdmin)
# admin.site.register(Category)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Vote,VoteAdmin)
admin.site.register(Approved,ApprovedAdmin)