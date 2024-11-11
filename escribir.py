import xml.etree.ElementTree as ET

root = ET.Element("Libros")
libro1 = ET.SubElement(root, "Libro", titulo="Python Básico")
autor1 = ET.SubElement(libro1, "Autor")
autor1.text = "Juan Pérez"

tree = ET.ElementTree(root)
tree.write("nuevos_libros.xml")
