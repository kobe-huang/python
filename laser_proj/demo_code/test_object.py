# -*- coding: utf-8 -*-
# import sys
# reload(sys)  
# sys.setdefaultencoding('utf8')  

class class_name(object):
    class_var = 'I am a class variable' #类变量
    def __init__(self):
        self.instance_var = 'I am a instance varibale'  #成员变量（实例变量）

    def instance_method(self,  formal_parameter):
        local_var_in_function = formal_parameter    #实例方法局部变量
        print "orig " + self.instance_var;
        self.local_var_also_in_function = formal_parameter  #实例方法局部变量
        self.instance_var = 'I am a instance 2_varibale'
        print "after " + self.instance_var + "\n";

    def ordinary_function(self,formal_parameter):
        print "orig " + self.instance_var;
        self.instance_var = formal_parameter
        print "after " + self.instance_var + "\n";   
        
        print "orig " + self.class_var  #当为空的时候，取class中的变量
        self.class_var = "instance can set class_var!!" #只修改instance中的  kobe
        print self.local_var_also_in_function;
        print "after " + self.class_var + "\n--------------------------------------------------\n";


    @classmethod  #注意这个classmethod
    def class_method( cls,formal_parameter): #类方法
        
        #print "orig" + cls.instance_var + '\n';  #报错，不能访问instance
        cls.instance_var = formal_parameter
        print "after " + cls.instance_var;
        print "orig "  + cls.class_var 
        cls.class_var   = formal_parameter
        print "after " + cls.class_var   + '\n';

    @staticmethod  #这
    def static_method(formal_parameter): #注意不能添加self 参数 kobe
        # print 'I am static method, I am the Adopted son(干儿子) for this class!!'
        # print class_var;
        if locals().has_key('huang') == False :
            huang = "ttt ";
        huang = huang + formal_parameter;
        print huang
        print "I can't modify anything in the class\n"
        #print self.class_var
        #print self.instance_var

print '______Get a class instance_____'
class_instance = class_name()
class_instance.class_method('class method is calling!!')
class_instance.static_method('static method in calling!!')
class_instance.instance_method('instance method is calling!!')
class_instance.ordinary_function("I am a instance 1_varibale");


print '\n_________直接处理___________'
print 'class var is calling!!'
print  class_instance.class_var
print 'instance var is calling!!'
print  class_instance.instance_var


print '\n_________Get a class!!___________'
class_name.class_method('class method is calling1!!')
class_name.static_method('static method in calling1!!')
print class_name.class_var
print class_name.instance_var  #注意这个是class的instance


print '\n______Get a class instance1_____'
class_instance1 = class_name();
class_instance1.class_method('class method is calling2!!')
class_instance1.static_method('static method in calling2!!')
class_instance1.instance_method('instance method is calling2!!')
class_instance1.ordinary_function('I am a instance 2_varibale');

print 'END!!'