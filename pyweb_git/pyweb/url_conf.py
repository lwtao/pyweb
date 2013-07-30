

"""baidu.com 2
sina.com 3
sohu.com 5
"""
urls=[]
g_index=0
file_name='/root/url_conf.txt'
#file_name='g://url_conf.txt'
def get_url():
    global g_index
    global urls
    if(len(urls)==0):
        g_index=0
        file_object = open(file_name,'r')
        try:
            lines = file_object.readlines()
        finally:
            file_object.close( )
        for url_str in lines:
            url_str=url_str.strip()
            t_list=url_str.split(' ')
            num=int(t_list[1])
            url=t_list[0]
            for i  in range(num):
                urls.append(url)
    if(g_index<len(urls)):
        t_url=urls[g_index]
        g_index=g_index+1
        return t_url
    else:
        g_index=1
        return urls[0]
def get_all_url():
    file_object = open(file_name,'r')
    url_p=[]
    try:
        lines = file_object.readlines()
        for str in lines:
            str=str.strip()
            t=str.split(' ')
            url_p.append((t[0],t[1]))
    finally:
        file_object.close( )
    return url_p

def save_url(str):
    file_object = open(file_name,'w')
    try:
        file_object.write(str);
    finally:
        file_object.close( )
    global urls
    urls=[]
    return 
