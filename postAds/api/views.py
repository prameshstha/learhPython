from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from postAds.models import PostAd
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from .serializers import PostAdListSerializer, PostAdDetailSerializer, PostAdCreateSerializer
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination


class PostCreateAPIView(CreateAPIView):
    queryset = PostAd.objects.all()
    serializer_class = PostAdCreateSerializer


# for all the list view
class PostListAPIView(ListAPIView):
    serializer_class = PostAdListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['post_title', 'post_category', 'post_body', 'id']
    pagination_class = PostPageNumberPagination

    # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostAd.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(post_title__icontains=query) |
                Q(post_category__icontains=query)
            ).distinct()
        return queryset_list


# for all the details view
# can be changed as required field and can be same
class PostDetailAPIView(RetrieveAPIView):
    queryset = PostAd.objects.all()
    serializer_class = PostAdDetailSerializer
    lookup_field = 'pk'


class PostUpdateAPIView(UpdateAPIView):
    queryset = PostAd.objects.all()
    serializer_class = PostAdDetailSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = PostAd.objects.all()
    serializer_class = PostAdDetailSerializer
