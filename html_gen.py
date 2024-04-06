import re

symbol_dic = {}


list_of_pages = []

with open('history_dates.txt', 'r', encoding='utf-8') as f:

    page = None
    index = -1
    for line in f.readlines():
        char = line[0]
        if char == '\n':
            continue
        '''
        if char not in symbol_dic:
            symbol_dic[char] = 1

        else:
            symbol_dic[char] += 1
        
        #if char == '+':
         #   print(line.strip())

        '''

        if char == '+':
            if page != None:
                list_of_pages.append(page)
                
            page = {}
            
            page['exam-board'] = line[1:].strip()
            page['dates'] = []
            index = -1

        elif char == '@':
            page['paper'] = line[1:].strip()

        elif char == '~':
            page['section'] = line[1:].strip()

        elif char == '^':
            page['title'] = line[1:].strip()

        elif char == '*':
            page['dates'].append([line[1:].strip(), None])
            index += 1
            

        elif char == '<':
            page['dates'][index][1] = line[1:].strip()

        
pattern = r'[\\/:*?"<>|]'       
template_1 = ""
template_2 = ""
with open('template_1.txt') as f:
    template_1 = "".join(f.readlines())

with open('template_2.txt') as f:
    template_2 = "".join(f.readlines())
            
for page in list_of_pages:
    formatted_page = template_1
    formatted_page += f'''
    <h2>{page['title']}</h2>
    <h3>Exam Board: <em>{page['exam-board']}</em></h3>
    <h3>Paper: <em>{page['paper']}</em></h3>
    <h3>Section: <em>{page['section']}</em></h3>
</div>

<div class="accordion">
'''

    for accordion_title, explanation in page['dates']:
        
        title, date = accordion_title.split(",*,")[0], accordion_title.split(",*,")[1]
        date = f"<b>{date[1:]} </b>"
        clean_accordion_title = date + title
        formatted_page += f'''
        
    <div class="accordion-item">
        <button class="accordion-button">{clean_accordion_title}</button>
            <div class="accordion-content">
                <p>{explanation}</p>
            </div>
    </div>

'''
        #print("-"*60)
        #print(date)
        #print(explanation)

    formatted_page = formatted_page + '</div>\n</div>\n' + template_2

    #print(formatted_page)
    clean_title = re.sub(pattern, ' ' ,page['title'])
    with open(f'periods\\{clean_title}.html', 'w', encoding='utf-8') as f:
        f.write(formatted_page)
    
    #input()

