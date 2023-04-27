# Create your views here.

from rest_framework import generics
from .models import Course
from django.db.models import Q
from .serializers import CourseSerializer
import os
import json
from pathlib import Path

# import BASE_DIR
from django.conf import settings

# from search_api.settings import BASE_DIR

# class SearchResultsView(generics.ListAPIView):
#     serializer_class = CourseSerializer
#     def get_queryset(self):
#         query = self.request.query_params.get('query', None)
#         level = self.request.query_params.get('level', None)
#         if query:
#             queryset = Course.objects.filter( (Q(title__icontains=query) | Q(level=level))  & Q(level=level))
#             if len(queryset) == 0:  # if the title doesnt exist in the database
#                 cwd = os.path.join(BASE_DIR, "api/demoscrap/start.py")
#                 os.system('{} {} --query {} --level {}'.format('python', cwd, query, level))
#                 f = open(os.path.join(BASE_DIR, 'finalll.json'))
#                 data = json.load(f)
#                 for element in data:
#                     print(element)
#                     c = Course(title=element['Course_name'], snippet=element['Snippet'], link=element['Link'], image=element['images'], level=level)
#                     c.save()
#                 f.close()
#                 os.remove(os.path.join(BASE_DIR, 'finalll.json'))

#         queryset = Course.objects.filter( (Q(title__icontains=query) | Q(level=level))  & Q(level=level))
#         return queryset
# exemple de recherche http://127.0.0.1:8000/courses/?q=s


class SearchResultsView(generics.ListAPIView):
    serializer_class = CourseSerializer


    def get_queryset(self):
        BASE_DIR = Path(__file__).resolve().parent.parent
        print(BASE_DIR)
        try:
            os.remove(os.path.join(BASE_DIR, 'resultat.json'))
        except FileNotFoundError:
            print('file not fouund')
        query = self.request.query_params.get('query', None)
        level = self.request.query_params.get('level', None)
        if query:
            queryset = Course.objects.filter((Q(title__icontains=query) | Q(snippet__icontains=query)) & Q(level=level))
            if len(queryset) != 0:
                return queryset
            else:
                os.system(f'python scrap/start.py --query {query} --level {level}')
                print('i m here')
                with open(os.path.join(BASE_DIR, 'resultat.json')) as f:
                    data = json.load(f)
                    for element in data:

                        c = Course(title=element['Course_name'], link=element['Link'], snippet=element['Snippet'],
                                   image=element['images'], level=level,totalResults=element['totalResults'],count=element['count'],
                                   startIndex=element['startIndex'])
                        # if c.image == None:
                        #     c.image = 'gezgzrg'
                        c.save()
                queryset = Course.objects.filter(
                    (Q(title__icontains=query) | Q(snippet__icontains=query)) & Q(level=level))
                return queryset













