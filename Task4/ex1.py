# v1
x = torch.arange(4*4).view(4,-1)
res = x.narrow(0,1,2).narrow(1,1,2).clone()
x[1,1]=3
assert np.allclose(res,[[ 5,  6],
                        [ 9, 10]]),"Not the Same!"

# v2
x = torch.arange(4*4).view(4,-1)
res = x[1:3,1:3].clone()
x[1,1]=3
assert np.allclose(res,[[ 5,  6],
                        [ 9, 10]]),"Not the Same!"