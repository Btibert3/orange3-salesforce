#!/usr/bin/env python3
"""
Test script for the Salesforce Authentication widget UI
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from orangecontrib.salesforce.widgets.owsfdcauth import OWSalesforceAuth

def test_widget_ui():
    """Test the widget UI in a proper Qt application context"""
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Create main window
    window = QMainWindow()
    window.setWindowTitle("Salesforce Auth Widget Test")
    window.setGeometry(100, 100, 800, 600)
    
    # Create central widget and layout
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    layout = QVBoxLayout(central_widget)
    
    try:
        # Create and test the Salesforce Auth widget
        print("Creating Salesforce Auth widget...")
        auth_widget = OWSalesforceAuth()
        
        # Check if all attributes exist
        print(f"✅ auth_method attribute exists: {hasattr(auth_widget, 'auth_method')}")
        print(f"✅ username attribute exists: {hasattr(auth_widget, 'username')}")
        print(f"✅ password attribute exists: {hasattr(auth_widget, 'password')}")
        print(f"✅ domain attribute exists: {hasattr(auth_widget, 'domain')}")
        print(f"✅ instance_url attribute exists: {hasattr(auth_widget, 'instance_url')}")
        print(f"✅ access_token attribute exists: {hasattr(auth_widget, 'access_token')}")
        print(f"✅ security_token attribute exists: {hasattr(auth_widget, 'security_token')}")
        
        # Add widget to layout
        layout.addWidget(auth_widget)
        
        print("✅ Widget created and added to UI successfully!")
        print("✅ No AttributeError for auth_method")
        print("✅ No AttributeError for groupBox/widgetBox")
        
        # Show the window
        window.show()
        
        # Run the application
        print("Starting Qt application... Press Ctrl+C to exit")
        sys.exit(app.exec_())
        
    except Exception as e:
        print(f"❌ Error testing widget: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    test_widget_ui()
