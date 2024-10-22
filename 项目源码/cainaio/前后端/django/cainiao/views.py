from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *
from djangoProject.bean import R
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class CainiaoBasedOption(GenericAPIView):

    serializer_class = CainiaoBased_Serializer

    def get(self, request):
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))
        item = CainiaoBased.objects.all()[page * size - size:page * size]
        totalPage = CainiaoBased.objects.all().count() // size + 1
        return R.ok(data={
            'items': self.get_serializer(item, many=True).data,
            'totalPage': totalPage
        })
    def post(self, request):
        item = self.get_serializer(data=request.data)
        if item.is_valid():
            CainiaoBased.objects.filter(id=request.data.get('id')).update(**item.validated_data)
            return R.ok(data='修改成功')
        else:
            return R.fail(msg='修改失败, 请检查数据格式')

    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return R.fail(msg='删除失败, 请传入id')
        item = CainiaoBased.objects.filter(id=id)
        if item:
            item.delete()
            return R.ok(data='删除成功')
        else:
            return R.fail(msg='删除失败, 该数据不存在')

    def put(self, request):
        data = request.data
        item = self.get_serializer(data=data)
        if item.is_valid():
            item.save()
            return R.ok(data='新增成功')
        else:
            return R.fail(msg='新增失败, 请检查数据格式')
    
class DesignlistOption(GenericAPIView):

    serializer_class = Designlist_Serializer

    def get(self, request):
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))
        item = Designlist.objects.all()[page * size - size:page * size]
        totalPage = Designlist.objects.all().count() // size + 1
        return R.ok(data={
            'items': self.get_serializer(item, many=True).data,
            'totalPage': totalPage
        })
    def post(self, request):
        item = self.get_serializer(data=request.data)
        if item.is_valid():
            Designlist.objects.filter(id=request.data.get('id')).update(**item.validated_data)
            return R.ok(data='修改成功')
        else:
            return R.fail(msg='修改失败, 请检查数据格式')

    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return R.fail(msg='删除失败, 请传入id')
        item = Designlist.objects.filter(id=id)
        if item:
            item.delete()
            return R.ok(data='删除成功')
        else:
            return R.fail(msg='删除失败, 该数据不存在')

    def put(self, request):
        data = request.data
        item = self.get_serializer(data=data)
        if item.is_valid():
            item.save()
            return R.ok(data='新增成功')
        else:
            return R.fail(msg='新增失败, 请检查数据格式')
    
class UserLikeOption(GenericAPIView):

    serializer_class = UserLike_Serializer

    def get(self, request):
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))
        item = UserLike.objects.all()[page * size - size:page * size]
        totalPage = UserLike.objects.all().count() // size + 1
        return R.ok(data={
            'items': self.get_serializer(item, many=True).data,
            'totalPage': totalPage
        })
    def post(self, request):
        item = self.get_serializer(data=request.data)
        if item.is_valid():
            UserLike.objects.filter(id=request.data.get('id')).update(**item.validated_data)
            return R.ok(data='修改成功')
        else:
            return R.fail(msg='修改失败, 请检查数据格式')

    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return R.fail(msg='删除失败, 请传入id')
        item = UserLike.objects.filter(id=id)
        if item:
            item.delete()
            return R.ok(data='删除成功')
        else:
            return R.fail(msg='删除失败, 该数据不存在')

    def put(self, request):
        data = request.data
        item = self.get_serializer(data=data)
        if item.is_valid():
            item.save()
            return R.ok(data='新增成功')
        else:
            return R.fail(msg='新增失败, 请检查数据格式')
    
class WordOption(GenericAPIView):

    serializer_class = Word_Serializer

    def get(self, request):
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))
        item = Word.objects.all()[page * size - size:page * size]
        totalPage = Word.objects.all().count() // size + 1
        return R.ok(data={
            'items': self.get_serializer(item, many=True).data,
            'totalPage': totalPage
        })
    def post(self, request):
        item = self.get_serializer(data=request.data)
        if item.is_valid():
            Word.objects.filter(id=request.data.get('id')).update(**item.validated_data)
            return R.ok(data='修改成功')
        else:
            return R.fail(msg='修改失败, 请检查数据格式')

    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return R.fail(msg='删除失败, 请传入id')
        item = Word.objects.filter(id=id)
        if item:
            item.delete()
            return R.ok(data='删除成功')
        else:
            return R.fail(msg='删除失败, 该数据不存在')

    def put(self, request):
        data = request.data
        item = self.get_serializer(data=data)
        if item.is_valid():
            item.save()
            return R.ok(data='新增成功')
        else:
            return R.fail(msg='新增失败, 请检查数据格式')


class findAllWorld(GenericAPIView):

    serializer_class = Designlist_Serializer
    def get(self, request):
        #查询所有title
        title = Designlist.objects.values('title')
        #去重
        title = title.distinct()
        #存入数组
        title = [i['title'] for i in title]
        return R.ok(data=title)

class gitintiitle(GenericAPIView):

    serializer_class = Designlist_Serializer
    def get(self, request):
      title = request.GET.get('title')
      #根据title查询所有的name
      name = Designlist.objects.filter(title=title).values('name')
      #去重·
      name = name.distinct()
      return R.ok(data=name)

class gitinintiitle(GenericAPIView):

    serializer_class = Designlist_Serializer
    def get(self, request):
        name = request.GET.get('title')
        #如果name长度大于10，就取【】里面的内容
        if len(name)>10:
            #取【】里面的内容
            name = name[name.find('【')+1:name.find('】')]
        #如果有’学习‘就去掉
        if name.find('学习')!=-1:
            name = name.replace('学习','')
        print(name)

            
        #根据title查询所有的name
        content = Designlist.objects.filter(name__contains=name).values('design_name')
        print(content)
        #去掉\n\t
        content = [i['design_name'].replace('\n','').replace('\t','') for i in content]

        return R.ok(data=content)

class gitcontent(GenericAPIView):

        serializer_class = Designlist_Serializer
        def get(self, request):
            name = request.GET.get('name')

            # content = Designlist.objects.filter(design_name=name).values('content')
            # 模糊查询
            content = Designlist.objects.filter(design_name__contains=name).values('content')[0]['content']


            return R.ok(data=content)


class putlike(GenericAPIView):

    serializer_class = UserLike_Serializer
    def get(self, request):
        name= request.GET.get('name')
        data = request.GET.get('data')
        #如果有\n\t,空格,去掉
        data = data.replace('\n','').replace('\t','').replace(' ','')

        print(name)
        print(data)
        #根据name和data查询是否有数据
        item = UserLike.objects.filter(user=name,like=data)
        if item:
            return R.fail(data='已经存在')
        else:
            UserLike.objects.create(user=name,like=data)

            return R.ok(data="收藏成功")


#根据user查询userlike

class getlikebyid(GenericAPIView):

        serializer_class = UserLike_Serializer
        def get(self, request):
            name = request.GET.get('id')
            #根据name查询所有的like
            data = UserLike.objects.filter(user=name).values('like')
            #去重
            data = data.distinct()
            #存入数组
            data = [i['like'] for i in data]
            return R.ok(data=data)


class getNameByname(GenericAPIView):

        serializer_class = Designlist_Serializer

        def get(self, request):
            name = request.GET.get('title')
            print(name)
            # 根据title查询所有的name
            content = Designlist.objects.filter(name=name).values('name')
            print(content)

            return R.ok(data=content)


#读取数据库cainiao——base
class getcainiao(GenericAPIView):

    serializer_class = CainiaoBased_Serializer
    def get(self, request):
        #模糊查询数据
        user = request.GET.get('user')
        print(user)
        #查询user是否存在
        item = CainiaoBased.objects.filter(user=user)



        if item:
            pass
        else:
            CainiaoBased.objects.create(user=user, CSS3=0,HTML=0,
                                        Googlemap=0,Memcached=0,name=0,
                                        Git=0,Cpp=0,jQueryUI=0,NumPy=0,Julia=0,SQL=0,Scala=0,HTMLDOM=0,Rust=0,Linux=0,
                                        JavaScript=0, Maven=0,Bootstrap3=0,MySQL=0,MongoDB=0,Python2x=0,
                                        MVC=0,FontAwesome=0,XPath=0,JSON=0,Eclipse=0,PostgreSQL=0,jQuery=0,
                                        Designpatterns=0,Nodejs=0,Chartjs=0,JSP=0,Java=0,Docker=0,W3C=0,XLink=0,
                                        Foundation=0,Echarts=0,XQuery=0,Highcharts=0,Kotlin=0,Pandas=0,C=0,Razor=0,
                                        ASPNET=0,Scipy=0,XSLT=0,WebHosting=0,SQLite=0,AppML=0,Matplotlib=0,
                                        AngularJS=0,servlet=0,HTML5=0,ionic=0,DTD=0,PHP=0,Bootstrap4=0,SVG=0,
                                        XPointer=0,BrowserInformation=0,XSLFO=0,WebsiteBuilding=0,jQueryMobile=0,
                                        Vue3=0,TCPIP=0,Redis=0,SOAP=0,Swift=0,algorithms=0,WebService=0,Perl=0,
                                        ASP=0,RDF=0,Svn=0,VBScript=0,XML=0,Vuejs=0,AJAX=0,WebPages=0,Django=0,
                                        TypeScript=0,c_s=0,XMLDOM=0,Bootstrap5=0,Python=0,WebsiteQuality=0,Go=0,
                                        WSDL=0,CSS=0,XMLSchema=0,RSS=0,HTTP=0,R=0,WebForms=0,Markdown=0,Lua=0,
                                        AngularJS2=0,React=0,Ruby=0,regular=0)
        #      CSS3=0,HTML=0,
        #                                         Googlemap=0,Memcached=0,name=0,
        #                                         Git=0,Cpp=0,jQueryUI=0,NumPy=0,Julia=0,SQL=0,Scala=0,HTMLDOM=0,Rust=0,Linux=0,
        #                                         JavaScript=0, Maven=0,Bootstrap3=0,MySQL=0,MongoDB=0,Python2x=0,
        #                                         MVC=0,FontAwesome=0,XPath=0,JSON=0,Eclipse=0,PostgreSQL=0,jQuery=0,
        #                                         Designpatterns=0,Nodejs=0,Chartjs=0,JSP=0,Java=0,Docker=0,W3C=0,XLink=0,
        #                                         Foundation=0,Echarts=0,XQuery=0,Highcharts=0,Kotlin=0,Pandas=0,C=0,Razor=0,
        #                                         ASPNET=0,Scipy=0,XSLT=0,WebHosting=0,SQLite=0,AppML=0,Matplotlib=0,
        #                                         AngularJS=0,servlet=0,HTML5=0,ionic=0,DTD=0,PHP=0,Bootstrap4=0,SVG=0,
        #                                         XPointer=0,BrowserInformation=0,XSLFO=0,WebsiteBuilding=0,jQueryMobile=0,
        #                                         Vue3=0,TCPIP=0,Redis=0,SOAP=0,Swift=0,algorithms=0,WebService=0,Perl=0,
        #                                         ASP=0,RDF=0,Svn=0,VBScript=0,XML=0,Vuejs=0,AJAX=0,WebPages=0,Django=0,
        #                                         TypeScript=0,c_s=0,XMLDOM=0,Bootstrap5=0,Python=0,WebsiteQuality=0,Go=0,
        #                                         WSDL=0,CSS=0,XMLSchema=0,RSS=0,HTTP=0,R=0,WebForms=0,Markdown=0,Lua=0,
        #                                         AngularJS2=0,React=0,Ruby=0,regular=0
        #     )
        demo = ['CSS3','HTML','Googlemap','Memcached','name','Git','Cpp','jQueryUI','NumPy','Julia','SQL','Scala','HTMLDOM','Rust','Linux','JavaScript','Maven','Bootstrap3','MySQL','MongoDB','Python2x','MVC','FontAwesome','XPath','JSON','Eclipse','PostgreSQL','jQuery','Designpatterns','Nodejs','Chartjs','JSP','Java','Docker','W3C','XLink','Foundation','Echarts','XQuery','Highcharts','Kotlin','Pandas','C','Razor','ASPNET','Scipy','XSLT','WebHosting','SQLite','AppML','Matplotlib','AngularJS','servlet','HTML5','ionic','DTD','PHP','Bootstrap4','SVG','XPointer','BrowserInformation','XSLFO','WebsiteBuilding','jQueryMobile','Vue3','TCPIP','Redis','SOAP','Swift','algorithms','WebService','Perl','ASP','RDF','Svn','VBScript','XML','Vuejs','AJAX','WebPages','Django','TypeScript','c_s','XMLDOM','Bootstrap5','Python','WebsiteQuality','Go','WSDL','CSS','XMLSchema','RSS','HTTP','R','WebForms','Markdown','Lua','AngularJS2','React','Ruby','regular']
         #根据demo模糊查询当前用户的收藏数据,并且统计每个收藏的次数
        for d in demo:
            #统计数量
            count = UserLike.objects.filter(user=user,like__contains=d).count()
            #更新数据
            CainiaoBased.objects.filter(user=user).update(**{d:count})
        return R.ok(data='ok')


#根据user推荐
class getTuijianForUser(GenericAPIView):


    def get(self, request):
        user = request.GET.get('user')
        #查询所有cainiao_based
        data = CainiaoBased.objects.all()
        #将data转换为dp
        item_based = pd.DataFrame(list(data.values()))
        item_based.set_index('user', inplace=True)
        item_similar = cosine_similarity(item_based.T)
        item_similar_df = pd.DataFrame(item_similar, index=item_based.columns, columns=item_based.columns)

        def top_k_similar_items(similar_df, item, k=10):
            return similar_df[item].sort_values(ascending=False)[:k].to_dict()

        def get_user_item_score(user, item, similar_df):
            similar_items = top_k_similar_items(similar_df, item)
            user_item_score = 0
            for item, score in similar_items.items():
                user_item_score += item_based.loc[user, item] * score
            return user_item_score

        def recommend(user, similar_df):
            user_items = item_based.loc[user]
            user_items = user_items[user_items == 0].index
            scores = []
            for item in user_items:
                score = get_user_item_score(user, item, similar_df)
                scores.append(score)
            return pd.Series(scores, index=user_items).sort_values(ascending=False)


        return R.ok(data=recommend(user, item_similar_df).index.tolist())



#根据name查询name
class getname(GenericAPIView):

    serializer_class = Designlist_Serializer
    def get(self, request):
        name = request.GET.get('name')
        #模糊查询
        data = Designlist.objects.filter(name__contains=name).values('name')
        #去重
        data = data.distinct()
        #存入数组
        data = [i['name'] for i in data]
        return R.ok(data=data)


class TitleCountOption(GenericAPIView):
    serializer_class = TitleCount_Serializer

    def get(self, request):
        page = int(request.GET.get('page', 1))
        size = int(request.GET.get('size', 10))
        item = TitleCount.objects.all()[page * size - size:page * size]
        totalPage = TitleCount.objects.all().count() // size + 1
        return R.ok(data={
            'items': self.get_serializer(item, many=True).data,
            'totalPage': totalPage
        })

    def post(self, request):
        item = self.get_serializer(data=request.data)
        if item.is_valid():
            TitleCount.objects.filter(id=request.data.get('id')).update(**item.validated_data)
            return R.ok(data='修改成功')
        else:
            return R.fail(msg='修改失败, 请检查数据格式')

    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return R.fail(msg='删除失败, 请传入id')
        item = TitleCount.objects.filter(id=id)
        if item:
            item.delete()
            return R.ok(data='删除成功')
        else:
            return R.fail(msg='删除失败, 该数据不存在')

    def put(self, request):
        data = request.data
        item = self.get_serializer(data=data)
        if item.is_valid():
            item.save()
            return R.ok(data='新增成功')
        else:
            return R.fail(msg='新增失败, 请检查数据格式')


#查询所有title_count
class TitleCountAll(GenericAPIView):

        serializer_class = TitleCount_Serializer
        def get(self, request):
            #查询所有title_count
            data = TitleCount.objects.all().values('title','count')
            #去重
            data = data.distinct()
            #存入数组
            x = [i['title'] for i in data]
            y = [i['count'] for i in data]
            data = {'x':x,'y':y}
            return R.ok(data=data)


#查询word
class getAllWord(GenericAPIView):
    serializers = Word_Serializer
    def get(self,request):
        data = Word.objects.all().values('word','count')
        #排序
        data = data.order_by('-count')[0:6]
        data_return= []
        for i in data:
            i_dist={}
            i_dist['name'] = i['word']
            i_dist['value'] = i['count']
            data_return.append(i_dist)
        return R.ok(data=data_return)

class getAllWordByc(GenericAPIView):
    serializers = Word_Serializer
    def get(self,request):
        data=['Java','Python','C','C++','C#','JavaScript','PHP','SQL','Go','Swift','R']
        #根据data查询所有的count
        data = Word.objects.filter(word__in=data).values('word','count')
        #排序
        data = data.order_by('-count')

        for i in data:
            i['name'] = i['word']
            i['value'] = i['count']
            del i['word']
            del i['count']


        return R.ok(data=data)


