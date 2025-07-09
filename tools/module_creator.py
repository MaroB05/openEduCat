import sys
import os
import json
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QTextEdit, 
                             QCheckBox, QComboBox, QPushButton, QTabWidget,
                             QScrollArea, QGroupBox, QFormLayout, QListWidget,
                             QSplitter, QTreeWidget, QTreeWidgetItem, QMessageBox,
                             QFileDialog, QSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import textwrap

class OdooModuleGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Odoo Module Generator")
        self.setGeometry(100, 100, 1200, 800)
        
        # Initialize module data
        self.module_data = {}
        self.modules_path = ""
        
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Tab widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)
        
        # Create tabs
        self.create_new_module_tab()
        self.create_edit_module_tab()
        
    def create_new_module_tab(self):
        """Create the new module creation tab"""
        tab = QWidget()
        self.tab_widget.addTab(tab, "Create New Module")
        
        layout = QVBoxLayout(tab)
        
        # Modules path selection
        path_layout = QHBoxLayout()
        path_layout.addWidget(QLabel("Modules Path:"))
        self.path_input = QLineEdit()
        self.path_input.setPlaceholderText("Select or enter path to your Odoo modules directory")
        path_layout.addWidget(self.path_input)
        
        browse_btn = QPushButton("Browse")
        browse_btn.clicked.connect(self.browse_modules_path)
        path_layout.addWidget(browse_btn)
        
        layout.addLayout(path_layout)
        
        # Scroll area for form
        scroll = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        
        # Required fields group
        required_group = QGroupBox("Required Fields")
        required_layout = QFormLayout(required_group)
        
        self.module_name = QLineEdit()
        self.module_name.setPlaceholderText("technical_name (no spaces, lowercase)")
        required_layout.addRow("Module Name*:", self.module_name)
        
        self.display_name = QLineEdit()
        self.display_name.setPlaceholderText("Display Name")
        required_layout.addRow("Display Name*:", self.display_name)
        
        self.version = QLineEdit("1.0.0")
        required_layout.addRow("Version*:", self.version)
        
        self.depends = QLineEdit("base")
        self.depends.setPlaceholderText("base,sale,purchase (comma separated)")
        required_layout.addRow("Dependencies*:", self.depends)
        
        scroll_layout.addWidget(required_group)
        
        # Optional fields group
        optional_group = QGroupBox("Optional Fields")
        optional_layout = QFormLayout(optional_group)
        
        self.summary = QLineEdit()
        self.summary.setPlaceholderText("Brief description")
        optional_layout.addRow("Summary:", self.summary)
        
        self.description = QTextEdit()
        self.description.setMaximumHeight(100)
        self.description.setPlaceholderText("Detailed description")
        optional_layout.addRow("Description:", self.description)
        
        self.author = QLineEdit()
        self.author.setPlaceholderText("Your Name")
        optional_layout.addRow("Author:", self.author)
        
        self.website = QLineEdit()
        self.website.setPlaceholderText("https://yourwebsite.com")
        optional_layout.addRow("Website:", self.website)
        
        self.category = QComboBox()
        self.category.addItems([
            "Uncategorized", "Accounting", "Administration", "CRM", "Document Management",
            "eCommerce", "Human Resources", "Inventory", "Manufacturing", "Marketing",
            "Point of Sale", "Project", "Purchases", "Sales", "Warehouse", "Website"
        ])
        optional_layout.addRow("Category:", self.category)
        
        self.license = QComboBox()
        self.license.addItems(["LGPL-3", "GPL-3", "MIT", "Apache-2.0", "Other/Proprietary/Open Source"])
        optional_layout.addRow("License:", self.license)
        
        self.installable = QCheckBox()
        self.installable.setChecked(True)
        optional_layout.addRow("Installable:", self.installable)
        
        self.auto_install = QCheckBox()
        optional_layout.addRow("Auto Install:", self.auto_install)
        
        self.application = QCheckBox()
        optional_layout.addRow("Application:", self.application)
        
        scroll_layout.addWidget(optional_group)
        
        # Module structure options
        structure_group = QGroupBox("Module Structure")
        structure_layout = QVBoxLayout(structure_group)
        
        self.create_models = QCheckBox("Create models folder")
        self.create_views = QCheckBox("Create views folder")
        self.create_controllers = QCheckBox("Create controllers folder")
        self.create_data = QCheckBox("Create data folder")
        self.create_static = QCheckBox("Create static folder")
        self.create_security = QCheckBox("Create security folder")
        self.create_wizard = QCheckBox("Create wizard folder")
        self.create_reports = QCheckBox("Create reports folder")
        
        structure_layout.addWidget(self.create_models)
        structure_layout.addWidget(self.create_views)
        structure_layout.addWidget(self.create_controllers)
        structure_layout.addWidget(self.create_data)
        structure_layout.addWidget(self.create_static)
        structure_layout.addWidget(self.create_security)
        structure_layout.addWidget(self.create_wizard)
        structure_layout.addWidget(self.create_reports)
        
        scroll_layout.addWidget(structure_group)
        
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)
        
        # Create button
        create_btn = QPushButton("Create Module")
        create_btn.clicked.connect(self.create_module)
        create_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; padding: 10px; }")
        layout.addWidget(create_btn)
        
    def create_edit_module_tab(self):
        """Create the edit module tab"""
        tab = QWidget()
        self.tab_widget.addTab(tab, "Edit Existing Module")
        
        layout = QHBoxLayout(tab)
        
        # Left panel - Module list
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        left_layout.addWidget(QLabel("Existing Modules:"))
        
        # Path selection for editing
        edit_path_layout = QHBoxLayout()
        self.edit_path_input = QLineEdit()
        self.edit_path_input.setPlaceholderText("Select modules directory")
        edit_path_layout.addWidget(self.edit_path_input)
        
        edit_browse_btn = QPushButton("Browse")
        edit_browse_btn.clicked.connect(self.browse_edit_path)
        edit_path_layout.addWidget(edit_browse_btn)
        
        left_layout.addLayout(edit_path_layout)
        
        # Module list
        self.module_list = QListWidget()
        self.module_list.itemClicked.connect(self.load_module_for_edit)
        left_layout.addWidget(self.module_list)
        
        refresh_btn = QPushButton("Refresh List")
        refresh_btn.clicked.connect(self.refresh_module_list)
        left_layout.addWidget(refresh_btn)
        
        left_panel.setMaximumWidth(300)
        layout.addWidget(left_panel)
        
        # Right panel - Module editor
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Module info display
        self.module_info_label = QLabel("Select a module to edit")
        self.module_info_label.setFont(QFont("Arial", 12, QFont.Bold))
        right_layout.addWidget(self.module_info_label)
        
        # File tree and editor
        splitter = QSplitter(Qt.Horizontal)
        
        # File tree
        self.file_tree = QTreeWidget()
        self.file_tree.setHeaderLabel("Files")
        self.file_tree.itemClicked.connect(self.load_file_content)
        splitter.addWidget(self.file_tree)
        
        # File editor
        self.file_editor = QTextEdit()
        self.file_editor.setPlaceholderText("Select a file to edit")
        splitter.addWidget(self.file_editor)
        
        right_layout.addWidget(splitter)
        
        # Save button
        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.save_file_changes)
        save_btn.setStyleSheet("QPushButton { background-color: #2196F3; color: white; padding: 10px; }")
        right_layout.addWidget(save_btn)
        
        layout.addWidget(right_panel)
        
        # Store current file path
        self.current_file_path = None
        
    def browse_modules_path(self):
        """Browse for modules directory"""
        path = QFileDialog.getExistingDirectory(self, "Select Modules Directory")
        if path:
            self.path_input.setText(path)
            self.modules_path = path
            
    def browse_edit_path(self):
        """Browse for modules directory for editing"""
        path = QFileDialog.getExistingDirectory(self, "Select Modules Directory")
        if path:
            self.edit_path_input.setText(path)
            self.refresh_module_list()
            
    def refresh_module_list(self):
        """Refresh the list of existing modules"""
        self.module_list.clear()
        path = self.edit_path_input.text()
        if not path or not os.path.exists(path):
            return
            
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "__manifest__.py")):
                self.module_list.addItem(item)
                
    def create_module(self):
        """Create a new Odoo module"""
        if not self.validate_required_fields():
            return
            
        module_name = self.module_name.text().strip()
        modules_path = self.path_input.text().strip()
        
        if not modules_path:
            QMessageBox.warning(self, "Error", "Please select a modules directory")
            return
            
        module_path = os.path.join(modules_path, module_name)
        
        if os.path.exists(module_path):
            QMessageBox.warning(self, "Error", f"Module '{module_name}' already exists")
            return
            
        try:
            # Create module directory
            os.makedirs(module_path)
            
            # Create __init__.py
            self.create_init_file(module_path)
            
            # Create __manifest__.py
            self.create_manifest_file(module_path)
            
            # Create optional folders
            self.create_optional_folders(module_path)
            
            QMessageBox.information(self, "Success", f"Module '{module_name}' created successfully!")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create module: {str(e)}")
            
    def validate_required_fields(self):
        """Validate required fields"""
        if not self.module_name.text().strip():
            QMessageBox.warning(self, "Error", "Module name is required")
            return False
            
        if not self.display_name.text().strip():
            QMessageBox.warning(self, "Error", "Display name is required")
            return False
            
        if not self.version.text().strip():
            QMessageBox.warning(self, "Error", "Version is required")
            return False
            
        if not self.depends.text().strip():
            QMessageBox.warning(self, "Error", "Dependencies are required")
            return False
            
        return True
        
    def create_init_file(self, module_path):
        """Create __init__.py file"""
        init_content = "# -*- coding: utf-8 -*-\n"
        
        if self.create_models.isChecked():
            init_content += "from . import models\n"
        if self.create_controllers.isChecked():
            init_content += "from . import controllers\n"
        if self.create_wizard.isChecked():
            init_content += "from . import wizard\n"
            
        with open(os.path.join(module_path, "__init__.py"), "w") as f:
            f.write(init_content)
            
    def create_manifest_file(self, module_path):
        """Create __manifest__.py file"""
        manifest = {
            'name': self.display_name.text().strip(),
            'version': self.version.text().strip(),
            'depends': [dep.strip() for dep in self.depends.text().split(',') if dep.strip()],
            'data': [],
            'installable': self.installable.isChecked(),
        }
        
        # Add optional fields
        if self.summary.text().strip():
            manifest['summary'] = self.summary.text().strip()
            
        if self.description.toPlainText().strip():
            manifest['description'] = self.description.toPlainText().strip()
            
        if self.author.text().strip():
            manifest['author'] = self.author.text().strip()
            
        if self.website.text().strip():
            manifest['website'] = self.website.text().strip()
            
        if self.category.currentText() != "Uncategorized":
            manifest['category'] = self.category.currentText()
            
        if self.license.currentText():
            manifest['license'] = self.license.currentText()
            
        if self.auto_install.isChecked():
            manifest['auto_install'] = True
            
        if self.application.isChecked():
            manifest['application'] = True
            
        # Add data files based on created folders
        data_files = []
        if self.create_security.isChecked():
            data_files.append('security/ir.model.access.csv')
        if self.create_views.isChecked():
            data_files.append('views/views.xml')
        if self.create_data.isChecked():
            data_files.append('data/data.xml')
            
        if data_files:
            manifest['data'] = data_files
            
        # Write manifest file
        with open(os.path.join(module_path, "__manifest__.py"), "w") as f:
            f.write("# -*- coding: utf-8 -*-\n")
            f.write(f"{manifest}")
            
    def create_optional_folders(self, module_path):
        """Create optional folders and basic files"""
        if self.create_models.isChecked():
            models_path = os.path.join(module_path, "models")
            os.makedirs(models_path)
            with open(os.path.join(models_path, "__init__.py"), "w") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                
        if self.create_views.isChecked():
            views_path = os.path.join(module_path, "views")
            os.makedirs(views_path)
            with open(os.path.join(views_path, "views.xml"), "w") as f:
                f.write("""<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Add your views here -->
</odoo>""")
                
        if self.create_controllers.isChecked():
            controllers_path = os.path.join(module_path, "controllers")
            os.makedirs(controllers_path)
            with open(os.path.join(controllers_path, "__init__.py"), "w") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                
        if self.create_data.isChecked():
            data_path = os.path.join(module_path, "data")
            os.makedirs(data_path)
            with open(os.path.join(data_path, "data.xml"), "w") as f:
                f.write("""<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Add your data here -->
</odoo>""")
                
        if self.create_static.isChecked():
            static_path = os.path.join(module_path, "static")
            os.makedirs(static_path)
            os.makedirs(os.path.join(static_path, "src"))
            os.makedirs(os.path.join(static_path, "src", "css"))
            os.makedirs(os.path.join(static_path, "src", "js"))
            
        if self.create_security.isChecked():
            security_path = os.path.join(module_path, "security")
            os.makedirs(security_path)
            with open(os.path.join(security_path, "ir.model.access.csv"), "w") as f:
                f.write("id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n")
                
        if self.create_wizard.isChecked():
            wizard_path = os.path.join(module_path, "wizard")
            os.makedirs(wizard_path)
            with open(os.path.join(wizard_path, "__init__.py"), "w") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                
        if self.create_reports.isChecked():
            reports_path = os.path.join(module_path, "reports")
            os.makedirs(reports_path)
            with open(os.path.join(reports_path, "__init__.py"), "w") as f:
                f.write("# -*- coding: utf-8 -*-\n")
                
    def load_module_for_edit(self, item):
        """Load a module for editing"""
        module_name = item.text()
        modules_path = self.edit_path_input.text()
        module_path = os.path.join(modules_path, module_name)
        
        self.module_info_label.setText(f"Editing Module: {module_name}")
        
        # Load file tree
        self.file_tree.clear()
        self.load_file_tree(module_path, self.file_tree)
        
    def load_file_tree(self, path, parent):
        """Load file tree structure"""
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            tree_item = QTreeWidgetItem(parent, [item])
            tree_item.setData(0, Qt.UserRole, item_path)
            
            if os.path.isdir(item_path):
                self.load_file_tree(item_path, tree_item)
                
    def load_file_content(self, item):
        """Load file content for editing"""
        file_path = item.data(0, Qt.UserRole)
        
        if os.path.isfile(file_path):
            self.current_file_path = file_path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.file_editor.setPlainText(content)
            except Exception as e:
                self.file_editor.setPlainText(f"Error reading file: {str(e)}")
                
    def save_file_changes(self):
        """Save changes to the current file"""
        if not self.current_file_path:
            QMessageBox.warning(self, "Error", "No file selected")
            return
            
        try:
            with open(self.current_file_path, 'w', encoding='utf-8') as f:
                f.write(self.file_editor.toPlainText())
            QMessageBox.information(self, "Success", "File saved successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file: {str(e)}")

def main():
    app = QApplication(sys.argv)
    generator = OdooModuleGenerator()
    generator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
