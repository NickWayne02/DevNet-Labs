import xml.etree.ElementTree as ET
import re

# Розбір XML файлу
xml = ET.parse("myfile.xml")
root = xml.getroot()

# Пошук тегів <edit-config>, <default-operation>, <test-option>
ns = re.match('{.*}', root.tag).group(0)
editconf = root.find("{}edit-config".format(ns))
defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))

# Друк значень <default-operation> та <test-option>
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))
