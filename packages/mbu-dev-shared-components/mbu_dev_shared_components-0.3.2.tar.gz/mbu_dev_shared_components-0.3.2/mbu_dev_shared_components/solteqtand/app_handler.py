"""
This module contains the SolteqTandApp class, which
automates interactions with the SolteqTand application
using the UIAutomation library.
"""
import os
import time
import uiautomation as auto


class ManualProcessingRequiredError(Exception):
    """
    Custom exception raised when the patient cannot be opened due incorrect SSN.
    """
    def __init__(self, message="Error occurred while opening the patient. There is no patient with the provided CPR number."):
        super().__init__(message)


class SolteqTandApp:
    """
    A class to automate interactions with the SolteqTand application.
    """
    def __init__(self, app_path, username, password):
        """
        Initializes the SolteqTandApp object.

        Args:
            app_path (str): Path to the application.
            username (str): Username for login.
            password (str): Password for login.
            ssn (str): SSN for lookup.
        """
        self.app_path = app_path
        self.username = username
        self.password = password
        self.app_window = None

    def find_element_by_property(self, control, control_type=None, automation_id=None, name=None, class_name=None) -> auto.Control:
        """
        Uses GetChildren to traverse through controls and find an element based on the specified properties.

        Args:
            control (Control): The root control to search from (e.g., main window or pane).
            control_type (ControlType, optional): ControlType to search for.
            automation_id (str, optional): AutomationId of the target element.
            name (str, optional): Name of the target element.
            class_name (str, optional): ClassName of the target element.

        Returns:
            Control: The found element or None if no match is found.
        """
        children = control.GetChildren()

        for child in children:
            if (control_type is None or child.ControlType == control_type) and \
               (automation_id is None or child.AutomationId == automation_id) and \
               (name is None or child.Name == name) and \
               (class_name is None or child.ClassName == class_name):
                return child

            found = self.find_element_by_property(child, control_type, automation_id, name, class_name)
            if found:
                return found

        return None

    def wait_for_control(self, control_type, search_params, search_depth=1, timeout=30, retry_interval=0.5):
        """
        Waits for a given control type to become available with the specified search parameters.

        Args:
            control_type: The type of control, e.g., auto.WindowControl, auto.ButtonControl, etc.
            search_params (dict): Search parameters used to identify the control.
                                The keys must match the properties used in the control type, e.g., 'AutomationId', 'Name'.
            search_depth (int): How deep to search in the user interface.
            timeout (int): Maximum time to wait for the control, in seconds.
            retry_interval (float): Time to wait between retries, in seconds.

        Returns:
            Control: The control object if found, otherwise raises TimeoutError.

        Raises:
            TimeoutError: If the control is not found within the timeout period.
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                control = control_type(searchDepth=search_depth, **search_params)
                if control.Exists(0, 0):
                    return control
            except Exception as e:
                print(f"Error while searching for control: {e}")

            time.sleep(retry_interval)
            print(f"Retrying to find control: {search_params}...")

        raise TimeoutError(f"Control with parameters {search_params} was not found within the {timeout} second timeout.")

    def wait_for_control_to_disappear(self, control_type, search_params, search_depth=1, timeout=30):
        """
        Waits for a given control type to disappear with the specified search parameters.

        Args:
            control_type: The type of control, e.g., auto.WindowControl, auto.ButtonControl, etc.
            search_params (dict): Search parameters used to identify the control.
                                The keys must match the properties used in the control type, e.g., 'AutomationId', 'Name'.
            search_depth (int): How deep to search in the user interface.
            timeout (int): How long to wait, in seconds.

        Returns:
            bool: True if the control disappeared within the timeout period, otherwise False.
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                control = control_type(searchDepth=search_depth, **search_params)
                if not control.Exists(0, 0):
                    return True
            except Exception as e:
                print(f"Error while searching for control: {e}")

            time.sleep(0.5)
            print(f"Retrying to find control: {search_params}...")

        raise TimeoutError(f"Control with parameters {search_params} did not disappear within the timeout period.")

    def start_application(self):
        """
        Starts the application using the specified path.
        """
        os.startfile(self.app_path)

    def login(self):
        """
        Logs into the application by entering the username and password.
        Checks if the login window is open and ready.
        Checks if the main window is opened and ready.
        """
        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormLogin'},
            search_depth=3,
            timeout=60
        )
        self.app_window.SetFocus()

        username_box = self.app_window.EditControl(AutomationId="TextLogin")
        username_box.SendKeys(text=self.username)

        password_box = self.app_window.EditControl(AutomationId="TextPwd")
        password_box.SendKeys(text=self.password)

        login_button = self.app_window.PaneControl(AutomationId="ButtonLogin")
        login_button.SetFocus()
        login_button.SendKeys('{ENTER}')

        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormFront'},
            search_depth=2,
            timeout=60
        )

    def open_patient(self, ssn):
        """
        When the main window is open, presses Ctrl + O to open the 'Open Patient' window,
        searches for the SSN, and opens the patient.
        """
        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormFront'},
            search_depth=2,
            timeout=5
        )

        self.app_window.SetFocus()
        self.app_window.SendKeys('{Ctrl}o', waitTime=0)

        open_patient_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormOpenPatient'},
            search_depth=2
        )
        open_patient_window.SetFocus()

        ssn_input = open_patient_window.EditControl(AutomationId="TextBoxCpr")
        search_button = open_patient_window.PaneControl(AutomationId="ButtonOk")

        ssn_input.SendKeys(text=ssn)
        search_button.SetFocus()
        search_button.SendKeys('{ENTER}')

        try:
            error_window = self.wait_for_control(
                auto.WindowControl,
                {'Name': 'TMT - Åbn patient'},
                search_depth=2,
                timeout=10
            )

            if error_window is not None:
                error_window_button = error_window.ButtonControl(Name="OK")
                error_window_button.SetFocus()
                error_window_button.Click(simulateMove=False, waitTime=0)

                raise ManualProcessingRequiredError

        except TimeoutError:
            pass

        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormPatient'},
            timeout=10
        )

        self.app_window.Maximize()

    def open_sub_tab(self, sub_tab_name: str):
        """
        Opens a specific sub-tab in the patient's main card.

        Args:
            sub_tab_name (str): The name of the sub-tab to open (e.g., "Dokumenter").
        """
        sub_tab_button = self.app_window.TabItemControl(Name=sub_tab_name)
        is_sub_tab_selected = sub_tab_button.GetPattern(10010).IsSelected

        if not is_sub_tab_selected:
            sub_tab_button.SetFocus()
            sub_tab_button.SendKeys('{ENTER}')

    def open_tab(self, tab_name: str):
        """
        Opens a specific tab in the patient's main card.

        Args:
            tab_name (str): The name of the tab to open (e.g., "Frit valg").
        """
        match tab_name:
            case "Stamkort":
                tab_name_modified = "S&tamkort"
            case "Fritvalg":
                tab_name_modified = "F&ritvalg"
            case "Journal":
                tab_name_modified = "&Journal"

        tab_button = self.find_element_by_property(
            control=self.app_window,
            control_type=auto.ControlType.TabItemControl,
            name=tab_name_modified
        )
        is_tab_selected = tab_button.GetPattern(10010).IsSelected

        if not is_tab_selected:
            tab_button.SetFocus()
            tab_button.SendKeys('{ENTER}')

    def create_document(self, document_full_path: str = None, document_type: str = None, document_description: str = None):
        """
        Creates a new document under the 'Dokumenter' tab.

        Args:
            document_full_path (str, optional): The full path of the document to upload.
            document_type (str, optional): The type of document to select from the dropdown.
        """
        self.open_tab("Stamkort")
        self.open_sub_tab("Dokumenter")

        document_list = self.find_element_by_property(
            control=self.app_window,
            control_type=auto.ControlType.ListControl,
            automation_id="cleverListView1"
        )
        document_list.RightClick(simulateMove=False, waitTime=0)

        document_list_menu = self.wait_for_control(
            auto.MenuControl,
            {'Name': 'Kontekst'},
            search_depth=2
        )

        menu_create_document = self.find_element_by_property(
            control=document_list_menu,
            control_type=auto.ControlType.MenuItemControl,
            name="Opret"
        )
        menu_create_document.Click(simulateMove=False, waitTime=0)

        create_document_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'UploadFile'},
            search_depth=2
        )
        file_path_textbox = self.find_element_by_property(
            control=create_document_window,
            control_type=auto.ControlType.EditControl,
            automation_id="textBoxLocalFilePath"
        )
        legacy_pattern = file_path_textbox.GetLegacyIAccessiblePattern()
        legacy_pattern.SetValue(document_full_path)

        if document_type:
            document_type_drop_down = self.find_element_by_property(
                control=create_document_window,
                control_type=auto.ControlType.ButtonControl,
                name="Åbn"
            )
            document_type_drop_down.Click(simulateMove=False, waitTime=0)

            document_type_button = self.find_element_by_property(
                control=create_document_window,
                control_type=auto.ControlType.ListItemControl,
                name=document_type
            )
            document_type_button.Click(simulateMove=False, waitTime=0)

        if document_description:
            description_text_field = self.find_element_by_property(
                control=create_document_window,
                control_type=auto.ControlType.DocumentControl,
                automation_id="richTextBoxDescription"
            )
            value_pattern = description_text_field.GetPattern(auto.PatternId.ValuePattern)
            value_pattern.SetValue(document_description)

        button_create_document = self.find_element_by_property(
            control=create_document_window,
            control_type=auto.ControlType.PaneControl,
            automation_id="buttonOpen"
        )
        button_create_document.Click(simulateMove=False, waitTime=0)

    def create_event(self, event_message: str, patient_clinic: str):
        """
        Creates an event for the given patient.

        Args:
            event_title (str): The title of the event to create.
            patient_clinic (str): The clinic associated with the patient.
        """
        self.open_tab("Stamkort")

        menu_funktioner = self.app_window.MenuItemControl(Name="Funktioner")
        menu_funktioner.Click(simulateMove=False, waitTime=0)

        henvis_patient = self.app_window.Control(
            Name="Henvis patient",
            ControlType=auto.ControlType.MenuItemControl
        )
        henvis_patient.Click(simulateMove=False, waitTime=0)

        clinic_list = self.wait_for_control(
            auto.WindowControl,
            {"AutomationId": "FormFindClinics"},
            search_depth=2
        )

        clinic_list_items = clinic_list.ListControl(AutomationId="ListClinics")
        clinic_list_item = clinic_list_items.Control(
            Name=patient_clinic,
            ControlType=auto.ControlType.ListItemControl
        )
        clinic_list_item.GetPattern(10017).ScrollIntoView()
        clinic_list_item.SetFocus()
        clinic_list_item.DoubleClick(simulateMove=False, waitTime=0)

        message_window = self.wait_for_control(
            auto.WindowControl,
            {"AutomationId": "VBInputBox"},
            search_depth=2
        )
        message_textbox = message_window.EditControl(AutmationId="TextBox")
        message_textbox_legacy_pattern = message_textbox.GetLegacyIAccessiblePattern()
        message_textbox_legacy_pattern.SetValue(event_message)
        message_textbox.SendKeys('{ENTER}')

        self.wait_for_control(
            self.app_window.TextControl,
            {'RegexName': '^Henvisning.*$'},
            search_depth=2
        )

        message_button = self.app_window.ButtonControl(Name="OK")
        message_button.Click(simulateMove=False, waitTime=0)

    def create_journal_note(self, note_message: str, checkmark_in_complete: bool):
        """
        Creates a journal note for the given patient.

        Args:
            note_message (str): The note message.
            checkmark_in_complete (bool): Checks the checkmark in 'Afslut'.
        """
        self.open_tab("Journal")

        self.wait_for_control(
            auto.DocumentControl,
            {"AutomationId": "RichTextBoxInput"},
            search_depth=19
            )

        input_box = self.app_window.DocumentControl(AutomationId="RichTextBoxInput")
        input_box_value_pattern = input_box.GetValuePattern()
        input_box_value_pattern.SetValue(value=note_message, waitTime=0)

        if checkmark_in_complete:
            checkbox = self.app_window.CheckBoxControl(AutomationId="CheckBoxAssignCompletionStatus")
            checkbox.SetFocus()
            checkbox.Click(simulateMove=False, waitTime=0)

        save_button = self.app_window.PaneControl(AutomationId="buttonSave")
        save_button.SetFocus()
        save_button.Click(simulateMove=False, waitTime=0)

    def close_patient_window(self):
        """
        Closes the current patient's window and ensures the application returns to the main window.

        Raises:
            TimeoutError: If the patient window does not close within the expected time.
        """

        title_bar_window = self.app_window.TitleBarControl()
        title_bar_window.ButtonControl(Name="Luk").Click(simulateMove=False, waitTime=0)

        self.app_window = self.wait_for_control_to_disappear(
            auto.WindowControl,
            {'AutomationId': 'FormPatient'},
            search_depth=2
        )

        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormFront'},
            search_depth=2,
            timeout=5
        )

    def close_solteq_tand(self):
        """
        Closes the SolteqTand application and confirms the closure.

        Raises:
            TimeoutError: If the application does not close within the expected time.
        """
        self.app_window = self.wait_for_control(
            auto.WindowControl,
            {'AutomationId': 'FormFront'},
            search_depth=2
        )
        self.app_window.SetFocus()
        title_bar_window = self.app_window.TitleBarControl()
        title_bar_window.ButtonControl(Name="Luk").Click(simulateMove=False, waitTime=0)

        self.app_window = self.wait_for_control(
            auto.ButtonControl,
            {'Name': 'Ja'},
            search_depth=3
        )

        self.app_window.Click(simulateMove=False)

        self.app_window = self.wait_for_control_to_disappear(
            auto.WindowControl,
            {'AutomationId': 'FormFront'},
            search_depth=2
        )
