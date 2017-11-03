# if False:
#     print ("ssdsdsdsd")
# if None:
#     print("dsdsdsdsd")
#直接遍历  
fruit_list = ['apple','banana','orange']  
print(fruit_list); 
for fruit in fruit_list:  
    print(fruit)  
      
#借助range()函数进行遍历  
fruit_list = ['apple','banana','orange']  
for i in range(len(fruit_list)):  
    print(fruit_list[i])  

fruits=("apple","banana","orange") 
print(fruits);   
print( type(fruits) );   
for i in range(len(fruits)):     
    print(fruits[i])   

fruit_dict = {'apple':1, 'banana':2, 'orange':3}  
print(type(fruit_dict)); 
print(fruit_dict); 
for key in fruit_dict:  
    print(fruit_dict[key])  

fruit_dict = {'apple':1, 'banana':2, 'orange':None}  
print(fruit_dict["orange"])
print(fruit_dict["ttttt"])
#--------------------------------------------------------------------
fruits = ('apple','banana','orange')  
#元组转换为列表：  
list(fruit)  
  
#元组不能直接转换为字典，附：  
#元组转换为字符串：  
fruits.__str__()  


fruit_list = ['apple','banana','orange']   
#列表转换为元组：  
tuple(fruit_list)  
  
#列表不能直接转换为字典，附：  
#列表转换为字符串：  
str(fruit_list) 


fruit_dict = {'apple':1, 'banana':2, 'orange':3}  
#将字典的key转换为元组:  
tuple(fruit_dict)  
#将字典的value转换为元组:  
tuple(fruit_dict.values())  
  
#将字典的key转换为列表:  
list(fruit_dict)  
#将字典的value转换为列表:  
list(fruit_dict.values())  
  
#附：  
#将字典转换为字符串：  
str(fruit_dict)  




#将字符串转换为元组：  
str = "(1,2,3)"  
tuple(eval(str))  
#将字符串转换为列表：  
str = "(1,2,3)"  
list(eval(str))  
#将字符串转换为字典：  
str = "{'a':1 ,'b':2}"  
eval(str)  