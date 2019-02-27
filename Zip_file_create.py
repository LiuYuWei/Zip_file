
# coding: utf-8

# ## Zip the file

# In[1]:


import os
import sys
import zipfile

def zip_file(startdir): 
    #壓縮過後的路徑:默認為[startdir].zip
    file_news = startdir +'.zip'
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(startdir):
        fpath = dirpath.replace(startdir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
    print ('成功')
    z.close()


# In[ ]:


if __name__ == '__main__':
    startdir = sys.argv[1]
    zip_file(startdir)

