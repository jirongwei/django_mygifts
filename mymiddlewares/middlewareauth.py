from django.http import HttpResponse,JsonResponse

from django.utils.deprecation import MiddlewareMixin

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print('process_request')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('process_view')

    def process_exception(self,request,exception):
        print('555')


    def process_response(self,request,response):
        print('process_response')
        return response