import codecs
import sys

fname = sys.argv[1]

f = codecs.open(fname, 'r', 'utf-8')

first = f.readline().strip().encode('utf-8')
f.readline()

rest = f.read().strip().encode('utf-8')




print '<pagina-tematica xmlns="http://servicos.gov.br/v3/schema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
print '<nome>' + first + '</nome>'
print '<conteudo><![CDATA[' + rest + ']]></conteudo>'
print '</pagina-tematica>'
