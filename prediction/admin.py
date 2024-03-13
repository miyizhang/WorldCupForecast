# admin.py
from .models import MatchInfo
from django.contrib import admin
from django.urls import path
from .views import update_match_info, admin_home, delete_match_info, edit_match_info


@admin.register(MatchInfo)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['match_date', 'match_time', 'team_a', 'team_b']


class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('update_match_info/', self.admin_view(update_match_info), name='update_match_info'),
            path('home/', self.admin_view(admin_home), name='admin_home'),
            path('edit_match_info/<int:match_id>', self.admin_view(edit_match_info), name='edit_match_info'),
            path('delete_match_info/<int:match_id>', self.admin_view(delete_match_info), name='delete_match_info')
        ]
        return custom_urls + urls


custom_admin_site = CustomAdminSite(name='custom_admin')
