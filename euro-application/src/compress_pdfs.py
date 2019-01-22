import glob
import zipfile

pdfs = (pdf for pdf in glob.iglob('./**/*.pdf') if pdf != './letter/main.pdf')

zip_file = zipfile.ZipFile('../Wilde12.zip', 'w')

for pdf in pdfs:
    name_index = pdf.rfind('/')
    name = pdf[name_index + 1:]
    
    if name == 'scan.pdf':
        name = 'recommendation.pdf'
    if name == 'main.pdf':
        dir_index = pdf.find('/')
        name = pdf[dir_index + 1: name_index] + '.pdf'
        
    zip_file.write(
        filename=pdf,
        arcname=name, 
        compress_type=zipfile.ZIP_DEFLATED
    )
    
zip_file.close()
