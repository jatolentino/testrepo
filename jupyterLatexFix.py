import re
import os

folder = '.'

files = [f for f in os.listdir(folder) if f.endswith(".md")]

urlStringStart = "<img src=\"https://latex.codecogs.com/svg.image?{\\large\\color{Blue}\\pmb{"
urlStringEnd = "}\" align=\"center\">"


#pattern1dollar = "[^0-9a-zA-Z?]\$(.*)\$[^\$0-9a-zA-Z?]"
pattern1dollar = "[^\$0-9a-zA-Z?]\$(.*?)\$[^\$0-9?]"
#patternDollarDollar = "(?<=\$\$)[\S\s]*(?=\$\$)"
#patternDollarDollar = "(?<=\$\$)[\S\s]*(?=\n\$\$)"
patternDollarDollar = "(?s)(?<=\$\$)(.*?)(?=\$\$)"


#Fix equations and add bold & style
for file in files:
    with open(os.path.join(folder, file), mode="r") as f:
        lines = f.read()
        
        # Delete bolds from jupyter
        lines = lines.replace("**", "")
        #lines = lines.replace("\$\$(.*)\$\$", "\n\$\$(.*)\n")
        #lines = re.sub('\$\$(.*)\$\$', '\n\$\$(.*)\$\$\n', lines)
        # Fix equation title list(filter(None, ))
        
        arrayDollars = list(filter(None,re.findall(pattern1dollar, lines)))
        arrayDollarsDollars = list(filter(None,re.findall(patternDollarDollar, lines)))
        
        #print(arrayDollars)
        
        #Counting number of ocurrences of $$
        numberOfOcurrences = len(arrayDollars)
        #print(numberOfOcurrences)
        #print(re.findall(pattern1dollar, lines))
        
        numberOfOcurrencesDD = len(arrayDollarsDollars)
        substringsDD = arrayDollarsDollars
        print(substringsDD)
        print(len(substringsDD))
        for i in range(numberOfOcurrencesDD):
            # totalsubstringDD = "$$" + substringsDD[i] +"$$" # todo string $..$
            # #print(totalsubstringDD)
            # newsubstringDD =  "\n$$" +  substringsDD[i] + "$$\n"
            # with open(os.path.join(folder, file), mode="w") as f:
                # lines = lines.replace(totalsubstringDD, newsubstringDD)
                # f.write(lines)
            if(i <= (numberOfOcurrencesDD +1)*0.5):
                totalsubstringDD = "$$" + substringsDD[i] +"$$" # todo string $..$
                #print(totalsubstringDD)
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
