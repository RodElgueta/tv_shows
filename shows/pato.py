clients = [
   {'id': 1, 'tax_number': '86620855', 'name': 'HECTOR ACUÑA BOLAÑOS'},
   {'id': 2, 'tax_number': '7317855K', 'name': 'JESUS RODRIGUEZ ALVAREZ'},
   {'id': 3, 'tax_number': '73826497', 'name': 'ANDRES NADAL MOLINA'},
   {'id': 4, 'tax_number': '88587715', 'name': 'SALVADOR ARNEDO MANRIQUEZ'},
   {'id': 5, 'tax_number': '94020190', 'name': 'VICTOR MANUEL ROJAS LUCAS'},
   {'id': 6, 'tax_number': '99804238', 'name': 'MOHAMED FERRE SAMPER'}
]

accounts = [
   {'client_id': 6, 'bank_id': 1, 'balance': 15000},
   {'client_id': 1, 'bank_id': 3, 'balance': 18000},
   {'client_id': 5, 'bank_id': 3, 'balance': 135000},
   {'client_id': 2, 'bank_id': 2, 'balance': 5600},
   {'client_id': 3, 'bank_id': 1, 'balance': 23000},
   {'client_id': 5, 'bank_id': 2, 'balance': 15000},
   {'client_id': 3, 'bank_id': 3, 'balance': 45900},
   {'client_id': 2, 'bank_id': 3, 'balance': 19000},
   {'client_id': 4, 'bank_id': 3, 'balance': 51000},
   {'client_id': 5, 'bank_id': 1, 'balance': 89000},
   {'client_id': 1, 'bank_id': 2, 'balance': 1600},
   {'client_id': 5, 'bank_id': 3, 'balance': 37500},
   {'client_id': 6, 'bank_id': 1, 'balance': 19200},
   {'client_id': 2, 'bank_id': 3, 'balance': 10000},
   {'client_id': 3, 'bank_id': 2, 'balance': 5400},
   {'client_id': 3, 'bank_id': 1, 'balance': 9000},
   {'client_id': 4, 'bank_id': 3, 'balance': 13500},
   {'client_id': 2, 'bank_id': 1, 'balance': 38200},
   {'client_id': 5, 'bank_id': 2, 'balance': 17000},
   {'client_id': 1, 'bank_id': 3, 'balance': 1000},
   {'client_id': 5, 'bank_id': 2, 'balance': 600},
   {'client_id': 6, 'bank_id': 1, 'balance': 16200},
   {'client_id': 2, 'bank_id': 2, 'balance': 10000}
]

banks = [
   {'id': 1, 'name': 'SANTANDER'},
   {'id': 2, 'name': 'CHILE'},
   {'id': 3, 'name': 'ESTADO'}
]

import functools
# Arreglo con los nombres de cliente ordenados de mayor a menor por la suma total de sus cuentas
result = sorted([
    {
      'name': client['name'],
      'total': functools.reduce(
        lambda num1, num2: num1 + num2,
        [account['balance'] for account in accounts if account['client_id'] == client['id']]
      )
    } for client in clients
], key=lambda item: item['total'], reverse=True)
from pprint import pprint
pprint(result)
