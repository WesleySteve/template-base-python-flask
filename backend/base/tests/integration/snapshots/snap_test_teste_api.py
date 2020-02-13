# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_obter_todos_testes_api 1'] = {
    'testes': [
        {
            'id': 1,
            'nome': 'Intel',
            'status': True
        },
        {
            'id': 2,
            'nome': 'AMD',
            'status': True
        },
        {
            'id': 3,
            'nome': 'HP',
            'status': True
        }
    ]
}

snapshots['test_adicionar_teste 1'] = {
    'teste': {
        'id': 1,
        'nome': 'teste adicionar',
        'status': True
    }
}
