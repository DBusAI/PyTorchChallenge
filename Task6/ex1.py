torch.manual_seed(23)
x = torch.randint(0,10,(4,4))
res = x.rot90().trace()
assert res.item()==24,"Not the Same!"