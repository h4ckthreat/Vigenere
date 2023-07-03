 #IFBWZ TDBMF BCTPSC FMEFS
import string
def poly(plain:str,key:int) -> str:
    plain,charset=plain.lower(),{}

    letters=string.ascii_lowercase 

    for i in range(len(letters)):
        charset.update({letters[i-key]:letters[i]})
       

    def encdec(plain:str,chareset:dict) -> str:

        es=''

        for char in plain:
            try:
                es+=charset[char]
            except:
                es+=char 

        return es 

    return encdec(plain,charset).upper() 

for i in range(26):
   
    possible_answer=poly("CKZPYAC QSZHCAR EYKC QSNNJW",i)
    print(f'{possible_answer}, Key:{i+1}')
