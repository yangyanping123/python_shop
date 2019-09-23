__author__ = 'Administrator'
import xadmin
from xadmin import views
from .models import UserMessage
class UserMessageAdmin(object):
    pass
xadmin.site.register(UserMessage)