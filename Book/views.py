from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
import urllib.parse
import json
# Create your views here.

class Test(APIView):
    def get(self,request):
        a=request.GET['a']
        res={
            'success':True,
            'data':a
        }
        return Response(res)


class bookname(APIView):
    def get(self,request):
        name_dict={}
        book=request.GET['bookname']
        if book == '鬼吹灯':
            names=models.Book.objects.all()
            for name in names:
                name_dict[name.id]=name.book_name
            res={
                'success': True,
                'bookname': name_dict
            }
        else:
            res={
                'fail':True
            }
        return Response(res)

class brief(APIView):
    def get(self,request):
        allid=[]
        id=request.GET['bookid']
        queries=models.Book.objects.all()
        for query in queries:
            allid.append(query.id)
        if int(id) in allid:
            info=models.Book.objects.get(id=id)
            res={
                'success':True,
                'data':info.book_brief
            }
        else:
            res={
                'fail':True
            }
        return Response(res)

class chapternames(APIView):
    def get(self,request):
        allid = []
        chapter_dict={}
        id=request.GET['bookid']
        queries = models.Book.objects.all()
        for query in queries:
            allid.append(query.id)
        if int(id) in allid:
            info=models.Book.objects.get(id=id)
            chapter_infos=models.Chapter.objects.filter(book_name=info.book_name)\
                .order_by('chapter_id')
            for chapter_info in chapter_infos:
                chapter_dict[chapter_info.chapter_id]=chapter_info.chapter_name
            res={
                'success':True,
                'bookname':{
                    info.book_name:chapter_dict
                }
            }
        else:
            res={
                'fail':True,
            }
        return Response(res)

class Article(APIView):
    def get(self,request):
        allid=[]
        allchapterid=[]
        id=request.GET['bookid']
        chapter_id=request.GET['chapterid']
        queries=models.Book.objects.all()
        for query in queries:
            allid.append(query.id)
        if int(id) in allid:
            bookname=models.Book.objects.get(id=id).book_name
            for chapter in models.Chapter.objects.filter(book_name=bookname):
                allchapterid.append(chapter.chapter_id)
            if int(chapter_id) in allchapterid:
                chapter_path=models.Chapter.objects.get(book_name=bookname,
                                                        chapter_id=chapter_id).chapter_path
                with open(chapter_path,'r',encoding='utf-8') as f:
                    article_info=f.readlines()
                res={
                    'success':True,
                    'data':{
                        'bookname':bookname,
                        'article' :''.join(article_info)
                    }
                }
            else:
                res={
                    'fail':True
                }
        else:
            res={
                'fail': True
            }

        return Response(res)




