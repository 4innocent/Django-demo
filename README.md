# 这是Django的学习笔记

---

## 1. 创建Django一个项目

    1. 首先使用django-admin startproject 项目名称
    2. 使用python manage.py startapp 应用名创建一个应用
    3. 将应用添加在settings.py的INSTALLED_APPS中
    4. 运行python manage.py runserver运行项目

## 2. 生成迁移文件
    
 > 生成数据库文件
 
    1. 使用python manage.py makemigrations生成迁移文件(用来构成数据库)
    2. 执行python manage.py migrate生成迁移生成表
        
 > 实现数据库的增删改查
 
    1. 使用python manage.py shell打开命令行模式
    2. 从booktest.models导入刚创建的BookInfo类，并创建一个实例
    3. 根据类中定义的数据类型添加到实例中，.属性名=
    4. 使用.save()来将实例中的数据保存到数据库，对已经有的实例保存方式为覆盖
    5. 使用.delete删除数据库中的数据
    6. 使用类名.objects.get(id(主键名))返回一个保存对应主键数据的对象实例
    7. 将其他表的实例赋值给外键属性建立一对多关系。如：h.hbook = b
    8. 查询表对应的多个数据用b.heroinfo_set.all() # 查询出b对应的所有英雄人物的信息
    
 > 后台管理
 
    1. 在settings中设置语言和时区
    2. python manage.py createsuperuser 创建超级管理员
    3. python manage.py runserver 启动服务器登陆管理员/admin
    
## 3. View视图

 > 添加路由

    1. 在app中新建urls文件
    2. 在项目目录中的urls文件中添加app的urls
    3. 在view中添加方法，方法名即为url地址
    
## 4. 模板

    1.在项目目录下新建templates文件夹，文件夹中包括各个app文件夹，内含对应app的html
    2. 在setting中配置模板路径
    3. 在views文件中使用render函数渲染模板并返回