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
    2. 导入刚创建的BookInfo类，并创建一个实例
    3. 根据类中定义的数据类型添加到实例中
    4. 使用.save()来将实例中的数据保存到数据库，对已经有的实例保存方式为覆盖
    5. 使用.delete删除数据库中的数据
    6. 使用类名.objects.get(id(主键名))返回一个保存对应主键数据的对象实例