#!/usr/bin/env python3
"""
AI Business Process Optimizer - Module Testing Script
Tests the module structure and validates key components
"""

import os
import ast
import xml.etree.ElementTree as ET
import json

def test_module_structure():
    """Test if all required files exist"""
    base_path = "extra-addons/ai_business_optimizer"
    
    required_files = [
        "__manifest__.py",
        "__init__.py",
        "models/__init__.py",
        "models/process_analysis.py",
        "models/optimization_recommendation.py", 
        "models/process_monitor.py",
        "models/optimization_engine.py",
        "models/kpi_tracker.py",
        "controllers/__init__.py",
        "controllers/main.py",
        "wizards/__init__.py",
        "wizards/process_optimizer_wizard.py",
        "views/process_analysis_views.xml",
        "views/optimization_recommendation_views.xml",
        "views/process_monitor_views.xml",
        "views/dashboard_views.xml",
        "views/menu_views.xml",
        "wizards/process_optimizer_wizard_views.xml",
        "reports/optimization_report_views.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "data/process_templates.xml",
        "data/optimization_rules.xml",
        "data/demo_data.xml",
        "static/src/js/dashboard.js",
        "static/src/css/dashboard.css",
        "static/description/index.html",
        "static/description/icon.png"
    ]
    
    missing_files = []
    existing_files = []
    
    for file_path in required_files:
        full_path = os.path.join(base_path, file_path)
        if os.path.exists(full_path):
            existing_files.append(file_path)
        else:
            missing_files.append(file_path)
    
    print(f"✅ Module Structure Test")
    print(f"   Existing files: {len(existing_files)}/{len(required_files)}")
    print(f"   Missing files: {len(missing_files)}")
    
    if missing_files:
        print("   Missing files:")
        for file in missing_files[:5]:  # Show first 5
            print(f"     - {file}")
        if len(missing_files) > 5:
            print(f"     ... and {len(missing_files) - 5} more")
    
    return len(missing_files) == 0

def test_python_syntax():
    """Test Python file syntax"""
    base_path = "extra-addons/ai_business_optimizer"
    python_files = []
    
    # Find all Python files
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    syntax_errors = []
    
    for file_path in python_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
        except SyntaxError as e:
            syntax_errors.append(f"{file_path}: {e}")
        except Exception as e:
            syntax_errors.append(f"{file_path}: {e}")
    
    print(f"✅ Python Syntax Test")
    print(f"   Files checked: {len(python_files)}")
    print(f"   Syntax errors: {len(syntax_errors)}")
    
    if syntax_errors:
        print("   Errors:")
        for error in syntax_errors[:3]:  # Show first 3
            print(f"     - {error}")
    
    return len(syntax_errors) == 0

def test_xml_validity():
    """Test XML file validity"""
    base_path = "extra-addons/ai_business_optimizer"
    xml_files = []
    
    # Find all XML files
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.xml'):
                xml_files.append(os.path.join(root, file))
    
    xml_errors = []
    
    for file_path in xml_files:
        try:
            ET.parse(file_path)
        except ET.ParseError as e:
            xml_errors.append(f"{file_path}: {e}")
        except Exception as e:
            xml_errors.append(f"{file_path}: {e}")
    
    print(f"✅ XML Validity Test")
    print(f"   Files checked: {len(xml_files)}")
    print(f"   XML errors: {len(xml_errors)}")
    
    if xml_errors:
        print("   Errors:")
        for error in xml_errors[:3]:  # Show first 3
            print(f"     - {error}")
    
    return len(xml_errors) == 0

def test_manifest():
    """Test manifest file"""
    manifest_path = "extra-addons/ai_business_optimizer/__manifest__.py"
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse as Python to check syntax
        manifest_dict = ast.literal_eval(content)
        
        required_keys = ['name', 'version', 'depends', 'data', 'installable']
        missing_keys = [key for key in required_keys if key not in manifest_dict]
        
        print(f"✅ Manifest Test")
        print(f"   Required keys present: {len(required_keys) - len(missing_keys)}/{len(required_keys)}")
        
        if missing_keys:
            print(f"   Missing keys: {missing_keys}")
        
        # Check dependencies
        depends = manifest_dict.get('depends', [])
        print(f"   Dependencies: {len(depends)}")
        
        # Check data files
        data_files = manifest_dict.get('data', [])
        print(f"   Data files declared: {len(data_files)}")
        
        return len(missing_keys) == 0
        
    except Exception as e:
        print(f"❌ Manifest Test Failed: {e}")
        return False

def test_model_structure():
    """Test model structure"""
    models_path = "extra-addons/ai_business_optimizer/models"
    
    expected_models = [
        'ai.process.analysis',
        'ai.optimization.recommendation', 
        'ai.process.monitor',
        'ai.optimization.engine',
        'ai.kpi.tracker'
    ]
    
    found_models = []
    
    for model_file in os.listdir(models_path):
        if model_file.endswith('.py') and model_file != '__init__.py':
            file_path = os.path.join(models_path, model_file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Look for _name definitions
                for line in content.split('\n'):
                    if '_name =' in line and 'ai.' in line:
                        # Extract model name
                        start = line.find("'") + 1
                        end = line.find("'", start)
                        if start > 0 and end > start:
                            model_name = line[start:end]
                            found_models.append(model_name)
            except Exception as e:
                print(f"Error reading {model_file}: {e}")
    
    print(f"✅ Model Structure Test")
    print(f"   Expected models: {len(expected_models)}")
    print(f"   Found models: {len(found_models)}")
    
    missing_models = [m for m in expected_models if m not in found_models]
    if missing_models:
        print(f"   Missing models: {missing_models}")
    
    return len(missing_models) == 0

def run_all_tests():
    """Run all tests"""
    print("🤖 AI Business Process Optimizer - Module Test Suite")
    print("=" * 60)
    
    tests = [
        ("Module Structure", test_module_structure),
        ("Python Syntax", test_python_syntax), 
        ("XML Validity", test_xml_validity),
        ("Manifest File", test_manifest),
        ("Model Structure", test_model_structure)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} Test...")
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"   Result: {status}")
        except Exception as e:
            print(f"   Result: ❌ ERROR - {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📊 Test Summary:")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅" if result else "❌"
        print(f"   {status} {test_name}")
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Module is ready for installation.")
        return True
    else:
        print("⚠️  Some tests failed. Review and fix issues before installation.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)