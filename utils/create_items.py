import os
import sys
from datetime import datetime
from pathlib import Path

import django
import pandas as pd
from django.conf import settings

# Configurações Django
DJANGO_BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(DJANGO_BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
settings.USE_TZ = False

django.setup()

# Imports após setup
from item.models import Item, Category  
from django.contrib.auth.models import User

# Caminho do Excel
EXCEL_PATH = os.path.join(DJANGO_BASE_DIR, 'utils', 'itens_carrinho_de_emergencia.xlsx')

# Verificar se o arquivo existe
if not os.path.exists(EXCEL_PATH):
    print(f"Arquivo {EXCEL_PATH} não encontrado.")
    sys.exit(1)

# Lê o arquivo Excel
df = pd.read_excel(EXCEL_PATH)

# Seleciona um usuário qualquer como owner
owner = User.objects.first()

# Lista para armazenar itens
items_to_create = []

# Processamento do arquivo
for index, row in df.iterrows():
    try:
        # Garante que a categoria exista
        category_name = row['category']
        category, _ = Category.objects.get_or_create(name=category_name)
        
        # Processa a data de validade com tratamento de erro
        expiration_date = pd.to_datetime(row['expiration_date'], errors='raise').date()
    except ValueError as e:
        print(f"Erro ao processar data na linha {index}: {row['expiration_date']}. Item será ignorado.")
        continue  # Continua com o próximo item em caso de erro com a data
    except Exception as e:
        print(f"Erro ao processar a linha {index}: {e}. Item será ignorado.")
        continue  # Continua com o próximo item em caso de erro geral
    
    # Criação do item
    item = Item(
        item=row['item'],
        amount=int(row['amount']),
        expiration_date=expiration_date,
        created_date=datetime.now(),
        show=True,
        category=category,
        owner=owner
    )
    items_to_create.append(item)

# Salva todos os itens no banco de dados de uma vez
if items_to_create:
    Item.objects.bulk_create(items_to_create)
    print(f"{len(items_to_create)} itens criados com sucesso.")
else:
    print("Nenhum item foi criado.")