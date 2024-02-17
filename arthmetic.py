def series(first_term,common_difference,num_terms):
    ap_series=[]
    for i in range(num_terms):
        term=first_term+(i*common_difference)
        ap_series.append(term)
    return ap_series
first_term=int(input("please enter the first term"))
common_difference = int(input("please enter the number"))
num_terms = int(input("please enter the number"))
result=series(first_term,common_difference,num_terms)
print(result)


