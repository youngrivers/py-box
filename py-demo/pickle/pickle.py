import pickle
d=dict(name='Bob',age=20,score=88)
with open('1.txt','wb')as f:
    pickle.dump(d,f)
with open('1.txt','rb')as f:
	pickle.load(f)