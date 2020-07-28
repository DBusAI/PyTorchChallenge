torch.manual_seed(2121)
a = torch.randn(5, 128)
b = torch.randn(5, 128)
res = torch.cosine_similarity(a, b)
assert np.allclose(res,torch.tensor([ 0.1203, -0.0406, -0.0571, -0.0857,  0.0572]),rtol=1e-3), "Not the same!"