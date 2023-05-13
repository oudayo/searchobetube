# Create your views here.

from rest_framework import generics
from .models import Course
from django.db.models import Q
from .serializers import CourseSerializer
import os
import json
from pathlib import Path




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
            query=query.lower()
            queryset = Course.objects.filter((Q(title__icontains=query) | Q(snippet__icontains=query)) & Q(level=level))
            print(len(queryset))

            if len(queryset) > 15:

                return queryset
            else:
                query_new=query.replace(' ', '')
                os.system(f'python scrap/start.py --query {query_new} --level {level}')

                with open(os.path.join(BASE_DIR, 'resultat.json')) as f:
                    try:
                        data = json.load(f)
                    except:
                        return []
                    for element in data:
                        print('*******************************************************************')
                        print(element)
                        try:
                            c = Course(title=element['Course_name'], link=element['Link'], snippet=element['Snippet'],
                                       image=element['images'], level=level,totalResults=element['totalResults'],count=element['count'],
                                       startIndex=element['startIndex'])
                            # if c.image == None:
                            #     c.image = 'gezgzrg'
                            c.save()
                        except :
                            print('file saved')
                queryset = Course.objects.filter(
                    (Q(title__icontains=query) | Q(snippet__icontains=query)) & Q(level=level))

                return queryset













