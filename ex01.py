#Herança em python
from biblioteca import *

# gato = Gato("Epaminondas", "Frajola")
# coelho1 = Coelho("Pernalonga", "Cinza")
# cachorro1 = Cachorro("Caramelo", "Caramelo")
# vaca1 = Vaca("Mimosa", "Malhada")
#
# cachorro1.latir()
# gato.miar()
# vaca1.mugir()
# coelho1.morrer()
valor = 25
ingresso_normal = Ingresso(valor)
ingresso_normal.imprimeValor()

ingresso_vip = IngressoVip(valor)
ingresso_vip.imprimeValor()
