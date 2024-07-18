from tinygrad import Tensor

if __name__=="__main__":
  a = Tensor.rand(1)
  b = Tensor.rand(1)
  c = a + b
  c.realize()
  print(a.item(), b.item(), c.item())