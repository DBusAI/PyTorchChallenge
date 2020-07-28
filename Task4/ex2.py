x = torch.arange(10)
res = torch.split(x,list(range(1,5)))
assert np.allclose([sum(i).item() for i in res],
            [0, 3, 12, 30]),"Not the Same!"