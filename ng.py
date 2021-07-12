#code = str(input("code(4) : "))
#name = str(input("name: "))
#name = "@nashenas"
code = "0921"
f = open("range921.vcf","a+")
n = 0 
cra = "0123456789"
string = '''
BEGIN:VCARD 
VERSION:2.1 
N:;@921;;;
TEL;CELL:{}
END:VCARD 
'''
for q1 in cra:
  for q2 in cra:
    for q3 in cra:
      for q4 in cra:
        for q5 in cra:
          for q6 in cra:
            for q7 in cra:
              phone = code+q1+q2+q3+q4+q5+q6+q7
              n = n+1
              #fullname = name+str(n)
              con = string.format(phone)#fullname,phon
              f.write(con)
f.close()
print (" nubmers : "+str(n))
