# f-Strings usage

'''
website = "ekika.co"
print(f"Hello, {website}")

num = 10
print(f"{num} + 10 = {num + 10}")

print(f"""He said {"I'm Meet"}""")

print(f'5 {"{stars}"}')

print(f'{{5}} {"stars"}')

name = "Meet"
age = 22

print(f"""Hello!
        I'm {name}.
        I'm {age}.""")
'''

# f-Strings Fill Align

"""
print(f'{"text":10}') 
print(f'{"test":*>10}')  
print(f'{"test":*<10}')
print(f'{"test":*^10}') 
print(f'{12345:0>10}')  
"""

# f-Strings type


"""
print(f'{10:b}')
print(f'{10:o}')
print(f'{200:x}')
print(f'{200:X}')
print(f'{34560000000000:e}')
print(f'{65:c}')
print(f'{10:#b}')
print(f'{10:#o}')
print(f'{10:#x}')
"""

# F-Strings Others

"""
print(f'{-12345:0=10}')  
print(f'{12345:010}')    
print(f'{-12345:010}')

import math       
math.pi
print(f'{math.pi:.2f}')
print(f'{1000000:,.2f}') 
print(f'{1000000:_.2f}')
print(f'{0.25:0%}')
print(f'{0.25:.0%}')
"""

# f-Strings Sign

"""
print(f'{12345:+}')
print(f'{-12345:+}')
print(f'{-12345:+10}')
print(f'{-12345:+010}')
"""
