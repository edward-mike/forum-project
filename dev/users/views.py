from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

from dev.users.services import User


# Create your views here.
@login_required
def user_profile(request,username,template_name="accounts/user/user.html"):
	"""
	View : user_profile

	Response data :

	[*] user articles

	[*] commented articles as done in Hashnode.com

	[*] followers & following counts

	[*] buttons - follow/unfollow (not owner)
			
	"""

	try:
		user = User._default_manager.get(username__iexact=username)
		print(user.full_name.title())
	except User.DoesNotExist:
		raise Http404

	# user data.



	template_data = {
	"user" : user,
	}
	return TemplateResponse(request,template_name,template_data)