from django.test import TestCase
from unittest.mock import Mock

from Produto.models import Produto

#['nome', 'marca', 'modelo', 'fornecedor']

class ProdutoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Produto.objects.create(nome="Chromebook de 11,6", marca="LENOVO", modelo="100E Celeron N4020" fornecedor="Miranda", preco_de_venda=2.098)
        Produto.objects.create(nome="ASPIRE 3", marca="ACER", modelo="CELERON N4500", fornecedor="Nargem", preco_de_venda=2.598)
        Produto.objects.create(nome="Galaxy Book Go", marca="SAMSUNG", modelo="Galaxy", fornecedor="Ibyte", qnt_em_estoque=50, preco_de_venda=2.248)
        Produto.objects.create(nome="MacBook Pro 13", marca="Apple", modelo="MacBook" fornecedor="Magalu", qnt_em_estoque=3, preco_de_venda=10.349)
    
    def test_ordering(self):
        lista_ordenada = [Produto.objects.get(id=3), Produto.objects.get(id=4),
                            Produto.objects.get(id=2), Produto.objects.get(id=1)]
        # lista_ordenada = Produtos.objects.all().order_by('nome', 'fornecedor')
        # produtos = list(Produtos.objects.all())
        produtos = [entry for entry in Produto.objects.all()]
        self.assertEquals(lista_ordenada, produtos)

    def test_nome_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('nome').verbose_name
        self.assertEquals(label_do_produto, "Nome")
    
    def test_fornecedor_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('fornecedor').verbose_name
        self.assertTrue(label_do_produto == "Fornecedor")

    def test_qnt_em_estoque_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('qnt_em_estoque').verbose_name
        self.assertEquals(label_do_produto, "Quantidade em estoque")

    def test_qnt_em_estoque_default(self):
        produto = Produto.objects.get(id=1)
        valor_default = produto.qnt_em_estoque
        self.assertEquals(valor_default, 0)

    def test_preco_de_venda_label(self):
        produto = Produto.objects.get(id=1)
        label_do_produto = produto._meta.get_field('preco_de_venda').verbose_name
        self.assertEquals(label_do_produto, "Preço de venda")
    
    def test_nome_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('nome').max_length
        self.assertEquals(max_length, 200)
    
    def test_fornecedor_max_length(self):
        produto = Produto.objects.get(id=1)
        max_length = produto._meta.get_field('fornecedor').max_length
        self.assertEquals(max_length, 200)

    def test_situacao(self):
        produto = Produto.objects.get(id=1)
        situacao = produto.situacao
        self.assertEquals(situacao, "1")

                        