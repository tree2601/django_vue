from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'cainiao后台管理'

class CainiaoBasedAdmin(admin.ModelAdmin):
    list_display = ['user','CSS3','HTML','Googlemap','Memcached','name','Git','Cpp','jQueryUI','NumPy','Julia','SQL','Scala','HTMLDOM','Rust','Linux','JavaScript','Maven','Bootstrap3','MySQL','MongoDB','Python2x','MVC','FontAwesome','XPath','JSON','Eclipse','PostgreSQL','jQuery','Designpatterns','Nodejs','Chartjs','JSP','Java','Docker','W3C','XLink','Foundation','Echarts','XQuery','Highcharts','Kotlin','Pandas','C','Razor','ASPNET','Scipy','XSLT','WebHosting','SQLite','AppML','Matplotlib','AngularJS','servlet','HTML5','ionic','DTD','PHP','Bootstrap4','SVG','XPointer','BrowserInformation','XSLFO','WebsiteBuilding','jQueryMobile','Vue3','TCPIP','Redis','SOAP','Swift','algorithms','WebService','Perl','ASP','RDF','Svn','VBScript','XML','Vuejs','AJAX','WebPages','Django','TypeScript','c_s','XMLDOM','Bootstrap5','Python','WebsiteQuality','Go','WSDL','CSS','XMLSchema','RSS','HTTP','R','WebForms','Markdown','Lua','AngularJS2','React','Ruby','regular','id']
    search_fields = []
    list_filter = []
        
class DesignlistAdmin(admin.ModelAdmin):
    list_display = ['id','title','name','url','design_name','design_url','content']
    search_fields = []
    list_filter = []
        
class UserLikeAdmin(admin.ModelAdmin):
    list_display = ['user','like','id']
    search_fields = []
    list_filter = []
        
class WordAdmin(admin.ModelAdmin):
    list_display = ['word','count','id']
    search_fields = []
    list_filter = []
        
admin.site.register(CainiaoBased,CainiaoBasedAdmin)
admin.site.register(Designlist,DesignlistAdmin)
admin.site.register(UserLike,UserLikeAdmin)
admin.site.register(Word,WordAdmin)
