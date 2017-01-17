class Car(object):
  speed = 0
  num_of_doors = 4
  num_of_wheels = 4

  def __init__(self,car_name='General',car_model='GM',car_type=''):
    self.car_type = car_type
    self.name = car_name
    self.model = car_model
    if car_name == 'Porshe' or car_name == 'Koenigsegg':
      self.num_of_doors = 2
    elif car_type == 'trailer':
      self.num_of_wheels = 8

  def drive(self,i):
    return self

  def is_saloon(self):
    if self.car_type == 'trailer':
      self.car_type = Car('Nissan','ns-gt','saloon')
      return self.car_type
