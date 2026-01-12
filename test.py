from database.dao import DAO
from model.model import Model
#print(DAO.read_state())
#print(DAO.read_sighting())

m=Model()

print(m.build_graph(1999, 'triangle'))