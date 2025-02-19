# from django.conf import settings
from django.contrib import admin

# 引入用户平台
from .models import *


# admin.site.site_header = settings.MAIN_CONFIG.get('site_header')
# admin.site.site_title = settings.MAIN_CONFIG.get('site_title')


class BaseInfoAdmin(admin.ModelAdmin):
    # fields = ('id', 'uuid', 'user_no', 'username', 'nickname', 'fullname', 'phone', 'email', 'user_type', 'privacies',
    #           'user_info', 'register_ip', 'register_time', 'is_delete')
    fieldsets = [
        ('用户基础信息', {'classes': 'collapse', 'fields': (
            ('id', 'uuid'), 'user_no', ('username', 'nickname'), 'fullname', ('phone', 'email'), 'user_type',
            ('user_info', 'privacies'), ('register_time', 'register_ip'), 'is_delete'
        )})
    ]
    list_display = (
        'id', 'uuid_short', 'user_no', 'username', 'nickname', 'fullname', 'phone', 'email', 'user_type',
        'user_info_short', 'privacies_short', 'register_ip', 'register_time', 'is_delete')
    list_display_links = ['username', 'phone', 'email']
    list_filter = ['user_type']
    search_fields = ('uuid', 'username', 'fullname', 'nickname', 'email', 'phone')
    readonly_fields = ['id', 'uuid']
    list_per_page = 20


class DetailInfoAdmin(admin.ModelAdmin):
    # fields = (
    #     'id', 'user', 'real_name', 'sex', 'birth', 'tags', 'signature', 'avatar', 'cover', 'id_card_type', 'id_card_no',
    #     'language', 'region_code', 'more',
    #     'field_1', 'field_2', 'field_3', 'field_4', 'field_5', 'field_6', 'field_7', 'field_8', 'field_9',
    #     'field_10', 'field_11', 'field_12', 'field_13', 'field_14', 'field_15'
    # )

    fieldsets = [
        ('用户详细信息', {'classes': 'collapse', 'fields': (
            'id', ('user', 'real_name'), ('sex', 'birth'), ('tags', 'signature'), ('avatar', 'cover'),
            ('id_card_type', 'id_card_no'), ('language', 'region_code'), 'more',
            ('field_1', 'field_2'), ('field_3', 'field_4'), ('field_5', 'field_6'), ('field_7', 'field_8'),
            ('field_9', 'field_10'), ('field_11', 'field_12'), ('field_13', 'field_14'), ('field_15')
        )})
    ]
    list_display = ('id', 'user_short', 'real_name', 'sex', 'birth', 'tags', 'avatar', 'cover', 'language', 'region_code',
                    )
    list_display_links = ['user_short']
    search_fields = ('user__username', 'user__fullname', 'real_name')
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class AuthAdmin(admin.ModelAdmin):
    fields = ('id', 'platform', 'user', 'password', 'salt', 'algorithm', 'token', 'ticket',
              'last_update_ip', 'create_time', 'update_time')
    list_display = ('platform', 'user', 'password', 'salt', 'algorithm', 'token_short',
                    'ticket_short', 'create_time', 'update_time')
    list_display_links = ['user']
    search_fields = ('user__username', 'user__fullname')
    list_filter = ['platform']
    readonly_fields = ['id', 'create_time', 'update_time']
    raw_id_fields = ['user']
    list_per_page = 20

    # def platform(self, obj):
    #     return obj.platform


class ExtendFieldAdmin(admin.ModelAdmin):
    fields = ('id', 'field', 'field_index', 'description', 'type', 'config', 'default', 'sort')
    list_display = ('field', 'field_index', 'description', 'type', 'config', 'default', 'sort')
    readonly_fields = ['id']
    list_per_page = 20


class AccessLogAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'ip', 'create_time', 'client_info', 'more',)
    list_display = ('user', 'ip', 'create_time', 'client_info',)
    readonly_fields = ['id', 'create_time']
    raw_id_fields = ['user']
    list_per_page = 20


class HistoryAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'field', 'old_value', 'new_value', 'create_time',)
    list_display = ('user', 'field', 'old_value', 'new_value', 'create_time',)
    readonly_fields = ['id', 'create_time']
    raw_id_fields = ['user']
    list_per_page = 20


class RestrictRegionAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'region_code',)
    list_display = ('user', 'region_code',)
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class PlatformAdmin(admin.ModelAdmin):
    fields = ('id', 'platform_id', 'platform_code', 'platform_name', 'root_category_value')
    list_display = ('id', 'platform_id', 'platform_code', 'platform_name', 'root_category_value')
    list_display_links = ['platform_code']
    search_fields = ('platform_id', 'platform_name', 'platform_code')
    list_per_page = 20


class PlatformsToUsersAdmin(admin.ModelAdmin):
    fields = ('user', 'platform', 'platform_user_id',)
    list_display = ('platform', 'user', 'platform_user_id',)
    list_filter = ['platform']
    # readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class ContactBookAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'friend', 'phone', 'phones', 'telephone', 'telephones',
              'email', 'qq', 'address', 'more', 'remarks')
    list_display = ('id', 'user', 'friend', 'phone', 'phones', 'telephone', 'telephones',
                    'email', 'qq', 'address', 'more', 'remarks')
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class UserSsoServeAdmin(admin.ModelAdmin):
    fields = ('id', 'sso_code', 'sso_name', 'sso_url', 'description', 'sso_appid', 'sso_account_id')
    list_display = ('id', 'sso_code', 'sso_name', 'sso_url', 'description')
    readonly_fields = ['id']
    list_per_page = 20


class UserSsoToUserAdmin(admin.ModelAdmin):
    fields = ('id', 'sso_serve', 'user', 'sso_unicode', 'sso_ticket', 'union_code',)
    list_display = ('id', 'sso_serve', 'user', 'sso_unicode', 'sso_ticket', 'union_code')
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class UserRelateTypeAdmin(admin.ModelAdmin):
    fields = ("id", "relate_key", "relate_name", "is_multipeople", "description",)
    list_display = ("id", "relate_key", "relate_name", "is_multipeople", "description",)
    readonly_fields = ['id']
    list_per_page = 20


class UserRelateToUserAdmin(admin.ModelAdmin):
    fields = ("id", "user", "with_user", "user_relate_type",)
    list_display = ("id", "user", "with_user", "user_relate_type",)
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


class UserBankCardsAdmin(admin.ModelAdmin):
    fields = ("id", "user", "bank_card_num", "open_account_bank")
    list_display = ("id", "user", "bank_card_num", "open_account_bank")
    readonly_fields = ['id']
    raw_id_fields = ['user']
    list_per_page = 20


admin.site.register(BaseInfo, BaseInfoAdmin)
admin.site.register(DetailInfo, DetailInfoAdmin)
admin.site.register(Auth, AuthAdmin)
admin.site.register(ExtendField, ExtendFieldAdmin)
# admin.site.register(AccessLog, AccessLogAdmin)
# admin.site.register(History, HistoryAdmin)
# admin.site.register(RestrictRegion, RestrictRegionAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(PlatformsToUsers, PlatformsToUsersAdmin)
# admin.site.register(Permission, PermissionAdmin)
# admin.site.register(PermissionValue, PermissionValueAdmin)
# admin.site.register(Group, GroupAdmin)
# admin.site.register(ContactBook, ContactBookAdmin)
admin.site.register(UserSsoServe, UserSsoServeAdmin)
admin.site.register(UserSsoToUser, UserSsoToUserAdmin)
# admin.site.register(UserRelateType, UserRelateTypeAdmin)
# admin.site.register(UserRelateToUser, UserRelateToUserAdmin)
admin.site.register(UserBankCards, UserBankCardsAdmin)
