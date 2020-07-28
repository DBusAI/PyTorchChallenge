x = torch.FloatTensor([1,2,3])
res = torch.reciprocal(x)
assert np.allclose(res,1/x), "Not the same!"