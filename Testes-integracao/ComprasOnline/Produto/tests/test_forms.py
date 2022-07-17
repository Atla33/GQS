from django.test import TestCase

from Produto.models import Produto
from Produto.forms import ProdutoForm

class ProdutoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produto.objects.create(nome="MacBook Pro 13", marca="Apple", modelo="MacBook" fornecedor="Magalu", qnt_em_estoque=3, preco_de_venda=10.349)

    def test_produto_fornecedor_existente(self):
        form = ProdutoForm(data={'nome': 'MacBook Pro 13', 'marca': 'Apple', 'modelo': 'MacBook', 'fornecedor': 'Magalu', 'preco_de_venda':10.349})
        self.assertFalse(form.is_valid())
    
    def test_produto_fornecedor_nao_existente_1(self):
        form = ProdutoForm(data={'nome': 'MacBook Pro 13', 'marca': 'Apple', 'modelo': 'MacBook', 'fornecedor': 'Miranda', 'preco_de_venda':13.500})
        self.assertTrue(form.is_valid())

    def test_produto_fornecedor_nao_existente_2(self):
        form = ProdutoForm(data={'nome': 'Galaxy Book Go', 'marca': 'SAMSUNG', 'modelo': 'Galaxy', 'fornecedor': 'Magalu', 'preco_de_venda':2.248})
        self.assertTrue(form.is_valid())

    def test_elementos_obrigatorios_1(self):
        form = ProdutoForm(data={'nome': '', 'marca': 'SAMSUNG', 'modelo': 'Galaxy', 'fornecedor': 'Magalu', 'preco_de_venda': 2.248})
        self.assertFalse(form.is_valid())

    def test_elementos_obrigatorios_2(self):
        form = ProdutoForm(data={'nome': 'Galaxy Book Go', 'marca': 'SAMSUNG', 'modelo': 'Galaxy', 'fornecedor': '', 'preco_de_venda': 2.248})
        self.assertFalse(form.is_valid())