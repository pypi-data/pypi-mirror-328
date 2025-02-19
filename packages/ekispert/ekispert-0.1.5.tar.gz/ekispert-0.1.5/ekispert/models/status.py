from ..base import Base

class Status(Base):
  def __init__(self, data = None):
    super().__init__()
    if data is None:
      return
    self.sets(data)

  def sets(self, data):
    for key in data:
      self.set(key, data[key])

  def set(self, key: str, value: any):
    match key.lower():
      case "code":
        self.code = int(value)
      case _:
        raise ValueError(f"key: {key} is not defined in Satus")
