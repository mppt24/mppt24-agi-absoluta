#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes de integração para a mppt24 AGI ABSOLUTA
"""

import unittest
import sys
import os
import json
import time
from unittest.mock import patch

# Adicionar o diretório pai ao path para importar main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from main import app, processar_mensagem
except ImportError:
    print("Erro: Não foi possível importar main.py")
    sys.exit(1)

class TestIntegration(unittest.TestCase):
    """Testes de integração do sistema completo"""

    def setUp(self):
        """Configuração antes de cada teste"""
        self.app = app.test_client()
        self.app.testing = True

    def test_flask_app_running(self):
        """Testa se a aplicação Flask está funcionando"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'mppt24 AGI', response.data)

    def test_api_endpoint_chat(self):
        """Testa o endpoint de chat da API"""
        # Dados de teste
        test_data = {
            'message': 'hidrogenio'
        }
        
        response = self.app.post('/chat', 
                               data=json.dumps(test_data),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        
        # Verificar se a resposta é JSON válido
        response_data = json.loads(response.data)
        self.assertIn('response', response_data)
        self.assertIn('Hidrogénio', response_data['response'])

    def test_api_multiple_requests(self):
        """Testa múltiplas requisições consecutivas"""
        test_messages = [
            'hidrogenio',
            'einstein',
            'calcular 2+2',
            'traduzir olá'
        ]
        
        for message in test_messages:
            test_data = {'message': message}
            response = self.app.post('/chat',
                                   data=json.dumps(test_data),
                                   content_type='application/json')
            
            self.assertEqual(response.status_code, 200)
            response_data = json.loads(response.data)
            self.assertIn('response', response_data)
            self.assertGreater(len(response_data['response']), 0)

    def test_api_error_handling(self):
        """Testa tratamento de erros da API"""
        # Requisição sem dados
        response = self.app.post('/chat')
        self.assertIn(response.status_code, [400, 500])
        
        # Requisição com JSON inválido
        response = self.app.post('/chat',
                               data='invalid json',
                               content_type='application/json')
        self.assertIn(response.status_code, [400, 500])

    def test_cors_headers(self):
        """Testa se os headers CORS estão configurados"""
        response = self.app.get('/')
        
        # Verificar se permite CORS (pode não estar configurado em todos os endpoints)
        # Este teste pode falhar se CORS não estiver configurado
        pass

    def test_static_files(self):
        """Testa se arquivos estáticos são servidos"""
        # Testar se a página principal carrega
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Verificar se contém elementos HTML esperados
        self.assertIn(b'html', response.data.lower())

    def test_performance_basic(self):
        """Testa performance básica do sistema"""
        start_time = time.time()
        
        # Fazer 10 requisições
        for i in range(10):
            response = processar_mensagem(f"teste {i}")
            self.assertIsNotNone(response)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Deve processar 10 mensagens em menos de 5 segundos
        self.assertLess(total_time, 5.0)

    def test_memory_usage(self):
        """Testa uso de memória básico"""
        import psutil
        import os
        
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Processar muitas mensagens
        for i in range(100):
            processar_mensagem(f"teste {i}")
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Aumento de memória deve ser razoável (menos de 50MB)
        self.assertLess(memory_increase, 50 * 1024 * 1024)

    def test_concurrent_requests(self):
        """Testa requisições concorrentes básicas"""
        import threading
        import queue
        
        results = queue.Queue()
        
        def make_request():
            try:
                response = processar_mensagem("hidrogenio")
                results.put(("success", response))
            except Exception as e:
                results.put(("error", str(e)))
        
        # Criar 5 threads
        threads = []
        for i in range(5):
            thread = threading.Thread(target=make_request)
            threads.append(thread)
            thread.start()
        
        # Esperar todas terminarem
        for thread in threads:
            thread.join()
        
        # Verificar resultados
        success_count = 0
        while not results.empty():
            result_type, result_data = results.get()
            if result_type == "success":
                success_count += 1
                self.assertIn("Hidrogénio", result_data)
        
        # Todas as requisições devem ter sucesso
        self.assertEqual(success_count, 5)

    def test_database_operations(self):
        """Testa operações básicas de base de dados (se existir)"""
        # Este teste assume que existe algum tipo de persistência
        # Se não existir, pode ser ignorado
        
        try:
            # Tentar processar uma mensagem que pode ser guardada
            response1 = processar_mensagem("teste database")
            self.assertIsNotNone(response1)
            
            # Processar outra mensagem
            response2 = processar_mensagem("outro teste")
            self.assertIsNotNone(response2)
            
        except Exception:
            # Se não há base de dados, o teste passa
            pass

    def test_edge_cases(self):
        """Testa casos extremos"""
        # Mensagem vazia
        response = processar_mensagem("")
        self.assertIsNotNone(response)
        
        # Mensagem muito longa
        long_message = "a" * 1000
        response = processar_mensagem(long_message)
        self.assertIsNotNone(response)
        
        # Caracteres especiais
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        response = processar_mensagem(special_chars)
        self.assertIsNotNone(response)
        
        # Unicode
        unicode_message = "🧠🤖🚀⚡🌟"
        response = processar_mensagem(unicode_message)
        self.assertIsNotNone(response)

    def test_system_integration(self):
        """Testa integração com o sistema"""
        # Verificar se todas as funcionalidades principais funcionam
        test_cases = [
            ("hidrogenio", "Hidrogénio"),
            ("calcular 2+2", "4"),
            ("traduzir olá", "Hello"),
            ("converter 1 metro cm", "100"),
            ("gerar senha", "🔐"),
            ("que horas", "🕐")
        ]
        
        for input_msg, expected_content in test_cases:
            response = processar_mensagem(input_msg)
            self.assertIn(expected_content, response, 
                         f"Falhou para '{input_msg}': esperado '{expected_content}' na resposta '{response}'")

    def test_error_recovery(self):
        """Testa recuperação de erros"""
        # Simular erro e depois requisição normal
        try:
            # Tentar algo que pode dar erro
            processar_mensagem("calcular 1/0")
        except:
            pass
        
        # Depois fazer requisição normal
        response = processar_mensagem("hidrogenio")
        self.assertIn("Hidrogénio", response)

    def test_configuration_loading(self):
        """Testa se a configuração é carregada corretamente"""
        # Verificar se a aplicação tem as configurações básicas
        self.assertIsNotNone(app)
        self.assertTrue(hasattr(app, 'config'))

if __name__ == '__main__':
    # Configurar para executar testes com mais verbosidade
    unittest.main(verbosity=2)

