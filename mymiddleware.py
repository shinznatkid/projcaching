from django.http import Http404


class ChromeCanSee(object):

    def process_request(self, request):
        print request.META['HTTP_USER_AGENT']
        if 'Chrome' not in request.META['HTTP_USER_AGENT']:
            raise Http404
