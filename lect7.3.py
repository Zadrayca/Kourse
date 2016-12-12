# xml
from xml.etree import ElementTree

# s = '''
# <people>
#     <man>
#         <name>Ольга Сидорова</name>
#         <age>30</age>
#     </man>
#     <man>
#         <name>Иван Петров</name>
#         <age>45<age/>
#     <man/>
# </people>
# '''



root = ElementTree.parse('1xml.xml')
print(root)

root = root.getroot()
for a in root:
    print(a, a.tag, a.text)

    for b in a:
        print(b.tag, b.text)

for i in root.findall('man'):
    print(a)
