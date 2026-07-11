import os 
import time

while True:
    for i in range(40):
        print("=",end="")
        time.sleep(0.080)
    print()
    
    letters="Security EvIdence Collector".upper().center(40)
    
    for letter in letters:
        print(letter,end="")
        time.sleep(0.080)
    print()
    
    for x in range(40):
        print("=",end="")
        time.sleep(0.080)
    print()
    
    print("Initializing",end="")
    
    for i in range(8):
        print(".",end="",flush=True)
        time.sleep(0.2)
        
    print("\nLoading Modules",end="") 
    for i in range(8):
        print(".",end="",flush=True)
        time.sleep(0.2)
        
        
    print("\nChecking Scanner",end="")
    for i in range(8):
        print(".",end="",flush=True)
        time.sleep(0.2)
        
    print("\nPreparing Report Engine",end="")
    for i in range(8):
           print(".",end="",flush=True)
           time.sleep(0.2)
    print('\n---------------------------------')   
    
    #------Main program --------
    
    print("\n> Scans directory for Important files(exe/txt/log/.....):-")
    print("[1] Scans Current directory:")
    print("[2] Scans Custom Directory:")
    print("[3] Exit")


    try:
     choice1=int(input("Enter your choice:"))
    except ValueError:
        print("[$] Only numeric value")
        continue
    
    if choice1 == 1:
        files=os.listdir()
        
        scan=['|','/','-','\\']
        
        for i in range(10):
            print("\rScanning current Directory",scan[i%len(scan)],end="",flush=True)
            time.sleep(1)
        
        count=1
        s_count=0
        report=""
        
        for file in files:
            if file.endswith(".txt") or file.endswith(".log") or file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".exe") or file.endswith(".bat") or file.endswith(".ps1"):
                size=os.path.getsize(file)
                loc=os.path.abspath(file)
                save=f""" [{count}] Name:{file} \n 
                Size : {size} Bytes \n
                Location : {loc}"""
                print("\n",save)
                
                report+=save

                count+=1
                s_count+=1
                
        if s_count == 0:
                print("No file found!")
        print("Total file scanned ",len(files))
        print("Total evidence/important file found:-",s_count)
        try:
         choice2=str(input("Want to save you scan reports (Y/n)?")).lower()
        except ValueError:
           print("only enter Y/N") 
   
        
        if choice2 == "y":
         try:
            file1_name=str(input("Enter the name of file:-"))
         except ValueError:
             print("Enter valid value!")
             if not file1_name.endswith(".txt"):
              file1_name += ".txt"
         file1=open(file1_name,"w")
         file1.write(report)
         file1.close()
         print("="*45)
         print("Report saved successfully!")
         print("File Name:",file1_name)
         print("="*45)
        else:
         print("Ok !, No problem")
    
    elif choice1 == 2:
        files1=input("Enter the path for custom directory:- \n(path example:-D:\example\....)")     
        try:
         os.chdir(files1)
        except FileNotFoundError:
            print("Error : File not found!")
            continue
        
        file_2=os.listdir()
        
        scan=['|','/','-','\\']
        
        for i in range(10):
            print("\rScanning custom Directory",scan[i%len(scan)],end="",flush=True)
            time.sleep(1)
            
        count1=1
        s_count2=0
        report1=""
        
        for filex in file_2:
            if filex.endswith(".txt") or filex.endswith(".log") or filex.endswith(".pdf") or filex.endswith(".docx") or filex.endswith(".exe") or filex.endswith(".bat") or filex.endswith(".ps1"):
              size1=os.path.getsize(filex)
              loc1=os.path.abspath(filex)
              name,ext=os.path.splitext(filex)
              
              save1=f"""[{count1}] Name:{filex} \n
              Size : {size1} Bytes \n
              Extension : {ext}
              Location : {loc1}
              
              """
              print(save1)
              
              count1+=1
              s_count2+=1
              report1+=save1
        
        if s_count2 == 0:
            print("No File found!")
        print("Total file scanned:-",len(file_2))
        print("Total evidence/Important Found!:-",s_count2)
        try:
         choicex=str(input("Want to save the file (y/n)?:-")).lower()
        except ValueError:
            print("Enter y/n only!")
            
        if choicex == "y":
            try:
             file2_name=input("Enter the name of file:-")
            except ValueError:
                print("Enter valid value !")
                if not file2_name.endswith(".txt"):
                 file2_name += ".txt"
            file2=open(file2_name,"w")
            file2.write(report1)
            file2.close()
            print("="*45)
            print("Report saved successfully!")
            print("File Name:",file2_name)
            print("="*45)
        else:
            print("No problem!")
    
    elif choice1 ==  3:
        print("\nExiting",end="")   
        
        for k in range(5):
            print(".",end="")
            time.sleep(0.15) 
        break
    
    else:
        print("Enter valid option!")          
