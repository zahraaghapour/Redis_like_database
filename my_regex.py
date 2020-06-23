
import re

def check_type(n) :
    # int

    if re.search('^[0-9]+$',n):
        x1=int(n)
        return x1

    #float

    elif re.search('\d\.\d', n):
        x2 = float(n)
        return x2

    #[]

    elif re.search('^\[.*',n):
      l1=[]
      n=n[1:-1]
      ind=[]
      if re.search('\{.*\}',n) or re.search('\(.*\)',n) or re.search('\[.*\]',n):
          if re.search('\{[^}]*\}', n):
              x = re.findall('\{[^}]*\}', n)
              n = re.sub('\{[^}]*\}', ' ', n)
              for i in x:
                  l1.append(check_type(i))
          if re.search('\[[^]]*\]', n):
              x = re.findall('\[[^]]*\]', n)
              n = re.sub('\[[^]]*\]', ' ', n)
              for i in x:
                  l1.append(check_type(i))
          if re.search('\([^)]*\)', n):
              x = re.findall('\([^)]*\)', n)
              n = re.sub('\([^)]*\)', ' ', n)
              for i in x:
                  l1.append(check_type(i))

          s = re.split(',', n)
          for index, item in enumerate(s):
              if item == ' ':
                  ind.append(index)
              else:
                  s[index]=check_type(s[index])


          id = 0
          for i in ind:
              s[i] = (l1[id])
              id = id + 1
      else:
        s = re.split(',', n)
        for i in range(len(s)):
          s[i]=check_type(s[i])
          s=s+l1
      return s

    #()

    elif re.search('^\(.*\)$',n):
        l1 = []
        n = n[1:-1]
        ind=[]
        if re.search('\{[^}]*\}', n) or re.search('\([^)]*\)', n) or re.search('\[[^]]*\]', n):
            if re.search('\{[^}]*\}', n):
                x = re.findall('\{[^}]*\}', n)
                n = re.sub('\{[^}]*\}', ' ', n)
                for i in x:
                    l1.append(check_type(i))
            if re.search('\[[^]]*\]', n):
                x = re.findall('\[[^]]*\]', n)
                n = re.sub('\[[^]]*\]', ' ', n)
                for i in x:
                    l1.append(check_type(i))
            if re.search('\([^)]*\)', n):
                x = re.findall('\([^)]*\)', n)
                n = re.sub('\([^)]*\)', ' ', n)
                for i in x:
                    l1.append(check_type(i))

            s = re.split(',', n)
            for index, item in enumerate(s):
              if item==' ':
                  ind.append(index)
            id = 0
            for i in ind:
              s[i]=l1[id]
              id=id+1

        else:
            s = re.split(',', n)
            for i in range(len(s)):
                s[i] = check_type(s[i])
            s = s + l1
        return tuple(s)

    #{}

    elif re.search('^{.*}$',n):
       l1 =[]
       l2=[]
       l3=[]
       ind=[]
       n = n[1:-1]
       if re.search('\{[^}]*\}', n) or re.search('\([^)]*\)', n) or re.search('\[[^]]*\]', n):
            if re.search('\{[^}]*\}', n):
                x = re.findall('\{[^}]*\}', n)
                n = re.sub('\{[^}]*\}', ' ', n)
                for i in x:
                    l1.append(check_type(i))
            if re.search('\[[^]]*\]', n):
                x = re.findall('\[[^]]*\]', n)
                n = re.sub('\[[^]]*\]', ' ', n)
                for i in x:
                    l1.append(check_type(i))
            if re.search('\([^)]*\)', n):
                x = re.findall('\([^)]*\)', n)
                n = re.sub('\([^)]*\)', ' ', n)
                for i in x:
                    l1.append(check_type(i))


            s = re.split(',', n)
            for i in s:
                x = (re.split(':', i))
                l2.append(check_type(x[0]))
                l3.append(check_type(x[1]))
            for index, item in enumerate(l3):
              if item==' ':
                  ind.append(index)
            id = 0
            for i in ind:
              l3[i]=l1[id]
              id=id+1
       else:
            s = (re.split(',', n))
            for i in s:
                 x=(re.split(':',i))
                 x[1]=check_type(x[1])
                 l2.append(x[0])
                 l3.append(x[1])
       d=dict(zip(l2,l3))
       return(d)

    else:
        return n



if __name__ == '__main__':
    n=input('Enter ')
    out=check_type(n)
    print(out)
    print(type(out))


