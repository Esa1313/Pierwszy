import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')

root = tree.getroot()

film = "THE KARATE KID"
print(film)
nowy_rok = root.find("./genre/decade/movie[@title='%s']/year" % film)
print("Rok przed zmianą: ", nowy_rok.text)

nowy_rok.text = '2023'
print("Rok po zmianie: ", nowy_rok.text)

tree.write('nowy_rok2023.xml')

print("Kopia pliku z wprowadzoną zmianą: 'nowy_rok2023.xml'")