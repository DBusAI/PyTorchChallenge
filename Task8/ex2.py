x = torch.tensor([1,1,1,1,2,2,2,34,1])
res = torch.mode(x)[1]
assert np.allclose(res,8),"Not the same!"