a = torch.logspace(-10,-3,5)
res = torch.erfinv(a)
assert np.allclose(res,torch.tensor([8.8623e-11, 4.9836e-09, 2.8025e-07, 1.5760e-05, 8.8623e-04]),rtol=1e-4), "Not the same!"