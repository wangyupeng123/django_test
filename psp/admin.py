from django.contrib import admin
from psp.models import  BookInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpup_date']
    list_per_page = 10
    # actions_on_bottom = True # 下拉列表选项功能栏，页面的动作栏。底部显示
    actions_on_top = False
    list_filter = ['btitle']
    search_fields = ['btitle'] # 搜索框顶部显示


admin.site.register(BookInfo, BookInfoAdmin)