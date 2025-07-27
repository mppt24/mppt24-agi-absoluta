#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar todos os testes da mppt24 AGI ABSOLUTA

Este script executa todos os testes automatizados e gera um relatório
detalhado dos resultados.

Uso:
    python run_tests.py                 # Executar todos os testes
    python run_tests.py --verbose       # Executar com saída detalhada
    python run_tests.py --coverage      # Executar com relatório de cobertura
    python run_tests.py --help          # Mostrar ajuda
"""

import unittest
import sys
import os
import argparse
from io import StringIO

# Adicionar o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_all_tests(verbose=False, coverage=False):
    """
    Executa todos os testes e retorna os resultados
    
    Args:
        verbose (bool): Se True, mostra saída detalhada
        coverage (bool): Se True, gera relatório de cobertura
    
    Returns:
        tuple: (success, results_text)
    """
    
    if coverage:
        try:
            import coverage
            cov = coverage.Coverage()
            cov.start()
        except ImportError:
            print("⚠️  Módulo 'coverage' não encontrado. Instale com: pip install coverage")
            coverage = False
    
    # Descobrir todos os testes
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Configurar runner
    stream = StringIO()
    runner = unittest.TextTestRunner(
        stream=stream,
        verbosity=2 if verbose else 1,
        buffer=True
    )
    
    print("🧪 Executando testes da mppt24 AGI ABSOLUTA...")
    print("=" * 60)
    
    # Executar testes
    result = runner.run(suite)
    
    # Obter resultados
    output = stream.getvalue()
    
    if coverage:
        try:
            cov.stop()
            cov.save()
            
            print("\n📊 Relatório de Cobertura:")
            print("-" * 30)
            cov.report()
            
            # Gerar relatório HTML se possível
            try:
                cov.html_report(directory='htmlcov')
                print("📄 Relatório HTML gerado em: htmlcov/index.html")
            except:
                pass
                
        except:
            print("⚠️  Erro ao gerar relatório de cobertura")
    
    # Mostrar resumo
    print("\n📋 Resumo dos Testes:")
    print("=" * 30)
    print(f"✅ Testes executados: {result.testsRun}")
    print(f"❌ Falhas: {len(result.failures)}")
    print(f"🚫 Erros: {len(result.errors)}")
    print(f"⏭️  Ignorados: {len(result.skipped)}")
    
    success_rate = ((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100) if result.testsRun > 0 else 0
    print(f"📈 Taxa de sucesso: {success_rate:.1f}%")
    
    # Mostrar detalhes de falhas
    if result.failures:
        print("\n❌ FALHAS:")
        print("-" * 20)
        for test, traceback in result.failures:
            print(f"• {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\n🚫 ERROS:")
        print("-" * 20)
        for test, traceback in result.errors:
            print(f"• {test}: {traceback.split('Error:')[-1].strip()}")
    
    # Status final
    if result.wasSuccessful():
        print("\n🎉 TODOS OS TESTES PASSARAM! ✅")
        return True, output
    else:
        print(f"\n⚠️  {len(result.failures + result.errors)} TESTE(S) FALHARAM ❌")
        return False, output

def run_specific_test(test_name, verbose=False):
    """
    Executa um teste específico
    
    Args:
        test_name (str): Nome do teste (ex: test_knowledge.TestKnowledgeSystem.test_elementos_quimicos)
        verbose (bool): Se True, mostra saída detalhada
    """
    
    print(f"🧪 Executando teste específico: {test_name}")
    print("=" * 60)
    
    try:
        # Carregar teste específico
        suite = unittest.TestLoader().loadTestsFromName(f'tests.{test_name}')
        
        # Executar
        runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
        result = runner.run(suite)
        
        if result.wasSuccessful():
            print(f"\n✅ Teste '{test_name}' passou!")
        else:
            print(f"\n❌ Teste '{test_name}' falhou!")
            
    except Exception as e:
        print(f"❌ Erro ao executar teste '{test_name}': {e}")

def list_available_tests():
    """Lista todos os testes disponíveis"""
    
    print("📋 Testes Disponíveis:")
    print("=" * 30)
    
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    def extract_tests(test_suite):
        tests = []
        for test in test_suite:
            if isinstance(test, unittest.TestSuite):
                tests.extend(extract_tests(test))
            else:
                tests.append(test.id())
        return tests
    
    all_tests = extract_tests(suite)
    
    # Agrupar por módulo
    modules = {}
    for test in all_tests:
        module = test.split('.')[1]  # tests.test_knowledge.TestClass.test_method
        if module not in modules:
            modules[module] = []
        modules[module].append(test)
    
    for module, tests in modules.items():
        print(f"\n📁 {module}:")
        for test in tests:
            test_name = test.split('.')[-1]
            print(f"  • {test_name}")

def main():
    """Função principal"""
    
    parser = argparse.ArgumentParser(
        description='Executar testes da mppt24 AGI ABSOLUTA',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python run_tests.py                                    # Todos os testes
  python run_tests.py --verbose                          # Com saída detalhada
  python run_tests.py --coverage                         # Com cobertura
  python run_tests.py --test test_knowledge              # Teste específico
  python run_tests.py --list                             # Listar testes
        """
    )
    
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Saída detalhada dos testes')
    parser.add_argument('--coverage', '-c', action='store_true',
                       help='Gerar relatório de cobertura')
    parser.add_argument('--test', '-t', type=str,
                       help='Executar teste específico')
    parser.add_argument('--list', '-l', action='store_true',
                       help='Listar todos os testes disponíveis')
    
    args = parser.parse_args()
    
    if args.list:
        list_available_tests()
        return
    
    if args.test:
        run_specific_test(args.test, args.verbose)
        return
    
    # Executar todos os testes
    success, _ = run_all_tests(args.verbose, args.coverage)
    
    # Exit code baseado no resultado
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()

