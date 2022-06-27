import re
import os

folder = '.'
files = [f for f in os.listdir(folder) if f.endswith(".md")]

urlStringStart = "<img src=\"https://latex.codecogs.com/svg.image?{\\large\\color{Blue}\\pmb{"
urlStringEnd = "}\" align=\"center\">"

pattern1dollar = "[^\$0-9a-zA-Z?]\$(.*?)\$[^\$0-9?]"
patternDollarDollar = "(?s)(?<=\$\$)(.*?)(?=\$\$)"
patternTitle = '^#.*'
patternPics = '^\!\[png\].*'


#Fix equations and add bold & style
for file in files:
    with open(os.path.join(folder, file), mode="r") as f:
        lines = f.read()
        
        #lines = lines.replace("**", "")

        arrayDollars = list(filter(None,re.findall(pattern1dollar, lines)))
        arrayDollarsDollars = list(filter(None,re.findall(patternDollarDollar, lines)))
        arrayTitle = list(filter(None,re.findall(patternTitle, lines, re.M))) #return all line
        newarrayTitle = [s.replace("**", "") for s in arrayTitle]

        
        #Counting number of ocurrences of $$
        numberOfOcurrences = len(arrayDollars)
        numberOfOcurrencesDD = len(arrayDollarsDollars)
        numberOfOcurrencesTitle = len(arrayTitle)
        #print(numberOfOcurrencesTitle)
        #print(arrayTitle)
        
        substringsDD = arrayDollarsDollars
        
        # Fix picture source
        arrayPics = list(filter(None,re.findall(patternPics, lines, re.M)))
        numberOfOcurrencesPics = len(arrayPics)
        
        
        # Delete ** from title
        for i in range(numberOfOcurrencesTitle):
            with open(os.path.join(folder, file), mode="w") as f:
                    lines = lines.replace(arrayTitle[i], newarrayTitle[i])
                    f.write(lines)
        
        for i in range(numberOfOcurrencesDD):
            if(i <= (numberOfOcurrencesDD +1)*0.5):
                totalsubstringDD = "$$" + substringsDD[i] +"$$" # todo string $..$
                newsubstringDD =  "\n$$" +  substringsDD[i] + "$$\n"
                with open(os.path.join(folder, file), mode="w") as f:
                    lines = lines.replace(totalsubstringDD, newsubstringDD)
                    f.write(lines)
                i=i+2;
        
        substrings= arrayDollars

        for i in range(numberOfOcurrences):
            totalsubstring = "$" + substrings[i] +"$" # todo string $..$
            substringNospaces = substrings[i].replace(" ", "") # removing spaces
            newsubstring = urlStringStart +  substringNospaces + urlStringEnd
            with open(os.path.join(folder, file), mode="w") as f:
                lines = lines.replace(totalsubstring, newsubstring)
                f.write(lines)


for file in files:
    with open(os.path.join(folder, file), mode="r") as f:
        lines = f.read()
        textWithoutStyle = re.sub('<style scoped>(\n.*?)*?\n</style>\n', '', lines, flags=re.MULTILINE)
        with open(os.path.join(folder, file), mode="w") as f:
            f.write(textWithoutStyle)

# print(arrayTitle)
# new_list = [s.replace("**", "") for s in arrayTitle]
# print(new_list)

#print(numberOfOcurrencesPics)
#print(arrayPics)
