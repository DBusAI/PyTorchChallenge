A = torch.arange(10,dtype=torch.float32).reshape(5,2)
B = torch.FloatTensor([[ 2.],[ 8.],[14.],[20.],[26.]])
X = torch.lstsq(B,A)[0][:2]
assert np.allclose(A@X,B),"Not the same!"