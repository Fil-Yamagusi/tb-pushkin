import random
import re
from urllib.parse import quote
from urllib.request import Request, urlopen

find_word = "весна"
url = "https://rifmovka.ru/rifma/{0}#similar".format(quote(find_word))
print(url)
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read().decode('utf-8')
# print(webpage[:50])

re.sub(r'<b>', '', webpage)
re.sub(r'</b>', '', webpage)
pattern = "<meta name=\"description\" content=\"(.*): (.*)\">"
match = re.findall(pattern, webpage)
if match:
    rhymes = match[0][1].split(', ')[0:-1]
    print(len(rhymes))
    for r in rhymes:
        if len(r) > 12:
            rhymes.remove(r)

    random.shuffle(rhymes)
    rhymes = rhymes[0:10]
    answer = f"Зацени рифмы: {find_word} - {', '.join(rhymes)}"

    print(answer)
    print(len(rhymes))
    # print(* rhymes)
else:
    print("Pook")
