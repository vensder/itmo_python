import xml

xml = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''

import xml.etree.ElementTree as ET
root = ET.fromstring(xml)
# root = tree.getroot() # получаем корневой эл
print(root)

#quit()

root[0][1].text = str(3012)
root[0][3].text = 'testtest'

for child in root:
	print(child.tag, child.attrib)
	
	for ch2 in child:
		if ch2.text is not None:
			print('TEXT EL', ch2.tag, ':', ch2.text)
		else:
			print('ATTR EL', ch2.tag, ':', ch2.attrib)
			
print(root[0][1].tag + ':', root[0][1].text)

tree = ET.ElementTree(root)
tree.write('xmlfile.xml')

a = ET.Element('a')
b = ET.SubElement(a,'b')

b.text = 'Hello'

tree = ET.ElementTree(a)
tree.write('xmlxml.xml')

ET.dump(a)

