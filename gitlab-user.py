import gitlab
from collections import defaultdict
gl = gitlab.Gitlab('http://gitlab.example.com/',private_token='XXXXX',api_version='4')
# projects = gl.projects.list(all=True)
# print(projects)
users = gl.users.list(active=True,all=True)  #拿到所有用户
u = [user.name for user in users] #生成用户列表
projects = gl.projects.list(all=True)   #拿到所有项目
print(u)
for i in u:  #只包含除组以外个人加入的项目
    name_dict = defaultdict(list)
    for project in projects:
        # print(project.id, project.name)
        members = project.members.list()   #项目下的成员列表，非继承，要继承父项目人员设置为project.members.list(all=True)
        a = [me.name for me in members]
        if i in tuple(a):
            name_dict[i].append(project.path_with_namespace) #生成以用户名为key，项目名为value列表的字典
    print(name_dict)
 
for i in u:  #只包含人所在的组
    name_dict = defaultdict(list)
    for group in groups:
        # print(project.id, project.name)
        members = group.members.list()
        a = [me.name for me in members]
        if i in tuple(a):
            name_dict[i].append(group.full_path)  #拿到用户拥有的所有组
    print(name_dict)
    
    
    #去掉黑名单，无项目的人要自己筛选
