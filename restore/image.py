from restore import mysql
import os

def file_name(file_dir):
    for pwd,dirs,files in os.walk(file_dir):
        return dirs

dirs=file_name('../book_info')

test=mysql.MySql('122.51.168.67','root','IRVing777!','Django_Book')
dirs_dict={}
for dir in dirs:
    str='select id from Book_book where book_name=\'{0}\''.format(dir)
    dirs_dict[dir[1:-1]]=test.sql(str)[0][0]

#
for i in dirs_dict.keys():
    str='INSERT INTO Book_image(series,url,book_id) VALUES(\'鬼吹灯\',' \
        '\'/static/{0}.jpg\',{1})'.format(i,dirs_dict[i])
    test.sql(str)