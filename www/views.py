#coding=utf-8
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.views import generic

from we.utils.ipgeo import ipgeo
from we.utils.navbar import get_navbar
from www.models import MoreService

from markdown import markdown

# 首页
def index(request):
    result = get_navbar(request)
    result.update({'more_service_list': get_services(request)})

    return render_to_response('www/index.html', result)

# 更多服务
class MoreServicesView(generic.ListView):
    template_name = 'www/more_services.html'
    context_object_name = 'more_service_list'

    def get_queryset(self):
        return get_services(self.request)

    def get_context_data(self, **kwargs):
        context = super(MoreServicesView, self).get_context_data(**kwargs)
        context.update(get_navbar(self.request))
        return context

# 获得更多服务列表
def get_services(request):
    services = []

    if ipgeo(request):
        more_services = cache.get('more_services__intranet')
        if not more_services:
            more_services = MoreService.objects.filter(intranet=True).order_by('order')
            cache.set('more_services__intranet', more_services, 600)
    else:
        more_services = cache.get('more_services__internet')
        if not more_services:
            more_services = MoreService.objects.filter(internet=True).order_by('order')
            cache.set('more_services__internet', more_services, 600)

    for more_service in more_services:
        services.append({
            'key': more_service.key,
            'title': more_service.title,
            'subtitle': more_service.subtitle,
            'content': markdown(more_service.content),
        })

    return services
