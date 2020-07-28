# v0
x = torch.tensor([[1,2],
                  [3,4]])
y = torch.tensor([[5,6],
                  [7,8]])
xy = torch.matmul(x,y)
assert np.allclose(xy,np.dot(x,y)),"Not the same!"

# v1
x = torch.tensor([[1,2],
                  [3,4]])
y = torch.tensor([[5,6],
                  [7,8]])
xy = x.mm(y)
assert np.allclose(xy,np.dot(x,y)),"Not the same!"

# v2
x = torch.tensor([[1,2],
                  [3,4]])
y = torch.tensor([[5,6],
                  [7,8]])
xy = x@y
assert np.allclose(xy,np.dot(x,y)),"Not the same!"

# v3
x = torch.tensor([[1,2],
                  [3,4]])
y = torch.tensor([[5,6],
                  [7,8]])
xy = torch.einsum('ij,jk->ik',x,y)
assert np.allclose(xy,np.dot(x,y)),"Not the same!"