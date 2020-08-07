import os
from restore.mysql import MySql

def file_name(file_dir):
    for pwd,dirs,files in os.walk(file_dir):
        return pwd,files

def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
        else:
            return False

pwd,list=file_name('../book_info/《鬼吹灯之龙岭迷窟》')

true_path="D:/Web_Book/"+pwd[3:]+'/'

write=MySql('122.51.168.67','root','IRVing777!','Django_Book')

#write.sql('insert into Book_Chapter(book_name,chapter_name,chapter_path)')
#
# for i in list:
#     for index,j in enumerate(i):
#         if j == '龙' and i[index-1].isdigit():
#             string='insert into Book_chapter(book_name,chapter_name,chapter_path,chapter_id) ' \
#                    'values(\'《鬼吹灯之龙岭迷窟》\',\'{0}\',\'{1}\',{2})'.format(i[index:],true_path+i,i[:index])
#             #print(i[:index])
#             #print(string)
#             write.sql(string)

with open('../book_info/《鬼吹灯之龙岭迷窟》/0天下霸唱',encoding='utf-8') as f:
    brief=f.read(100)

string2='insert into Book_book(book_name,book_brief) values(\'{0}\',\'{1}\')'.\
    format('《鬼吹灯之龙岭迷窟》',brief+'...')
print(brief+'...')
# write.sql(string2)
