
# Python program to explain os.path.getsize() method  
    
# importing os module  
import os 
FileSize= {}  
# Path 
File1 = '/home/Shukrithi/College/DeviceDrivers/TestEmail1.txt'
  
# Get the size (in bytes) 
# of specified path  
FileSize[File1] = os.path.getsize(File1)  
print(FileSize)
  
# Print the size (in bytes) 
# of specified path  
#print("Size (In bytes) of '%s':" %path, size) 
