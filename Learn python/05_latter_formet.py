latter= '''Hello (name),
I'm very happy to tell you that you are selected for job,
Best wises for your future.
Smith.
(date)'''
name=input('Enter your name :')
date=input('Enter Date :')
latter=latter.replace("(name)",name)
latter=latter.replace("(date)",date)
print(latter)