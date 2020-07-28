# v1
x = torch.empty(size=(10,10)).fill_(23)
assert np.allclose(x.numpy(),
                   np.ones(shape=(10,10))*23), "Not the Same"

# v2
x = torch.ones(size=(10,10))*23
assert np.allclose(x.numpy(),
                   np.ones(shape=(10,10))*23), "Not the Same"

# v3
x = torch.full((10,10),23)
assert np.allclose(x.numpy(),
                   np.ones(shape=(10,10))*23), "Not the Same"