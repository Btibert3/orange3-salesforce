from Orange.widgets.widget import OWWidget, Output
from Orange.widgets import gui
from Orange.data import Table
from PyQt5.QtWidgets import QMessageBox
from simple_salesforce import Salesforce
import json

class OWSalesforceAuth(OWWidget):
    name = "Salesforce Authentication"
    description = "Connect to Salesforce org"
    icon = "icons/Salesforce.svg"
    category = "Salesforce"
    
    class Outputs:
        connection = Output("Connection", object)
    
    def __init__(self):
        super().__init__()
        
        # Widget layout
        box = gui.widgetBox(self.controlArea, "Salesforce Connection")
        
        # Username input
        self.username = gui.lineEdit(box, self, "username", "Username:")
        
        # Password input
        self.password = gui.lineEdit(box, self, "password", "Password:")
        self.password.setEchoMode(gui.lineEdit.Password)
        
        # Security token input
        self.token = gui.lineEdit(box, self, "token", "Security Token:")
        self.token.setEchoMode(gui.lineEdit.Password)
        
        # Test connection button
        gui.button(box, self, "Test Connection", callback=self.test_connection)
        
        # Connect button
        gui.button(box, self, "Connect", callback=self.connect)
        
        # Status label
        self.status_label = gui.label(box, self, "Status: Not connected")
        
        # Store connection
        self.sf_connection = None
        
    def test_connection(self):
        """Test the Salesforce connection"""
        try:
            sf = Salesforce(
                username=self.username.text(),
                password=self.password.text(),
                security_token=self.token.text()
            )
            
            # Test by getting org info
            org_info = sf.describe()
            org_name = org_info['name']
            
            QMessageBox.information(
                self, 
                "Connection Successful", 
                f"Connected to Salesforce org: {org_name}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Connection Failed", 
                f"Failed to connect: {str(e)}"
            )
    
    def connect(self):
        """Establish connection and send to output"""
        try:
            self.sf_connection = Salesforce(
                username=self.username.text(),
                password=self.password.text(),
                security_token=self.token.text()
            )
            
            # Test connection
            org_info = self.sf_connection.describe()
            org_name = org_info['name']
            
            self.status_label.setText(f"Status: Connected to {org_name}")
            
            # Send connection to output
            self.Outputs.connection.send(self.sf_connection)
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                "Connection Failed", 
                f"Failed to connect: {str(e)}"
            )
            self.status_label.setText("Status: Connection failed")
