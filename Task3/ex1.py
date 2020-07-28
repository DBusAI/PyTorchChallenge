x=torch.arange(1,4)
y = torch.combinations(x,with_replacement=True)
assert np.allclose(y,[[1, 1],
                    [1, 2],
                    [1, 3],
                    [2, 2],
                    [2, 3],
                    [3, 3]]),"Not the Same"