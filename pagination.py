from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict

class Pagination(PageNumberPagination):
    """
    Custom pagination to paginate get data
    """
    def paginate_queryset(self, queryset, request, view=None):
        self.page_size_query_param = 'page_size'
        return super(Pagination, self).paginate_queryset(queryset, request, view)