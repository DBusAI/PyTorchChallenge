x = torch.FloatTensor([0,1,float("inf")])
res = torch.isinf(x)
assert np.allclose(res,[False,False,True]), "Not the same!"