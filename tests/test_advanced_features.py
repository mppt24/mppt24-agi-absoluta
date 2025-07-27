#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para as funcionalidades avançadas da mppt24 AGI ABSOLUTA
"""

import unittest
import sys
import os
import re

# Adicionar o diretório pai ao path para importar main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import processar_mensagem

class TestAdvancedFeatures(unittest.TestCase):
    """Testes para funcionalidades avançadas"""

    def test_calculadora_basica(self):
        """Testa operações básicas da calculadora"""
        # Soma
        response = processar_mensagem("calcular 2+2")
        self.assertIn("4", response)
        
        # Multiplicação
        response = processar_mensagem("calcular 3*4")
        self.assertIn("12", response)
        
        # Divisão
        response = processar_mensagem("calcular 10/2")
        self.assertIn("5", response)

    def test_calculadora_cientifica(self):
        """Testa funções científicas da calculadora"""
        # Raiz quadrada
        response = processar_mensagem("calcular sqrt(16)")
        self.assertIn("4", response)
        
        # Seno
        response = processar_mensagem("calcular sin(0)")
        self.assertIn("0", response)
        
        # Logaritmo
        response = processar_mensagem("calcular log(100)")
        self.assertIn("2", response)

    def test_calculadora_constantes(self):
        """Testa constantes matemáticas"""
        # Pi
        response = processar_mensagem("calcular pi")
        self.assertIn("3.14", response)
        
        # Euler
        response = processar_mensagem("calcular e")
        self.assertIn("2.71", response)

    def test_tradutor(self):
        """Testa o sistema de tradução"""
        # Olá
        response = processar_mensagem("traduzir olá")
        self.assertIn("Hello", response)
        self.assertIn("Hola", response)
        self.assertIn("Bonjour", response)
        self.assertIn("Ciao", response)
        
        # Obrigado
        response = processar_mensagem("traduzir obrigado")
        self.assertIn("Thank you", response)
        self.assertIn("Gracias", response)
        self.assertIn("Merci", response)
        self.assertIn("Grazie", response)

    def test_conversor_unidades(self):
        """Testa o conversor de unidades"""
        # Metro para centímetros
        response = processar_mensagem("converter 1 metro em cm")
        self.assertIn("100", response)
        self.assertIn("centímetros", response)
        
        # Quilómetros para metros
        response = processar_mensagem("converter 1 km em metros")
        self.assertIn("1000", response)
        self.assertIn("metros", response)
        
        # Quilogramas para gramas
        response = processar_mensagem("converter 1 kg em gramas")
        self.assertIn("1000", response)
        self.assertIn("gramas", response)

    def test_conversor_temperatura(self):
        """Testa conversão de temperatura"""
        # Celsius para Fahrenheit
        response = processar_mensagem("converter 0 celsius fahrenheit")
        self.assertIn("32", response)
        self.assertIn("Fahrenheit", response)
        
        # Fahrenheit para Celsius
        response = processar_mensagem("converter 32 fahrenheit celsius")
        self.assertIn("0", response)
        self.assertIn("Celsius", response)

    def test_conversor_tempo(self):
        """Testa conversão de tempo"""
        # Horas para minutos
        response = processar_mensagem("converter 1 hora minutos")
        self.assertIn("60", response)
        self.assertIn("minutos", response)
        
        # Dias para horas
        response = processar_mensagem("converter 1 dia horas")
        self.assertIn("24", response)
        self.assertIn("horas", response)

    def test_gerador_senha(self):
        """Testa o gerador de senhas"""
        response = processar_mensagem("gerar senha")
        
        # Deve conter uma senha
        self.assertIn("🔐", response)
        self.assertIn("Senha", response)
        
        # Procurar por uma string que parece uma senha (12 caracteres)
        senha_match = re.search(r'[A-Za-z0-9@#$%^&*!]{12}', response)
        self.assertIsNotNone(senha_match, "Senha de 12 caracteres não encontrada")

    def test_informacoes_sistema(self):
        """Testa informações do sistema"""
        # Hora atual
        response = processar_mensagem("que horas")
        self.assertIn("🕐", response)
        self.assertIn(":", response)  # Formato de hora
        
        # Data atual
        response = processar_mensagem("data hoje")
        self.assertIn("📅", response)
        # Deve conter um ano (4 dígitos)
        self.assertTrue(re.search(r'\d{4}', response))

    def test_conversacao_basica(self):
        """Testa conversação básica"""
        # Cumprimentos
        response = processar_mensagem("ola")
        self.assertIn("Olá", response)
        
        response = processar_mensagem("oi")
        self.assertIn("Oi", response)
        
        response = processar_mensagem("bom dia")
        self.assertIn("Bom dia", response)
        
        # Agradecimentos
        response = processar_mensagem("obrigado")
        self.assertIn("obrigado", response.lower())
        
        # Despedidas
        response = processar_mensagem("tchau")
        self.assertIn("tchau", response.lower())

    def test_conversacao_natural(self):
        """Testa conversação natural específica"""
        # Pergunta comum
        response = processar_mensagem("ola tudo bem")
        self.assertIn("Olá", response)
        self.assertIn("bem", response)
        
        # Como estás
        response = processar_mensagem("como estas")
        self.assertIn("estou", response.lower())

    def test_funcionalidades_combinadas(self):
        """Testa combinação de funcionalidades"""
        # Calcular e depois traduzir
        calc_response = processar_mensagem("calcular 2+2")
        self.assertIn("4", calc_response)
        
        trad_response = processar_mensagem("traduzir olá")
        self.assertIn("Hello", trad_response)
        
        # Ambas devem funcionar independentemente
        self.assertNotEqual(calc_response, trad_response)

    def test_entrada_invalida(self):
        """Testa comportamento com entrada inválida"""
        # Cálculo inválido
        response = processar_mensagem("calcular abc")
        self.assertIn("erro", response.lower())
        
        # Conversão inválida
        response = processar_mensagem("converter xyz")
        # Deve dar uma resposta, mesmo que não seja específica
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)

    def test_case_insensitive_funcionalidades(self):
        """Testa se as funcionalidades são case-insensitive"""
        # Calculadora
        response1 = processar_mensagem("CALCULAR 2+2")
        response2 = processar_mensagem("calcular 2+2")
        self.assertEqual(response1, response2)
        
        # Tradutor
        response3 = processar_mensagem("TRADUZIR olá")
        response4 = processar_mensagem("traduzir olá")
        self.assertEqual(response3, response4)

    def test_espacos_extras(self):
        """Testa comportamento com espaços extras"""
        # Espaços antes e depois
        response1 = processar_mensagem("  calcular 2+2  ")
        response2 = processar_mensagem("calcular 2+2")
        self.assertEqual(response1, response2)
        
        # Múltiplos espaços
        response3 = processar_mensagem("calcular   2+2")
        self.assertEqual(response1, response3)

if __name__ == '__main__':
    unittest.main()

