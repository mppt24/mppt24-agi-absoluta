#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pacote de testes para mppt24 AGI ABSOLUTA

Este pacote contém todos os testes automatizados para verificar
o funcionamento correto da Inteligência Artificial Geral.

Módulos de teste:
- test_knowledge.py: Testes do sistema de conhecimento universal
- test_advanced_features.py: Testes das funcionalidades avançadas
- test_integration.py: Testes de integração do sistema completo
"""

__version__ = "1.3.0"
__author__ = "mppt24"
__email__ = "mppt24@gmail.com"

# Importar classes de teste principais para facilitar importação
from .test_knowledge import TestKnowledgeSystem
from .test_advanced_features import TestAdvancedFeatures
from .test_integration import TestIntegration

__all__ = [
    'TestKnowledgeSystem',
    'TestAdvancedFeatures', 
    'TestIntegration'
]

