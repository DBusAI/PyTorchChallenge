x = torch.linspace(1.2,1.5,10)
assert np.allclose(x,[1.2000, 1.2333, 1.2667, 
                      1.3000, 1.3333, 1.3667, 
                      1.4000, 1.4333, 1.4667, 1.5000],rtol=1e-3), "Not the Same"