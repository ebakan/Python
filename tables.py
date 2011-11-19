tables=lambda f,x: '\n'.join([': '.join(k) for k in zip([str(i) for i in x],[str(f(i)) for i in x])])
