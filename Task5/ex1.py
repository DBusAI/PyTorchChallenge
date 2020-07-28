a=torch.FloatTensor([1,2,3])
b=torch.FloatTensor([2,3,4])
m = torch.dist(a,b,1)
e = torch.dist(a,b,2)
assert np.allclose(m,3)&np.allclose(e,1.7320508),"Not the same!"