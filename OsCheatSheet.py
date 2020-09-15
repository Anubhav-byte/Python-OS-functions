import os

#joining directory paths
dpath = os.path.join( '.git' , 'info')

print(dpath)

#Getting the current working directory

pwd= os.getcwd()
print( pwd )

#Changing working directory
os.chdir('C:\\Users')
print( os.getcwd() )

#Creating new directory
os.makedirs( 'D:\\testfolder' )
os.chdir( 'D:\\testfolder' )
print( os.getcwd() )

#getting the absolute paths
absolute_path = os.path.abspath('.')
print(absolute_path)

#to check whether a path is absolute or not
is_absolute = os.path.isabs('.')

#getting the relative path
relative_path = os.path.relpath( 'C:\\Users' , 'C:\\' )
print( relative_path )

#getting the base name
path = "D:\\testfolder\\test.txt"
base_name = os.path.basename( path )
print(base_name)

#getting the directory name
dir_name = os.path.dirname(path)
print(dir_name)

#splitting the filepath into file and directory paths
spath = os.path.split(path)     #it returns a tuple consisting of directory path and file dir_name
print(spath)


#getting the size of a file
fsize = os.path.getsize( path )
print( fsize )

#Listing the directory
ls = os.listdir( path )
print( ls )


#Checking path validity

#check whether a path exist
pe = os.path.exists(path)
print( pe )

#check whether a directory exists
dir_exists= os.path.isdir('C:\\User')
print(dir_exists)

#check whether a file exists
file_exists= os.path.isfile( path )
print( file_exists )
