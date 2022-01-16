from rest_framework.views import APIView
from rest_framework import filters
from Core.models import Film
from .serializers import FilmSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination



'''Override get_search_fields method of SearchFilter'''
class DynamicSearch(filters.SearchFilter,):
    def get_search_fields(self,view, request):
        return request.GET.getlist('search_fields',[])

'''Override page_size_query_param attribute of PageNumberPagination'''
class CustomizePagination(PageNumberPagination):
    page_size_query_param = 'limit'


"""Pagination Handler"""
class PaginationHanlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is  None:
                 self._paginator =None
            else :
                self._paginator = self.pagination_class()
        else :
            pass

        return self._paginator

    def  paginate_queryset(self,queryset):
        if self.paginator is None:
            return None
        
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self,data):
        if self.paginator is None:
            raise "Paginator is None"
        return self.paginator.get_paginated_response(data)



class SearchFilm(APIView,PaginationHanlerMixin):
    authentication_classes = ()
    def __init__(self,):
        APIView.__init__(self)
        self.search_class=DynamicSearch
        self.pagination_class=CustomizePagination

    def filter_queryset(self,queryset):
      filterd_queryset=self.search_class().filter_queryset(self.request,queryset,self)
      return filterd_queryset


    def get(self, request):
        films= Film.objects.all()
        filtered_queryset=self.filter_queryset(films)
        #Get appropriate results for each page
        results=self.paginate_queryset(filtered_queryset)
        if(results is not None):
            serializer=FilmSerializer(results,many=True)
            serializer=self.get_paginated_response(serializer.data)
        else :
            serializer=FilmSerializer(filtered_queryset,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



