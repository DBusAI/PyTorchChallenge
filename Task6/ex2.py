torch.manual_seed(23)
a1 = torch.rand((2, 3))
a2 = torch.rand((3, 4))
a3 = torch.rand((4, 5))
a4 = torch.rand((5, 6))

res = torch.chain_matmul(a1,a2,a3,a4)
assert np.allclose(res,a1@a2@a3@a4),"Not the Same!"