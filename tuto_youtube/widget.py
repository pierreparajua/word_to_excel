from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QStatusBar, QPushButton, QMessageBox, QWidget, \
    QVBoxLayout, QListWidget, QAbstractItemView, QGridLayout, QGroupBox, QLineEdit, QLabel, QHBoxLayout, QRadioButton
from function import get_files_name, PATH_DOCUMENT_SOURCE
from function import main


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
        self.QL_project_name = QLabel('Non du projet:   ')
        self.QLE_project_name = QLineEdit()
        self.QL_client_name = QLabel('Non du client:    ')
        self.QLE_client_name = QLineEdit()
        self.QL_tech = QLabel('Technologie:      ')
        self.QLE_tech = QLineEdit()
        self.QL_phase = QLabel('Phase:                ')
        self.QLE_phase = QLineEdit()
        self.QL_doc_nbr = QLabel('Document Nb°: ')
        self.QLE_doc_nbr = QLineEdit()
        self.QL_revision = QLabel('Révision:            ')
        self.QLE_revision = QLineEdit()
        self.QL_issue_date = QLabel('Date de sortie:   ')
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
        header = QGroupBox()
        header_layout = QVBoxLayout()
        header_layout.addLayout(project_layout)
        header_layout.addLayout(client_layout)
        header_layout.addLayout(tech_layout)
        header_layout.addLayout(phase_layout)
        header_layout.addLayout(doc_nbr_layout)
        header_layout.addLayout(revision_layout)
        header_layout.addLayout(issue_date_layout)
        # Ajout de la V_layout au GroupBox
        header.setLayout(header_layout)
        # Création d'un layout englobant le GroupBox
        layout_gb_header = QVBoxLayout()
        layout_gb_header.addWidget(header)

        # _____________________________________version_layout_____________________________________
        #  Widget edition du contrôle de version
        self.ql_version = QLabel('Version:')
        self.qle_version = QLineEdit()
        self.ql_approved_date = QLabel("Date d'approbation:")
        self.qle_approved_date = QLineEdit()
        self.ql_approved_by = QLabel('Approuver par:')
        self.qle_approved_by = QLineEdit()
        self.ql_notes = QLabel('Notes:')
        self.qle_notes = QLineEdit()

        #  creation des layout du contrôle de version
        version_layout = QHBoxLayout()
        version_layout.addWidget(self.ql_version)
        version_layout.addWidget(self.qle_version)
        approved_date_layout = QHBoxLayout()
        approved_date_layout.addWidget(self.ql_approved_date)
        approved_date_layout.addWidget(self.qle_approved_date)
        approved_by_layout = QHBoxLayout()
        approved_by_layout.addWidget(self.ql_approved_by)
        approved_by_layout.addWidget(self.qle_approved_by)
        notes_layout = QHBoxLayout()
        notes_layout.addWidget(self.ql_notes)
        notes_layout.addWidget(self.qle_notes)

        # Ajout des H_layouts au V_layout
        version = QGroupBox()
        version_control_layout = QVBoxLayout()
        version_control_layout.addLayout(version_layout)
        version_control_layout.addLayout(approved_date_layout)
        version_control_layout.addLayout(approved_by_layout)
        version_control_layout.addLayout(notes_layout)
        # Ajout de la V_layout au GroupBox
        version.setLayout(version_control_layout)
        # Création d'un layout englobant le GroupBox
        layout_gb_version = QVBoxLayout()
        layout_gb_version.addWidget(version)

        # _____________________________________language_choice_layout_____________________________________
        #  Création des radios buttons
        qrb_french = QRadioButton("Francais")
        qrb_french.toggled.connect(self.selected_language)
        qrb_english = QRadioButton("Anglais")
        #  creation du layout contenant les boutons
        language_layout = QVBoxLayout()
        language_layout.addWidget(qrb_french)
        language_layout.addWidget(qrb_english)
        #  creation du GroupBox contenant le layout contenant les boutons
        language = QGroupBox()
        language.setLayout(language_layout)
        # création d'un layout contenant le GroupBox
        layout_gb_language = QVBoxLayout()
        layout_gb_language.addWidget(language)

        # _____________________________________format_choice_layout_____________________________________
        #  Création des radio-buttons
        qrb_word = QRadioButton("Word")
        qrb_word.setChecked(True)
        qrb_pdf = QRadioButton("PDF")
        #  creation du layout contenant les boutons
        format_layout = QVBoxLayout()
        format_layout.addWidget(qrb_word)
        format_layout.addWidget(qrb_pdf)
        #  creation du GroupBox contenant le layout contenant les boutons
        format = QGroupBox()
        format.setLayout(format_layout)
        # création d'un layout contenant le GroupBox
        layout_gb_format = QVBoxLayout()
        layout_gb_format.addWidget(format)

        # _____________________________________QPushButton__layout_____________________________________
        #  Création des QPushButton
        result_path = QPushButton('Répertoire de depot')
        create = QPushButton('Crée les documents')
        create.clicked.connect(self.create_template)
        #  creation du layout contenant les boutons
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(result_path)
        btn_layout.addWidget(create)

        # _____________________________________main_layout_____________________________________

        #  creation de la layout principale
        main_layout = QGridLayout()
        main_layout.addLayout(list_layout, 0, 0, 50, 20)
        main_layout.addLayout(layout_gb_header, 0, 21, 20, 10)
        main_layout.addLayout(layout_gb_version, 0, 42, 20, 10)
        main_layout.addLayout(layout_gb_language, 21, 21, 7, 10)
        main_layout.addLayout(layout_gb_format, 21, 42, 7, 10)
        main_layout.addLayout(btn_layout, 30, 21, 7, 10)

        self.setLayout(main_layout)

    def selected_language(self, checked):
        if checked:
            return "french"
        else:
            return "english"

    def create_template(self):
        main(self.selected_language(self))
