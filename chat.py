import os

while True:
   print("chat with me  your requirements:", end='')
   print=input()
 

   if ("run" in p) and ("chrome" in p):
       os.system("start chrome")
   elif(("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
       os.system("notepad")
   elif("run" in p) or ("execute" in p) and ("paint" in p):
       os.system("mspaint")
   elif("run" in p) or ("execute" in p) and ("clock" in p):
       os.system("start clock")
   elif("run" in p) or ("execute" in p) and ("calendar" in p):
       os.system("start calendar")
   elif ("exit in p") or ("quit" in p):
       break
   else:
       print("dont support")
