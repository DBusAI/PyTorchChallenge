# v1
a = torch.arange(28).reshape(7,-1)
chunk_a = torch.chunk(a,3)
assert np.allclose([torch.sum(i).item() for i in chunk_a],
                    [66, 210, 102]), "Not the Same"

# v2
a = torch.arange(28).reshape(7,-1)
chunk_a = torch.split(a,3)
assert np.allclose([torch.sum(i).item() for i in chunk_a],
                    [66, 210, 102]), "Not the Same"
