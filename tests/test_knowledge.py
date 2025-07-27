#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes para o sistema de conhecimento da mppt24 AGI ABSOLUTA
"""

import unittest
import sys
import os

# Adicionar o diretório pai ao path para importar main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import processar_mensagem

class TestKnowledgeSystem(unittest.TestCase):
    """Testes para o sistema de conhecimento universal"""

    def test_elementos_quimicos(self):
        """Testa o conhecimento sobre elementos químicos"""
        # Elemento 1 - Hidrogénio
        response = processar_mensagem("hidrogenio")
        self.assertIn("Hidrogénio", response)
        self.assertIn("elemento 1", response)
        
        # Elemento 118 - Oganessão
        response = processar_mensagem("oganessao")
        self.assertIn("Oganessão", response)
        self.assertIn("elemento 118", response)
        
        # Elemento comum - Oxigénio
        response = processar_mensagem("oxigenio")
        self.assertIn("Oxigénio", response)
        self.assertIn("elemento 8", response)

    def test_pessoas_famosas(self):
        """Testa o conhecimento sobre pessoas famosas"""
        # Cientista
        response = processar_mensagem("einstein")
        self.assertIn("Einstein", response)
        self.assertIn("físico", response)
        
        # Futebolista
        response = processar_mensagem("messi")
        self.assertIn("Messi", response)
        self.assertIn("futebolista", response)
        
        # Futebolista português
        response = processar_mensagem("ronaldo")
        self.assertIn("Ronaldo", response)
        self.assertIn("português", response)

    def test_animais(self):
        """Testa o conhecimento sobre animais"""
        # Rei da selva
        response = processar_mensagem("leao")
        self.assertIn("Leão", response)
        self.assertIn("selva", response)
        
        # Animal doméstico
        response = processar_mensagem("cao")
        self.assertIn("Cão", response)
        self.assertIn("doméstico", response)
        
        # Animal aquático
        response = processar_mensagem("tubarao")
        self.assertIn("Tubarão", response)
        self.assertIn("predador", response)

    def test_paises(self):
        """Testa o conhecimento sobre países"""
        # Portugal
        response = processar_mensagem("portugal")
        self.assertIn("Portugal", response)
        self.assertIn("Europa", response)
        
        # Brasil
        response = processar_mensagem("brasil")
        self.assertIn("Brasil", response)
        self.assertIn("América", response)
        
        # França
        response = processar_mensagem("franca")
        self.assertIn("França", response)
        self.assertIn("Europa", response)

    def test_comidas(self):
        """Testa o conhecimento sobre comidas"""
        # Pizza
        response = processar_mensagem("pizza")
        self.assertIn("Pizza", response)
        self.assertIn("italiana", response)
        
        # Sushi
        response = processar_mensagem("sushi")
        self.assertIn("Sushi", response)
        self.assertIn("japonesa", response)
        
        # Francesinha
        response = processar_mensagem("francesinha")
        self.assertIn("Francesinha", response)
        self.assertIn("Porto", response)

    def test_tecnologia(self):
        """Testa o conhecimento sobre tecnologia"""
        # Apple
        response = processar_mensagem("apple")
        self.assertIn("Apple", response)
        self.assertIn("tecnologia", response)
        
        # Google
        response = processar_mensagem("google")
        self.assertIn("Google", response)
        self.assertIn("pesquisa", response)
        
        # Bitcoin
        response = processar_mensagem("bitcoin")
        self.assertIn("Bitcoin", response)
        self.assertIn("criptomoeda", response)

    def test_comandos_linux(self):
        """Testa o conhecimento sobre comandos Linux"""
        # sudo apt update
        response = processar_mensagem("sudo apt update")
        self.assertIn("sudo apt update", response)
        self.assertIn("atualiza", response)
        
        # git clone
        response = processar_mensagem("git clone")
        self.assertIn("git clone", response)
        self.assertIn("repositório", response)
        
        # docker run
        response = processar_mensagem("docker run")
        self.assertIn("docker run", response)
        self.assertIn("container", response)

    def test_medicina(self):
        """Testa o conhecimento sobre medicina"""
        # DNA
        response = processar_mensagem("dna")
        self.assertIn("DNA", response)
        self.assertIn("genético", response)
        
        # Vacina
        response = processar_mensagem("vacina")
        self.assertIn("Vacina", response)
        self.assertIn("imunidade", response)
        
        # Coração
        response = processar_mensagem("coracao")
        self.assertIn("Coração", response)
        self.assertIn("sangue", response)

    def test_matematica(self):
        """Testa o conhecimento sobre matemática"""
        # Pi
        response = processar_mensagem("pi")
        self.assertIn("Pi", response)
        self.assertIn("3.14159", response)
        
        # Fibonacci
        response = processar_mensagem("fibonacci")
        self.assertIn("Fibonacci", response)
        self.assertIn("sequência", response)
        
        # Infinito
        response = processar_mensagem("infinito")
        self.assertIn("Infinito", response)
        self.assertIn("matemático", response)

    def test_historia(self):
        """Testa o conhecimento sobre história"""
        # Roma
        response = processar_mensagem("roma")
        self.assertIn("Roma", response)
        self.assertIn("império", response)
        
        # Revolução Francesa
        response = processar_mensagem("revolucao francesa")
        self.assertIn("Revolução Francesa", response)
        self.assertIn("1789", response)
        
        # Segunda Guerra Mundial
        response = processar_mensagem("segunda guerra mundial")
        self.assertIn("Segunda Guerra", response)
        self.assertIn("1939", response)

    def test_filosofia(self):
        """Testa o conhecimento sobre filosofia"""
        # Sócrates
        response = processar_mensagem("socrates")
        self.assertIn("Sócrates", response)
        self.assertIn("filósofo", response)
        
        # Existencialismo
        response = processar_mensagem("existencialismo")
        self.assertIn("Existencialismo", response)
        self.assertIn("filosofia", response)

    def test_case_insensitive(self):
        """Testa se o sistema é case-insensitive"""
        # Maiúsculas
        response1 = processar_mensagem("EINSTEIN")
        response2 = processar_mensagem("einstein")
        self.assertEqual(response1, response2)
        
        # Misto
        response3 = processar_mensagem("EiNsTeIn")
        self.assertEqual(response1, response3)

    def test_acentos(self):
        """Testa se o sistema funciona com e sem acentos"""
        # Com acento
        response1 = processar_mensagem("oxigénio")
        # Sem acento
        response2 = processar_mensagem("oxigenio")
        
        # Ambos devem funcionar
        self.assertIn("Oxigénio", response1)
        self.assertIn("Oxigénio", response2)

if __name__ == '__main__':
    unittest.main()

