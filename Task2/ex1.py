torch.manual_seed(23)
a = torch.tensor([0.4,0.2,0.5,0.6,0.8])
res = a.bernoulli()
assert np.allclose(res.numpy(),[0., 0., 1., 1., 0.]),"Not the same!"