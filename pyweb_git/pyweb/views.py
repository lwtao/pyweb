# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2013

@author: kevin
'''
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,RequestContext,Context
from django.shortcuts import render_to_response
import url_conf 
log_file_dir='/root/jump_log/'
#log_file_dir='g://'
def show(request):
    urls_list=url_conf.get_all_url()
    html="""<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<style>
.url{width: 70%;height: 30px;font-size: 18px;}
.url_w{width: 2%;height: 30px;font-size: 18px;}
</style>
<script type="text/javascript" src="http://upcdn.b0.upaiyun.com/libs/jquery/jquery-1.9.0.min.js"></script>
</head>
<body>
<form action="/modify_swqgerz/" method="post" style="width: 80%">
{% csrf_token %}
{% for item  in urls %}
<input name="url" value="{{item.0}}" class="url" >&nbsp;
<input name="url_w" value="{{item.1}}" class="url_w" ><label style="font-size:20px;">%</label>
{% endfor %}
<div style="display:block">
<input type="button" value="add" onclick="add(this);return false;" >
<input type="submit" value="save">
</div>
</form>
<a href="/jump/" target="_blank">外链测试</a><br/>
<a href="/jump_tongji/{{yesterday}}" target="_blank">看昨天统计</a><br/>
<a href="/jump_tongji/{{today}}" target="_blank">看今天统计</a><br/>
<script>
function add(elem){
    var html='<input name="url" value="" class="url" >&nbsp;<input name="url_w" value="" class="url_w" ><label style="font-size:20px;">%</label>';
    $(elem).parent().before(html);
}
</script>
</body>
</html>
    """
    t=Template(html)
    today=datetime.date.today()
    yesterday=datetime.date.today()+datetime.timedelta(days=-1)
    c=RequestContext(request,{'urls':urls_list,'today':str(today),'yesterday':str(yesterday)})
    return HttpResponse(t.render(c))

def modify(request):
    '''url=request.POST['url_w']'''
    '''url=url.strip()'''
    '''url_conf.save_url('str');'''
    url_=request.POST.getlist('url')
    url_w_=request.POST.getlist('url_w')
    url_str=''
    for i in range(len(url_)):
        if(url_[i].strip()!='') and (url_w_[i].strip()!=''):
            try:
                t_url_w=int(url_w_[i].strip())
                t_url=url_[i].strip()
                if (not t_url.startswith('http:') and not t_url.startswith('https:')):
                    t_url='http://'+t_url
                url_str+=t_url+' '+url_w_[i].strip()+'\n'
            except ValueError: 
                print ValueError
    url_conf.save_url(url_str)
    return HttpResponseRedirect('/show_xoljua/')

def jump(request):
    url=url_conf.get_url().strip()
    try:
       import datetime
       today=datetime.date.today()
       log_file=open(log_file_dir+str(today),'a')
       log_file.write(url+' '+request.META.get('REMOTE_ADDR')+'\n')
    finally:
        log_file.close()
    return HttpResponseRedirect(url)

def zdx_test(request):
    height=request.GET['height']
    height=int(height)/100.0
    weight =request.GET['weight']
    weight=int(weight)
    bmi=(weight/(height**2))
    my_dict=dict()
    if bmi<18.5:
        my_dict['desc']='偏瘦'
    elif bmi>=18.5 and bmi<24.0:
        my_dict['desc']='健康'
    elif bmi>=18.5 and bmi<24.0:
        my_dict['desc']='超重'
    elif bmi>=28.0:
        my_dict['desc']='肥胖'
    if bmi>=18.5:
        my_dict['show_']=True
    else:
        my_dict['show_']=False    
    html1= '<strong class=\"reasonShow\">@</strong><span>+</span>'
    html= ''
    ck=request.GET.getlist('ck')
    if (len(ck) >0) :
        if '1' in ck or '2' in ck:
            html+=html1.replace('@','进食不科学')
        if '3' in ck:
            html+=html1.replace('@','情绪致胖')
        if '4' in ck:
            html+=html1.replace('@','缺乏运动')
        if '5' in ck:
            html+=html1.replace('@','生理遗传')
        if '6' in ck:
            html+=html1.replace('@','代谢不足')  
        if html.endswith('<span>+</span>'):
            html=html[:-14]
    my_dict['html']=html
    #return HttpResponse(html)
    return render_to_response('test.html',my_dict)
    

def jump_tongji(request,select_date):
    reslut_map=tongji(select_date)
    html="""
    <html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<style>
table{ border:1px solid #ccc; border-collapse:collapse; font-size:12px; font-family:"microsoft YaHei";margin-top: 40px;}
    td,th{ border:1px solid #ccc; padding:5px;}
    td{ word-break:break-all; text-align:center;}
    tr:nth-child(2n+1){ background:#f1f1f1;}
    tr:first-child{ background:#e0e0e0;}
    tr:hover{ background:#f7f7f7;}
    tr{height: 40px;}
    table textarea{ border:1px solid #ddd; resize:none; width:180px; height:100px; font-size:12px; padding:5px; font-family:"microsoft YaHei";}
</style>
</head>
<body>
<div style="text-align:center;margin-top:20px;">
日期:{{select_date}}
</div>
<table align="center">
<tr>
<th width="650">链接</th>
<th width="90">点击ip数</th>
</tr>
{% for k,v in  reslut_map.items%}
<tr>
<td>{{k}}</td>
<td>{{v}}</td>
</tr>
{%endfor%}
</table>
</body>
</html>
    """
    t=Template(html)
    c=RequestContext(request,{'select_date':select_date,'reslut_map':reslut_map})
    return HttpResponse(t.render(c))
def index(request):
    return render_to_response('index.html')
  
def hello(request):
    return HttpResponse('hello')
def add_hours(request,add):
    add_hours=int(add)
    now=datetime.datetime.now()+datetime.timedelta(hours=add_hours)
    '''assert False'''
    ss="""dfdfd
    """
    return HttpResponse('this is:%s.add %s' %(now,add))
def t_test(request):
    html="""<html>
    <body>
    <p>{{c1}}</p>
    <span>
    {% if c2 %}
    c2 is true
    {% else %}
    c2 is false
    {% endif%}
    </span>
    </body>
    </html>"""
    t=Template(html)
    c=Context({'c1':'xxxx1x','c2':True})
    x=t.render(c)
    xx=type(x)
    return HttpResponse(x)


def tongji(selct_date):
    reslut_map=dict()
    try:
        file_obj=open(log_file_dir+selct_date)
        lines=file_obj.readlines()
        map=dict()
        for line in lines:
            line=line.strip()
            if line!='':
                ss=line.split(' ')
                if len(ss)==2:
                    if ss[0] in map:
                        map[ss[0]].add(ss[1])
                    else:
                        my_set=set()
                        my_set.add(ss[1])
                        map[ss[0]]=my_set
        for k,v in map.items():
            reslut_map[k]=len(v)
    finally:
        file_obj.close()
    return reslut_map