from Orange.widgets.widget import OWWidget, Input, Output
from Orange.widgets import gui
from Orange.data import Table, Domain, StringVariable
from PyQt5.QtWidgets import QMessageBox
import pandas as pd

class OWSalesforceQuery(OWWidget):
    name = "Salesforce Query"
    description = "Execute SOQL queries on Salesforce objects"
    icon = "icons/Salesforce.svg"
    category = "Salesforce"
    
    class Inputs:
        connection = Input("Connection", object)
    
    class Outputs:
        data = Output("Data", Table)
    
    def __init__(self):
        super().__init__()
        
        # Widget layout
        box = gui.widgetBox(self.controlArea, "Query Settings")
        
        # Object dropdown
        self.object_combo = gui.comboBox(box, self, "selected_object", "Object:")
        self.object_combo.addItems(["Contact", "Opportunity"])
        
        # SOQL query input
        self.query_input = gui.lineEdit(box, self, "soql_query", "SOQL Query:")
        self.query_input.setText("SELECT Id, Name FROM Contact LIMIT 5")
        
        # Execute button
        gui.button(box, self, "Execute Query", callback=self.execute_query)
        
        # Status label
        self.status_label = gui.label(box, self, "Status: Ready")
        
        # Store connection
        self.sf_connection = None
        
        # Update query when object changes
        self.object_combo.currentTextChanged.connect(self.update_query)
    
    def update_query(self):
        """Update the SOQL query when object selection changes"""
        selected = self.object_combo.currentText()
        if selected == "Contact":
            self.query_input.setText("SELECT Id, FirstName, LastName FROM Contact LIMIT 5")
        elif selected == "Opportunity":
            self.query_input.setText("SELECT Id, Name, Amount, StageName FROM Opportunity LIMIT 5")
    
    @Inputs.connection
    def set_connection(self, connection):
        """Receive Salesforce connection from input"""
        self.sf_connection = connection
        if connection:
            self.status_label.setText("Status: Connected")
        else:
            self.status_label.setText("Status: No connection")
    
    def execute_query(self):
        """Execute the SOQL query and output results"""
        if not self.sf_connection:
            QMessageBox.warning(self, "No Connection", "Please connect to Salesforce first")
            return
        
        try:
            self.status_label.setText("Status: Executing query...")
            
            # Execute SOQL query
            results = self.sf_connection.query(self.query_input.text())
            
            if results['totalSize'] == 0:
                QMessageBox.information(self, "No Results", "Query returned no results")
                self.status_label.setText("Status: No results")
                return
            
            # Convert to pandas DataFrame
            records = results['records']
            df = pd.DataFrame(records)
            
            # Remove Salesforce metadata columns
            if 'attributes' in df.columns:
                df = df.drop('attributes', axis=1)
            
            # Create Orange3 Table
            domain = Domain([StringVariable(col) for col in df.columns])
            table = Table.from_list(domain, df.values.tolist())
            
            # Send to output
            self.Outputs.data.send(table)
            
            self.status_label.setText(f"Status: Retrieved {len(df)} records")
            
        except Exception as e:
            QMessageBox.critical(self, "Query Error", f"Failed to execute query: {str(e)}")
            self.status_label.setText("Status: Query failed")
