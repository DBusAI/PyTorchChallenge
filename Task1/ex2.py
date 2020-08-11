x = torch.arange(10000).float()
numpy_std = x.numpy().std()
torch_std = x.std(unbiased=False)
assert np.allclose(torch_std,numpy_std),"Not the same!"
