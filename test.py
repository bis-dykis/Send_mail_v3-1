import os
attach_url = "abc"
name = "1"
file_name = ''.join([name, ".pdf"])
pdfurl = os.path.join(attach_url, file_name)
print(pdfurl)