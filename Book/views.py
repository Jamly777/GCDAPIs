from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
import os
# Create your views here.

class Test(APIView):
    def get(self,request):
        a=request.GET['a']
        res={
            'success':True,
            'data':a
        }
        return Response(res)

class series(APIView):
    def get(self,request):
        list=[]
        queries=models.Image.objects.filter(book_id=0)
        for query in queries:
            list.append({'name':query.series,'image':query.url})
        res={
            'success':True,
            'series':list
        }
        return Response(res)

class bookname(APIView):
    def get(self,request):
        name_list=[]
        book=request.GET['series']
        if book == '鬼吹灯':
            names=models.Book.objects.filter(series=book)
            for name in names:
                image=models.Image.objects.get(book_id=name.id).url
                name_list.append({'id':name.id,'bookname':name.book_name,'image':image})
            res={
                'success': True,
                'books': name_list
            }
        else:
            res={
                'fail':True,
                'info': '资源更新中'
            }
        return Response(res)

class brief(APIView):
    def get(self,request):
        allid=[]
        allseries=[]
        series=request.GET['series']
        id=request.GET['bookid']
        queries=models.Book.objects.all()
        for query in queries:
            allseries.append(query.series)
            allid.append(query.id)
        if series in allseries:
            if int(id) in allid:
                info=models.Book.objects.get(id=id)
                res={
                    'success':True,
                    'data':{
                        'bookname':info.book_name,
                        'brief':info.book_brief
                    }
                }
            else:
                res={
                    'fail':True,
                    'info':'暂无此资源'
                }
        else:
            res = {
                'fail': True,
                'info': '暂无此资源'
            }
        return Response(res)

class chapternames(APIView):
    def get(self,request):
        allid = []
        chapter_list=[]
        id=request.GET['bookid']
        queries = models.Book.objects.all()
        for query in queries:
            allid.append(query.id)
        if int(id) in allid:
            info=models.Book.objects.get(id=id)
            chapter_infos=models.Chapter.objects.filter(book_name=info.book_name)\
                .order_by('chapter_id')
            for chapter_info in chapter_infos:
                chapter_list.append({'chapter_id':chapter_info.chapter_id,'chapternames':chapter_info.chapter_name})
            res={
                'success':True,
                'bookname':{
                    info.book_name:chapter_list
                }
            }
        else:
            res={
                'fail':True,
                'info': '暂无此资源'
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
                chapter_info=models.Chapter.objects.get(book_name=bookname,
                                                        chapter_id=chapter_id)
                with open(chapter_info.chapter_path,'r',encoding='utf-8') as f:
                    article_info=f.readlines()
                res={
                    'success':True,
                    'data':{
                        'bookname':bookname,
                        'chapter' :chapter_info.chapter_name,
                        'article' :''.join(article_info)
                    }
                }
            else:
                res={
                    'fail':True,
                    'info': '暂无此资源'
                }
        else:
            res={
                'fail': True,
                'info': '暂无此资源'
            }

        return Response(res)




