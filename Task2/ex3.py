a = torch.tensor([1,3,2,4])
b = torch.repeat_interleave(a,a)
assert np.allclose(b,[1, 3, 3, 3, 2, 2, 4, 4, 4, 4]),"Not the same!"