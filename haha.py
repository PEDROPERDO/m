def pali(sentence : str) -> bool:
  """
  >>> print(pali("rar"))
  True
  """
  return sentence == sentence[::-1]

if __name__ == "__main__":
  import doctest
  doctest.testmod()
