text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

text=text.replace('.','')#文字列の中の記号を除去
text=text.replace(',','')
text_str=text.split()
int_list=list(map(len,text_str))#文字数を数えたリストを作る
L=[str(a) for a in int_list]#文字列に変換
L=" ".join(L)
answer=L.replace(' ','')

print(answer)