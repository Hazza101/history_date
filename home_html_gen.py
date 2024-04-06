import os

filenames = os.listdir("periods")

for filename in filenames:
    
    if filename.split('.')[1] != 'html':
        continue
    #print(filename)
    print(f'''
<div class="result">
    <h3><a href="periods/{filename}">{filename.split('.')[0]}</a></h3>
</div>
''')
