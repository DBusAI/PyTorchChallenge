# v1
torch.manual_seed(23)
a = torch.randint(0,10,(5,5))
index_cols= torch.tensor([1, 3])
res = torch.index_select(a,1,index_cols)
assert np.allclose(res.numpy(),[[6, 7],
                                [7, 4],
                                [6, 7],
                                [5, 9],
                                [9, 0]]),"Not the same!"

# v2
torch.manual_seed(23)
a = torch.randint(0,10,(5,5))
index_cols= torch.tensor([1, 3])
res = a[:,index_cols]
assert np.allclose(res.numpy(),[[6, 7],
                                [7, 4],
                                [6, 7],
                                [5, 9],
                                [9, 0]]),"Not the same!"