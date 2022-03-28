import wolframalpha
import numpy as np
import sympy as sp
from sympy.interactive import printing

printing.init_printing(use_latex=True)

app_id = "7UWKUJ-TRG2GVVEAX"
client = wolframalpha.Client(app_id)

while True:
    ques = str(input("Enter Your Query::\t"))
    res = client.query(ques)
    answer = next(res.results).text
    ans = sp.Function(answer)
    x, y = sp.symbols("x y")
    f = sp.Function(x, y)
    f
    print("Your request has been satisfied::\t", end=" ")
    # display(ans)
