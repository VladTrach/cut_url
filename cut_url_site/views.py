from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.views import View
from django.views.generic import CreateView, TemplateView
from rest_framework.reverse import reverse

from core.utils import get_full_url, get_shortcut_by_id
from cut_url_site.forms import NewShortcutForm


class ShortcutRedirect(View):

    def get(self, request, shortcut):
        full_url = get_full_url(shortcut)
        if full_url:
            return HttpResponseRedirect(full_url)
        return HttpResponseBadRequest()


class NewShortcutFormView(CreateView):
    template_name = 'new_shortcut.html'
    form_class = NewShortcutForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('site-shortcut', kwargs={'pk': self.object.pk})


class ShortcutView(TemplateView):
    template_name = 'shortcut.html'

    def get_context_data(self, **kwargs):
        context = super(ShortcutView, self).get_context_data(**kwargs)
        shortcut = get_shortcut_by_id(kwargs['pk'])
        context['shortcut_url'] = f'{settings.BASE_URL}/{shortcut}'
        return context
