torch_std = torch.arange(10000,dtype=torch.float32).std(unbiased=False).numpy()
numpy_std = np.arange(10000).std()
assert np.allclose(torch_std,numpy_std),"Not the same!"