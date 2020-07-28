# v1
x = torch.tensor([1,3,7,5,2])
res = x[torch.randperm(x.nelement())]
assert np.allclose(torch.sort(res)[0],torch.sort(x)[0])&(~np.allclose(res,x)),"The Same!"

# v2
x = torch.tensor([1,3,7,5,2])
res = torch.take(x,torch.randperm(x.nelement()))
assert np.allclose(torch.sort(res)[0],torch.sort(x)[0])&(~np.allclose(res,x)),"The Same!"