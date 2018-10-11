import re

text = """Welcome to #CEICData. If you need any help 
	      from HRs you can write to #Kapka.Mircheva. For 
	      any technical problems you should contact
	      #Nevolia.Prikaznova. If you need any smart
	      advices, please contact #Miroslav.Georgiev or
	      #Ivan.Arnaudov. #When you are sick, please
	      stay at #.Home."""


pattern = r'(#\w+\.\w+)'

result = re.findall(pattern, text)

for item in result:
	print(item)