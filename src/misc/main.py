import random
import time

def encrypt(message,key=None,charsize=3):
    mlength=len(message)
    chars=" `1234567890—-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?"+'"'
    chars=list(chars)
    indexs=[]
    if key==None:
        key=random.randint(10**(charsize-1)+1,10**(charsize)-1)
    for x in range(len(chars)):
        if len(indexs)<2:
            newindex=(key%(10**(charsize)))
        else:
            newindex=( (indexs[-1]+indexs[-2])%(10**(charsize)) )
        while newindex in indexs:
            newindex=(newindex+1)%(10**(charsize))
        indexs.append(newindex)
    
    
    convmess=""
    for char in message:
        convchar=str(indexs[chars.index(char)])
        convchar=("0"*(charsize-len(convchar)))+convchar
        convmess+=convchar
    convmess=convmess[1:]+convmess[0]

    oldconvmess=convmess
    convmess=[]
    for place in range(mlength):
        char=int(oldconvmess[place*charsize:place*charsize+charsize])
        char*=key
        
        convmess.append(char)
    
    
    stringmess=""
    for char in convmess:
        char=str(char)
        char=("0"*((2*charsize)-len(char)))+char
        stringmess+=char
        

    return key,stringmess

def decrypt(message,key):
    charsize=len(str(key))
    mlength=int(len(message)/(charsize*2))
    chars=" `1234567890—-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?"+'"'
    chars=list(chars)
    indexs=[]
    for x in range(len(chars)):
        if len(indexs)<2:
            newindex=(key%(10**(charsize)))
        else:
            newindex=( (indexs[-1]+indexs[-2])%(10**(charsize)) )
        while newindex in indexs:
            newindex=(newindex+1)%(10**(charsize))
        indexs.append(newindex)
    
    convmess=""
    
    for place in range(mlength):
        char=int(int(message[place*charsize*2:place*charsize*2+(charsize*2)])//key)
        char=str(char)
        char=("0"*(charsize-len(char)))+char
        convmess+=char
    
    convmess=convmess[-1]+convmess[:-1]
    finmess=""
    
    for place in range(mlength):
        char=int(convmess[place*charsize:place*charsize+(charsize)])
        finmess+=chars[indexs.index(char)]
    
    return finmess
    
    
if __name__ == "__main__":
    adv=0
    for _ in range(10):
        start=time.time()
        m=encrypt("Consider, if you will, the many instances throughout history—far too numerous to name and yet far too important to dismiss—when the simple act of preparing to prepare has proved as consequential as preparation itself. When great nations girded themselves not for action but for the dignified contemplation of whether action might one day be desirable, they revealed a strength not of arms or armies, but of admirable administrative patience. We, too, stand now at the hallowed threshold of that initial moment when a people, united in purpose though yet uncertain in aim, recognize that the very prospect of beginning is itself a beginning of considerable magnitude. What, after all, is a first step but the subtle whisper of a step that one day may be taken? And what is that whisper if not the proud declaration that we remain capable of hesitation on a grand and unified scale? Indeed, let us take comfort in the notion that hesitation, when executed with sufficient ceremony, rises to the level of a civic virtue. For there is no greater testament to the seriousness of a nation than its willingness to stand together in unified uncertainty, shielding itself from precipitous action with the steady armor of prolonged forethought. Even the greatest architects, before drawing their first lines, spend hours surveying the blankness of the page, marveling at the untouched potential it presents. And so we, too, must survey our own blankness—our blankness of intent, of plan, of decisive inclination—knowing that in that emptiness lies the infinite possibility of all that might eventually occur. Thus, let us cherish this moment, not as an absence of movement but as a triumph of dignified inertia, a celebration of the art of almost.",
        None,10)
        print(m[0],len(m[1]))
        print(decrypt(m[1],m[0]))
        end=time.time()-start
        adv+=end
        print(end)
    print(adv/10)