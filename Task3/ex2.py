x=torch.arange(1,4)
y = torch.cartesian_prod(x,x)
assert np.allclose(y,[[1, 1],
                    [1, 2],
                    [1, 3],
                    [2, 1],
                    [2, 2],
                    [2, 3],
                    [3, 1],
                    [3, 2],
                    [3, 3]]),"Not the Same"