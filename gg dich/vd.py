from googletrans import Translator
inputs=input()
t=Translator()
a=t.translate(inputs,src='vi',dest="en")
b=a.text