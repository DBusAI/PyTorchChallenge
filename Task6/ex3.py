x = torch.FloatTensor([1, 6, 5, 7, 0, 2])
res = torch.abs(x - torch.cummax(x,0)[0])
assert np.allclose(res,[0., 0., 1., 0., 7., 5.]),"Not the Same!"