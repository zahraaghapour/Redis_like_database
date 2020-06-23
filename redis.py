import hashlib
import shelve
from my_regex import check_type
print('''                     
                      ****  Welcome to redis-like data base  ****     
                        ''')
from abc import ABC, abstractmethod
f=open('password.txt', 'a')
class Main(ABC):

    @abstractmethod
    def Login(self):
        pass

    @abstractmethod
    def SignUp(self):
        pass

    @abstractmethod
    def hash_pass(self,passw):
        pass

    @abstractmethod
    def user_operetion(self):
        pass

    @abstractmethod
    def SET_KEY(self,k,v):
        pass

    @abstractmethod
    def GET_VALUE(self,k):
        pass

    @abstractmethod
    def GET_KEYS(self, k):
        pass

    @abstractmethod
    def REMOVE_Key(self,k):
        pass

    @abstractmethod
    def Help(self):
        pass


class ConcreteMain(Main):
    instance = None
    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


    def hash_pass(self, passw):
        x = lambda a: hashlib.new('sha256', a.encode()).hexdigest()
        return x(passw)

    def Login(self):
        f = open("password.txt", "r").read()
        self.Username = input('Enter Username : ')
        Password = input('Enter Password : ')
        Password = self.hash_pass(Password)
        while self.Username not in f or ('%s:%s' % (self.Username, Password)) not in f:
            print('Wrong Username or Password. Try again ')
            self.Username = input('Enter Username : ')
            Password = input('Enter Password : ')
            Password = self.hash_pass(Password)
        self.user_operetion()

    def SignUp(self):
        f=open("password.txt", 'r').read()
        self.Username = input('Enter Username : ')
        while self.Username in f:
            print('Select Another One : Username Exists !!!')
            self.Username = input('Enter Username : ')
        Password = input('Enter Password : ')
        while len(Password) < 8:
            Password = input('Enter Password(at least 8 char) : ')
        Password1 = input('Enter Password again: ')
        while Password != Password1:
            print('Password Confirmation is wrong !!!')
            Password1 = input('Enter Password again: ')
        Password = self.hash_pass(Password)
        f1 = shelve.open(f"{self.Username}")
        f = open("password.txt", "a")
        f.write('%s:%s\n' % (self.Username, Password))
        f.close()
        f1.close()
        self.user_operetion()

    def user_operetion(self):
        print('\n  ***  Welcome '  +self.Username,'  ***')

        menu = None
        while menu != 'EXIT':
          self.sf = shelve.open(f"{self.Username}")
          print ('''
Menue : Select and print\n
        HELP
        SET Key value
        GET key
        GET_SET keys
        REMOVE Key
        SAVE
        EXIT
            ''')
          try:
            menu=(input('Select from menue : '))
            List = (menu.split())
            comment = List[0]

            if comment == 'HELP':
                self.Help()
            elif comment == 'SET':
                k=List[1]
                v=List[2]
                v=check_type(v)
                self.SET_KEY(k,v)
            elif comment == 'GET':
                k=List[1]
                self.GET_VALUE(k)
            elif comment == 'GET_SET':
                k=List[1]
                k=k.split(',')
                self.GET_KEYS(k)
            elif comment == 'REMOVE':
                k = List[1]
                self.REMOVE_Key(k)
            elif comment == 'SAVE':
                self.sf.close()
            elif comment == 'EXIT':
                self.sf.close()
                break
            else: print ('Wrong Selection. Print again')
          except:
            print('Wrong Input. Try again')
            continue

    def Help(self):
            print ('''
        SET Key value  --> Adding a key value element to file e.g:  SET name zahra
        GET key  --> Get value of a specific key e.g:  GET name
        GET_SET keys  ---> Get sets of values for sets of keys : GET_SET name,age
        REMOVE Key  --> Remove key value element from file e.g:  REMOVE name
        SAVE  --> Save file
        EXIT  --> Exit and log out
            ''')

    def SET_KEY(self,key,value):
        elm1 = Element(key, value)
        self.sf[key]=elm1

    def GET_VALUE(self,key):
        first = None
        values=self.sf.values()
        for elm in values:
          if first == None:
              first=elm
          else:
              elm.next=first
              first=elm
          temp=first
          if key == temp.key :
                print(temp.value)
                return
        print('key not in file')


    def GET_KEYS(self, k):
        first = None
        value_lists=[]
        for i in k:
            value = self.sf[i]
            if first == None:
                first = value
            else:
                value.next = first
                first = value
        temp = first
        while temp != None:
            value_lists.append(temp.value)
            temp = temp.next
        print(list(reversed(value_lists)))

    def REMOVE_Key(self,key):
            del self.sf[key]



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# if __name__ == '__main__':

while(1):

    print ('''
1.Login
2.Sign Up
        ''')
    try:
        select=int(input('Select one option 1 or 2 : '))
    except:
        print("Your entered option is not true. Select a number between 1 and 2: \n")
        continue
    main_obj = ConcreteMain()
    if select not in range(1, 3):
        print('Wrong selection.  try again.\n')
        continue
    if select==1:
       main_obj.Login()
    else :
       main_obj.SignUp()
