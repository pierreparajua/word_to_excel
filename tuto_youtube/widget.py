from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton, QMessageBox, QWidget, \
    QVBoxLayout, QListWidget, QAbstractItemView, QGridLayout, QGroupBox, QLineEdit, QLabel, QHBoxLayout
from excel_to_word import get_files_name, PATH_DOCUMENT_SOURCE


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Excel_to_word  SKYRAY")
        self.resize(1600, 900)

        # _____________________________________list_layout_____________________________________
        #  Widget liste de selection des fichiers
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItems(get_files_name(PATH_DOCUMENT_SOURCE))

        #  creation du layout pour la selection des fichiers
        list_layout = QVBoxLayout()
        list_layout.addWidget(self.list_widget)

        # _____________________________________header_layout_____________________________________
        #  Widget edition du header
        self.QL_project_name = QLabel('Non du projet:')
        self.QLE_project_name = QLineEdit()
        self.QL_client_name = QLabel('Non du client:')
        self.QLE_client_name = QLineEdit()
        self.QL_tech = QLabel('Technologie:')
        self.QLE_tech = QLineEdit()
        self.QL_phase = QLabel('Phase:')
        self.QLE_phase = QLineEdit()
        self.QL_doc_nbr = QLabel('Document Nb°:')
        self.QLE_doc_nbr = QLineEdit()
        self.QL_revision = QLabel('Révision:')
        self.QLE_revision = QLineEdit()
        self.QL_issue_date = QLabel('Date de sortie:')
        self.QLE_issue_date = QLineEdit()

        #  creation des layout pour éditer le header
        project_layout = QHBoxLayout()
        project_layout.addWidget(self.QL_project_name)
        project_layout.addWidget(self.QLE_project_name)
        client_layout = QHBoxLayout()
        client_layout.addWidget(self.QL_client_name)
        client_layout.addWidget(self.QLE_client_name)
        tech_layout = QHBoxLayout()
        tech_layout.addWidget(self.QL_tech)
        tech_layout.addWidget(self.QLE_tech)
        phase_layout = QHBoxLayout()
        phase_layout.addWidget(self.QL_phase)
        phase_layout.addWidget(self.QLE_phase)
        doc_nbr_layout = QHBoxLayout()
        doc_nbr_layout.addWidget(self.QL_doc_nbr)
        doc_nbr_layout.addWidget(self.QLE_doc_nbr)
        revision_layout = QHBoxLayout()
        revision_layout.addWidget(self.QL_revision)
        revision_layout.addWidget(self.QLE_revision)
        issue_date_layout = QHBoxLayout()
        issue_date_layout.addWidget(self.QL_issue_date)
        issue_date_layout.addWidget(self.QLE_issue_date)

        # Ajout des H_layouts au V_layout
        header_layout = QVBoxLayout()
        header_layout.addLayout(project_layout)
        header_layout.addLayout(client_layout)
        header_layout.addLayout(tech_layout)
        header_layout.addLayout(phase_layout)
        header_layout.addLayout(doc_nbr_layout)
        header_layout.addLayout(revision_layout)
        header_layout.addLayout(issue_date_layout)

        # _____________________________________version_layout_____________________________________
        #  Widget edition du contrôle de version
        self.QL_version = QLabel('Version:')
        self.QLE_version = QLineEdit()
        self.QL_approved_date = QLabel("Date d'approbation:")
        self.QLE_approved_date = QLineEdit()
        self.QL_approved_by = QLabel('Approuver par:')
        self.QLE_approved_by = QLineEdit()
        self.QL_notes = QLabel('Notes:')
        self.QLE_notes = QLineEdit()

        #  creation des layout du contrôle de version
        version_layout = QHBoxLayout()
        version_layout.addWidget(self.QL_version)
        version_layout.addWidget(self.QLE_version)
        approved_date_layout = QHBoxLayout()
        approved_date_layout.addWidget(self.QL_approved_date)
        approved_date_layout.addWidget(self.QLE_approved_date)
        approved_by_layout = QHBoxLayout()
        approved_by_layout.addWidget(self.QL_approved_by)
        approved_by_layout.addWidget(self.QLE_approved_by)
        notes_layout = QHBoxLayout()
        notes_layout.addWidget(self.QL_notes)
        notes_layout.addWidget(self.QLE_notes)

        # Ajout des H_layouts au V_layout
        version_control_layout = QVBoxLayout()
        version_control_layout.addLayout(version_layout)
        version_control_layout.addLayout(approved_date_layout)
        version_control_layout.addLayout(approved_by_layout)
        version_control_layout.addLayout(notes_layout)

        # _____________________________________main_layout_____________________________________

        #  creation de la layout principale
        main_layout = QGridLayout()
        main_layout.addLayout(list_layout, 0, 0, 50, 20)
        main_layout.addLayout(header_layout, 0, 21, 20, 10)
        main_layout.addLayout(version_control_layout, 0, 42, 20, 10)

        self.setLayout(main_layout)

