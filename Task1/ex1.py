# v1
a = np.array([1,2,3])
b = torch.from_numpy(a)
a[0]=-1
assert np.all(a==b.numpy()),"Not the same!"

# v2
a = np.array([1,2,3])
b = torch.as_tensor(a)
a[0]=-1
assert np.all(a==b.numpy()),"Not the same!"