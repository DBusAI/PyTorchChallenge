v1 = torch.arange(4., 1,-1)
v2 = torch.arange(1., 4)
res_etalon = v1.reshape(-1,1)*v2.reshape(1,-1)
res = torch.ger(v1,v2)
assert np.allclose(res,res_etalon), "Not the same!"