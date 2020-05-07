def caught_speeding(speed, is_birthday):
  noTicket = 0
  smallTicket = 1
  bigTicket = 2
  if is_birthday is True:
    if speed <= 65:
      return noTicket
    elif 66 <= speed <= 85:
      return smallTicket
    elif speed >= 86:
      return bigTicket
  elif speed <= 60:
    return noTicket
  elif speed >= 61 and speed <= 80:
    return smallTicket
  elif speed >= 81:
    return bigTicket