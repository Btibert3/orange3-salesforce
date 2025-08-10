#!/usr/bin/env python3
"""
Basic test script to verify the module structure is correct.
"""

def test_module_structure():
    """Test that the basic module structure is correct."""
    try:
        # Test basic imports
        import orangecontrib
        print("✓ orangecontrib package found")
        
        import orangecontrib.salesforce
        print("✓ orangecontrib.salesforce package found")
        
        import orangecontrib.salesforce.widgets
        print("✓ orangecontrib.salesforce.widgets package found")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_file_imports():
    """Test that individual widget files can be imported."""
    try:
        # Test widget imports (without instantiating)
        from orangecontrib.salesforce.widgets.owsfdcauth import OWSalesforceAuth
        print("✓ OWSalesforceAuth class imported")
        
        from orangecontrib.salesforce.widgets.owsfcontacts import OWSalesforceContacts
        print("✓ OWSalesforceContacts class imported")
        
        return True
    except ImportError as e:
        print(f"✗ Widget import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("Testing basic module structure...")
    print("-" * 40)
    
    structure_ok = test_module_structure()
    if structure_ok:
        imports_ok = test_file_imports()
        if imports_ok:
            print("\n🎉 Basic structure test passed!")
        else:
            print("\n❌ Widget imports failed.")
    else:
        print("\n❌ Module structure test failed.")
