from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DynamicPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link(),
               'params': self.request.build_absolute_uri().split('?')[1]
            },
            'count': self.page.paginator.count,
            'current_page': self.page.number, 
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })