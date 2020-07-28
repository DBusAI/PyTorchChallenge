res = torch.finfo(torch.float32).eps -  torch.finfo(torch.float16).eps
assert np.allclose(res,-0.0009764432907104492,rtol=1e-8), "Not the same!"