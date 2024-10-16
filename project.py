print("python basics")
str1="this is me"
age=21
weight=75.55
#number strings liost tuplle dictionaries
print("3+5 =",3+4)

mls='''this 
is a 
multi line string '''
print(mls)

# print("this is print 1",end="")
print("this is print 2 "*5)

#list
colleges=['ucp','pgc','fc']
print(colleges[-1])
colleges[2]="numl uni"
print(colleges[-1])
print(colleges[0:2])
#append
colleges.append("punjab university")
print(colleges)
colleges.insert(0, "fast")
colleges.remove("punjab university")
print(colleges)

#tuple
tup1=(1,2,3)
print(tup1[0])
#tuple value cant change

#dictionary
name={
    "name":"john",
    "age":21,
    "city":"new york"
}
print(name)

#if eslse
# number2=int (input())
# print(number2)
# if(number2>90):
#     print("number is greater than 90")
# elif(number2>80):
#     print("number is greater than 80 but less than 90")    
# else:
#     print("number is less than 80")

#loops in pyhton
for i in range(0,10):
    print(i)
for item in colleges:
    print(item)

#functions in pyhton
def add(a,b):
 return a+b  
result=add(5,7)
print(result)

#strings
str1="this is me"
print(str1[0:2])
print (str1[:-2])
print(str1.capitalize())

#object oriented programming languages
class Employee:
   __name=None
   __id=0
   __salary=0

   def set_name(self,name):
      self.__name=name
   def get_name(self):
      return self.__name
   def set_id(self, id):
      self.__id=id 
   def get_id(self):
     return self.__id
harry=Employee()
harry.set_name('harry')
print(harry.get_name())
setids=id()
setids.set_id(10)
print(setids.get_id())
