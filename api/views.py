from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.generics import GenericAPIView

from api.serializers import ShortcutSerializer
from core.utils import get_full_url


class FullUrl(GenericAPIView):
    serializer_class = ShortcutSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        shortcut = serializer.validated_data['shortcut']
        full_url = get_full_url(shortcut)

        if full_url:
            return JsonResponse(
                {'status': 'ok', 'full_url': full_url},
                status=status.HTTP_200_OK
            )
        return HttpResponseBadRequest()
