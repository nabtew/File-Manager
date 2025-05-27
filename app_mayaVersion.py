from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QWidget
from PySide6.QtGui import QFont
import subprocess
import sys
import os
import shutil
import json
import ui4 # ไฟล์ UI ที่ถูกแปลงเป็น Python

from shiboken6 import wrapInstance
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from importlib import reload

moduleDir = os.path.dirname(__file__) # find file location
json_data_path = os.path.join(moduleDir, "json_data.json")

maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)

def setup_ui_maya(parent): #Qt Module to load .ui file
    # read .ui directly
    myWidget = QMainWindow(parent) # สร้างหน้าต่างหลัก
    ui = ui4.Ui_NabtewStudio() # เรียกใช้คลาสในไฟล์ .py ที่แปลงมา
    ui.setupUi(myWidget) # เซ็ตอัพ UI
    return myWidget, ui # รีเทิร์นทั้ง widget และตัว ui เพื่อเข้าถึง element ข้างในได้

class App(QMainWindow):
    def __init__(self):
        super().__init__()  # เรียก constructor ของ QMainWindow
        self.ui = ui4.Ui_NabtewStudio()  # สร้าง instance ของ Ui_NabtewStudio
        self.ui.setupUi(self)  # เชื่อม UI กับ QMainWindow
        self.setup_tools()  # เรียกใช้ฟังก์ชันสำหรับตั้งค่าเริ่มต้น
        self.item_list_asset = []

    def setup_tools(self):
        try:
            self.data_json()        
            self.setup_project_box()
            self.setup_department_box()
            self.setup_type()
            self.setup_section_box()
            self.setup_storage()
            self.list_file_in_folder("{}".format(self.user_path), self.ui.project_box)

            self.ui.Storage_box.currentIndexChanged.connect(self.storage)
            self.ui.project_box.currentIndexChanged.connect(self.project)
            self.ui.section_box.currentIndexChanged.connect(self.section)
            self.ui.department1_box.currentIndexChanged.connect(self.department1)
            self.ui.department2_box.currentIndexChanged.connect(self.department2)
            self.ui.type_box.currentIndexChanged.connect(self.type) 
            self.ui.asset_list_box.itemClicked.connect(self.asset_list)
            self.ui.scene_list_box.itemClicked.connect(self.scene_list)
            self.ui.asset_ver_box.itemClicked.connect(self.asset_ver)
            self.ui.scene_ver_box.itemClicked.connect(self.scene_ver)
            self.ui.asset_search_box.textChanged.connect(self.search_key)
            self.ui.scene_search_box.textChanged.connect(self.search_key)
           
            self.ui.open_button.clicked.connect(self.open_file)
            self.ui.publish_button.clicked.connect(self.publish)
            self.ui.data_button.clicked.connect(self.data)
            self.ui.export_button.clicked.connect(self.export)

        except AssertionError as e:
            print(f"Error setting up tools: {e}")           

    def setup_department_box(self):
        # เพิ่ม department ลงใน ComboBox: department_box
        self.depart_grp = [self.ui.department1_box, self.ui.department2_box]
        for depart in self.depart_grp:
            depart.insertItem(0, "- Department -") # เพิ่ม Placeholder
            depart.setEditable(False)  # ตั้งค่าให้ ComboBox ไม่สามารถแก้ไขได้
            depart.setCurrentIndex(0)  # ตั้งค่าเริ่มต้นให้เลือก Placeholder

    def setup_project_box(self):
        # เพิ่ม project ลงใน ComboBox: project_box
        self.ui.project_box.insertItem(0, "- Project -") # เพิ่ม Placeholder
        self.ui.project_box.setEditable(False)  # ตั้งค่าให้ ComboBox ไม่สามารถแก้ไขได้
        self.ui.project_box.setCurrentIndex(0)  # ตั้งค่าเริ่มต้นให้เลือก Placeholder

    def setup_storage(self):
        # เพิ่ม storage type ลงใน ComboBox: storage_box
        self.ui.Storage_box.insertItem(0, "- File Storage -")
        self.ui.Storage_box.setEditable(False)
        self.ui.Storage_box.setCurrentIndex(0)

    def setup_type(self):
        # เพิ่ม storage type ลงใน ComboBox: type_box
        self.ui.type_box.insertItem(0, "- Type -")
        self.ui.type_box.setEditable(False)
        self.ui.type_box.setCurrentIndex(0)

    def setup_section_box(self):
        # เพิ่ม project ลงใน ComboBox: section_box
        self.ui.section_box.insertItem(0, "- Section -") # เพิ่ม Placeholder
        self.ui.section_box.setEditable(False)  # ตั้งค่าให้ ComboBox ไม่สามารถแก้ไขได้
        self.ui.section_box.setCurrentIndex(0)  # ตั้งค่าเริ่มต้นให้เลือก Placeholder

    def project(self):
        self.user_project = self.ui.project_box.currentText() #get current ""(project) from user
        self.ui.Storage_box.clear()
        self.ui.Storage_box.insertItem(0, "- File Storage -")
        self.list_file_in_folder("{}/{}/File".format(self.user_path, self.user_project), self.ui.Storage_box)

    def storage(self):
        self.user_storage = self.ui.Storage_box.currentText()
        self.ui.type_box.clear()
        self.ui.type_box.insertItem(0, "- Type -")
        self.list_file_in_folder("{}/{}/File/{}/Assets".format(self.user_path, self.user_project, self.user_storage), self.ui.type_box)
        self.ui.section_box.clear()
        self.ui.section_box.insertItem(0, "- Section -")
        self.list_file_in_folder("{}/{}/File/{}/Scenes".format(self.user_path, self.user_project, self.user_storage), self.ui.section_box)

    def department2(self):
        self.ui.scene_search_box.clear()
        self.ui.scene_list_box.clear()
        self.ui.scene_ver_box.clear()
        if self.ui.department2_box.currentText() == "- Department -":
            pass
            
        elif self.ui.department2_box.currentText() == "":
            pass

        else:
            self.user_department2 = self.ui.department2_box.currentText() #get current ""(department) from user
            self.list_file_in_folder("{}/{}/File/{}/Scenes/{}".format(self.user_path, self.user_project, self.user_storage, self.user_section), self.ui.scene_list_box)
            self.item_list_scene = [self.ui.scene_list_box.item(i).text() for i in range(self.ui.scene_list_box.count())]

    def department1(self):
        self.ui.asset_search_box.clear()
        self.ui.asset_list_box.clear()
        self.ui.asset_ver_box.clear()
        if self.ui.department1_box.currentText() == "- Department -":
            pass

        elif self.ui.department1_box.currentText() == "":
            pass

        else:
            self.user_department1 = self.ui.department1_box.currentText() #get current ""(department) from user
            self.list_file_in_folder("{}/{}/File/{}/Assets/{}".format(self.user_path, self.user_project, self.user_storage, self.user_type), self.ui.asset_list_box)
            self.item_list_asset = [self.ui.asset_list_box.item(i).text() for i in range(self.ui.asset_list_box.count())]

    def delete_list(self, suffix, check_list):
        if check_list == False:
            current_tab_index = self.ui.tabList.currentIndex()
            if current_tab_index == 0:
                for i in self.asset_list_grp:
                    if i.endswith(suffix):
                        self.asset_delete_grp.append()
            elif current_tab_index == 1:
                for i in self.scene_list_grp:
                    if i.endswith(suffix):
                        self.scene_delete_grp.append()
        else:
            pass

    def type(self):
        self.user_type = self.ui.type_box.currentText() #get current ""(type) from user
        self.ui.department1_box.clear()
        self.ui.department1_box.insertItem(0, "- Department -")
        self.ui.department1_box.addItems(self.departments)

    def section(self):
        self.user_section = self.ui.section_box.currentText() #get current ""(section) from user
        self.ui.department2_box.clear()
        self.ui.department2_box.insertItem(0, "- Department -")
        self.ui.department2_box.addItems(self.departments)

    def asset_list(self):
        self.ui.asset_ver_box.clear()
        for item in self.ui.asset_list_box.selectedItems():
            self.user_asset = item.text()
            self.list_file_in_folder("{}/{}/File/{}/Assets/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_type, self.user_asset, self.user_department1), self.ui.asset_ver_box)

    def scene_list(self):
        self.ui.scene_ver_box.clear()
        for item in self.ui.scene_list_box.selectedItems():
            self.user_scene = item.text()
            self.list_file_in_folder("{}/{}/File/{}/Scenes/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_section, self.user_scene, self.user_department2), self.ui.scene_ver_box)
        print(self.ui.scene_list_box.selectedItems())

    def asset_ver(self):
        for item in self.ui.asset_ver_box.selectedItems():
            self.user_asset_ver = item.text()
            self.asset_ver_path = "{}/{}/File/{}/Assets/{}/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_type, self.user_asset, self.user_department1, self.user_asset_ver)

    def scene_ver(self):
        for item in self.ui.scene_ver_box.selectedItems():
            self.user_scene_ver = item.text()
            self.scene_ver_path = "{}/{}/File/{}/Scenes/{}/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_section, self.user_scene, self.user_department2, self.user_scene_ver)

    def open_file(self):
        current_widget = self.ui.tabList.currentIndex()

        if current_widget == 0:
            file_name_only, file_extension = os.path.splitext(self.asset_ver_path)
            if file_extension == ".ma":
                subprocess.Popen([self.maya_path, self.asset_ver_path], shell=True)

            elif file_extension == ".mb":
                subprocess.Popen([self.maya_path, self.asset_ver_path], shell=True)

            elif file_extension == ".spp":
                subprocess.Popen([self.spp_path, self.asset_ver_path], shell=True)
        
        elif current_widget == 1:
            file_name_only, file_extension = os.path.splitext(self.scene_ver_path)

            if file_extension == ".ma":
                subprocess.Popen([self.maya_path, self.scene_ver_path], shell=True)

            elif file_extension == ".mb":
                subprocess.Popen([self.maya_path, self.scene_ver_path], shell=True)

            elif file_extension == ".spp":
                subprocess.Popen([self.spp_path, self.scene_ver_path], shell=True)

    def publish(self):
        current_widget = self.ui.tabList.currentIndex()
        if current_widget == 0:
            path = "{}/{}/File/Publish/Assets/{}/{}/{}".format(self.user_path, self.user_project, self.user_type, self.user_asset, self.user_department1)
            pub_path = os.path.join(path, self.user_asset_ver)
            ver_path = self.asset_ver_path
            Fname = self.user_asset_ver

            if os.path.exists(pub_path):
                self.suffix_dialog(Fname, path, ver_path)

            else:
                if os.path.exists(self.asset_ver_path):
                   shutil.copy(self.asset_ver_path, path)

        elif current_widget == 1:
            path = "{}/{}/File/{}/Scenes/{}/{}/{}".format(self.user_path, self.user_project, "Publish" , self.user_section, self.user_scene, self.user_department2)
            pub_path = os.path.join(path, self.user_scene_ver)
            ver_path = self.scene_ver_path
            Fname = self.user_scene_ver

            if os.path.exists(pub_path):
                self.suffix_dialog(Fname, path, ver_path)

            else:    
                if os.path.exists(self.scene_ver_path):
                    shutil.copy(self.scene_ver_path, path)

    def suffix_dialog(self, Fname, path, ver_path):
        suffixBox = QMessageBox(self)
        suffixBox.setText("file already exists, do u wanna overwrite?   ")
        suffixBox.setWindowTitle("Suffix")
        suffixBox.resize(400, 129)

        font = QFont("Microsoft YaHei Light", 12)
        suffixBox.setFont(font)

        owr = suffixBox.addButton(QMessageBox.Yes)
        owr.setFont(font)
        sfx = suffixBox.addButton(QMessageBox.No)
        sfx.setFont(font)

        result = suffixBox.exec()

    def search_key(self):
        current_widget = self.ui.tabList.currentIndex()
        if current_widget == 0:
            name_file_search = self.ui.asset_search_box.text()
            self.ui.asset_list_box.clear()
            self.ui.asset_ver_box.clear()
            for item in self.item_list_asset:
                if name_file_search.lower() in item.lower():
                    self.ui.asset_list_box.addItem(item)

                else:
                    pass

        elif current_widget == 1:
            name_file_search = self.ui.scene_search_box.text()
            self.ui.scene_list_box.clear()
            self.ui.scene_ver_box.clear()
            for item in self.item_list_scene:
                if name_file_search.lower() in item.lower():
                    self.ui.scene_list_box.addItem(item)

                else:
                    pass
    
    def export(self):
        current_widget = self.ui.tabList.currentIndex()
        if current_widget == 0:
            Fname = self.user_asset_ver
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(
                None,
                "export to",
                "{}".format(Fname),
                "All Files (*)",
                options=options
            )

            if file_path:
                print("export to:", file_path)
            else:
                print("cancle")

            ver_path = self.asset_ver_path
            export_path = os.path.join(file_path, self.user_asset_ver)


            if os.path.exists(export_path):
                self.suffix_dialog(Fname, file_path, ver_path)

            else:
                if os.path.exists(self.asset_ver_path):
                   shutil.copy(self.asset_ver_path, file_path)

        elif current_widget == 1:
            Fname = self.user_scene_ver
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(
                None,
                "export to",
                "{}".format("A"),
                "All Files (*)",  # กำหนดประเภทไฟล์
                options=options
            )

            if file_path:
                print("export to:", file_path)
            else:
                print("cancle")

            ver_path = self.scene_ver_path
            export_path = os.path.join(file_path, self.user_scene_ver)


            if os.path.exists(export_path):
                self.suffix_dialog(Fname, file_path, ver_path)

            else:
                if os.path.exists(self.scene_ver_path):
                   shutil.copy(self.scene_ver_path, file_path)

    def data(self):
        subprocess.Popen(['notepad', r'{}'.format(json_data_path)])
        self.ui.project_box.setCurrentIndex(0)


    def list_file_in_folder(self, folder_path, list_widget):
        try:
            if not os.path.exists(folder_path):
                return

            #Iterate through files in the folder
            for file_name in os.listdir(folder_path):
                list_widget.addItem(file_name)

        except:
            print("")

    def data_json(self):
        #อ่าน data file path จาก .json
        with open(json_data_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        #ประกาศตัวแปรให้กับ data ของ file path
        self.departments = data.get("Department", [])
        self.user_path = data.get("User_path", "{}".format([]))
        self.maya_path = data.get("Maya_path", "{}".format([]))
        self.spp_path = data.get("spp_path", "{}".format([]))

maya_ptr = omui.MQtUtil.mainWindow()
ptr = wrapInstance(int(maya_ptr), QWidget)
mainUi = App()
mainUi.show()
