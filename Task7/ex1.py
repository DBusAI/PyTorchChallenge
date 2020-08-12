x = torch.tensor([0,1,2,3,1,1,2,5])
res = torch.bincount(x)
assert np.allclose(res,[1, 3, 2, 1, 0, 1]), "Not the same!"
