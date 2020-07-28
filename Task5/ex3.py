y = torch.arange(0,5)
y_ = torch.trapz(y)
assert np.allclose(y_,8),"Not the same!"