#!/usr/bin/env python3
"""
Simple test script to verify the Salesforce widgets can be imported.
"""

def test_imports():
    """Test that all required modules can be imported."""
    try:
        from orangecontrib.salesforce.widgets import OWSalesforceAuth, OWSalesforceContacts
        print("✓ Successfully imported Salesforce widgets")
        return True
    except ImportError as e:
        print(f"✗ Failed to import Salesforce widgets: {e}")
        return False

def test_widget_creation():
    """Test that widgets can be instantiated (without GUI)."""
    try:
        from orangecontrib.salesforce.widgets import OWSalesforceAuth, OWSalesforceContacts
        
        # Test auth widget
        auth_widget = OWSalesforceAuth()
        print("✓ Successfully created OWSalesforceAuth widget")
        
        # Test contacts widget
        contacts_widget = OWSalesforceContacts()
        print("✓ Successfully created OWSalesforceContacts widget")
        
        return True
    except Exception as e:
        print(f"✗ Failed to create widgets: {e}")
        return False

if __name__ == "__main__":
    print("Testing Salesforce widgets...")
    print("-" * 40)
    
    import_success = test_imports()
    if import_success:
        widget_success = test_widget_creation()
        if widget_success:
            print("\n🎉 All tests passed! Widgets are ready to use.")
        else:
            print("\n❌ Widget creation failed.")
    else:
        print("\n❌ Import failed.")
