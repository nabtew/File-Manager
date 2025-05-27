from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QInputDialog, QDialog
from PySide6.QtGui import QFont
import subprocess
import sys
import os
import re
import shutil
import json
import ui4 # ไฟล์ UI ที่ถูกแปลงเป็น Python

moduleDir = os.path.dirname(__file__) # find file location
json_data_path = os.path.join(moduleDir, "json_data.json")

class App(QDialog):
    def __init__(self):
        super().__init__()  # เรียก constructor ของ QMainWindow
        self.ui = ui4.Ui_NabtewStudio()  # สร้าง instance ของ Ui_NabtewStudio
        self.ui.setupUi(self)  # เชื่อม UI กับ QMainWindow
        self.setup_tools()  # เรียกใช้ฟังก์ชันสำหรับตั้งค่าเริ่มต้น
        self.item_list_asset = []
        #self.show()  # แสดงหน้าต่าง

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
            self.ui.Storage_box.currentIndexChanged.connect(self.section_add_unenable)
            self.ui.project_box.currentIndexChanged.connect(self.project)
            self.ui.section_box.currentIndexChanged.connect(self.section)
            self.ui.section_box.currentIndexChanged.connect(self.section_del_unenable)
            self.ui.department1_box.currentIndexChanged.connect(self.department1)
            self.ui.department1_box.currentIndexChanged.connect(self.assets_add_unenable)
            self.ui.department2_box.currentIndexChanged.connect(self.department2)
            self.ui.department2_box.currentIndexChanged.connect(self.scene_add_unenable)
            self.ui.type_box.currentIndexChanged.connect(self.type) 
            self.ui.asset_list_box.itemClicked.connect(self.asset_list)
            self.ui.asset_list_box.itemSelectionChanged.connect(self.asset_del_unenable)
            self.ui.scene_list_box.itemClicked.connect(self.scene_list)
            self.ui.scene_list_box.itemSelectionChanged.connect(self.scene_del_unenable)
            self.ui.asset_ver_box.itemClicked.connect(self.asset_ver)
            self.ui.scene_ver_box.itemClicked.connect(self.scene_ver)
            self.ui.asset_search_box.textChanged.connect(self.search_key)
            self.ui.scene_search_box.textChanged.connect(self.search_key)
           
            self.ui.open_button.clicked.connect(self.open_file)
            self.ui.publish_button.clicked.connect(self.publish)
            self.ui.data_button.clicked.connect(self.data)
            self.ui.export_button.clicked.connect(self.export)
            self.ui.addProject_button.clicked.connect(self.add_project)
            self.ui.delProject_button.clicked.connect(self.del_project)
            self.ui.addAsset_button.clicked.connect(self.add_scene)
            self.ui.delAsset_button.clicked.connect(self.del_scene)
            self.ui.addScene_button.clicked.connect(self.add_scene)
            self.ui.delScene_button.clicked.connect(self.del_scene)
            self.ui.addSection_button.clicked.connect(self.add_section)
            self.ui.delSection_button.clicked.connect(self.del_section)



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

    def scene_add_unenable(self):
        section = self.ui.department2_box.currentIndex()
        if section == 0:
            self.ui.addScene_button.setEnabled(False)
        else:
            self.ui.addScene_button.setEnabled(True)

    def scene_del_unenable(self):
        self.ui.delScene_button.setEnabled(False)

    def assets_add_unenable(self):
        section = self.ui.department1_box.currentIndex()
        if section == 0:
            self.ui.addAsset_button.setEnabled(False)
        else:
            self.ui.addAsset_button.setEnabled(True)

    def asset_del_unenable(self):
        self.ui.delAsset_button.setEnabled(False)

    def section_add_unenable(self):
        section = self.ui.Storage_box.currentIndex()
        if section == 0:
            self.ui.addSection_button.setEnabled(False)
        else:
            self.ui.addSection_button.setEnabled(True)

    def section_del_unenable(self):
        section = self.ui.section_box.currentIndex()
        if section == 0:
            self.ui.delSection_button.setEnabled(False)
        else:
            self.ui.delSection_button.setEnabled(True)

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
        self.ui.addSection_button.setEnabled(True)

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
        self.ui.delAsset_button.setEnabled(True)
        for item in self.ui.asset_list_box.selectedItems():
            self.user_asset = item.text()
            self.list_file_in_folder("{}/{}/File/{}/Assets/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_type, self.user_asset, self.user_department1), self.ui.asset_ver_box)

    def scene_list(self):
        self.ui.scene_ver_box.clear()
        self.ui.delScene_button.setEnabled(True)
        for item in self.ui.scene_list_box.selectedItems():
            self.user_scene = item.text()
            self.list_file_in_folder("{}/{}/File/{}/Scenes/{}/{}/{}".format(self.user_path, self.user_project, self.user_storage, self.user_section, self.user_scene, self.user_department2), self.ui.scene_ver_box)

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
            path = "{}/{}/File/Publish/Scenes/{}/{}/{}".format(self.user_path, self.user_project, self.user_section, self.user_scene, self.user_department2)
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

        suffix_button = suffixBox.addButton("Suffix", QMessageBox.ActionRole)
        suffix_button.setFont(font)

        overwrite_button = suffixBox.addButton("Overwrite", QMessageBox.ActionRole)
        overwrite_button.setFont(font)

        cancel_button = suffixBox.addButton("Cancel", QMessageBox.RejectRole)
        cancel_button.setFont(font)

        suffixBox.exec()

        if suffixBox.clickedButton() == suffix_button:
    
            dir_name, base_name = os.path.split(ver_path)
            name, ext = os.path.splitext(base_name)
            match = re.search(r"_(\d+)$", name)

            if match:
                base_name = name[:match.start()]
                print("match")
            else:
                base_name = name
                print("not match")

            num = 1
            new_name = f"{base_name}_{num}{ext}"
            new_path = os.path.join(path, new_name)
            while os.path.exists(new_path):
                print(new_path)
                new_path = os.path.join(path, f"{base_name}_{num}{ext}")
                num += 1

            try:
                shutil.copy(ver_path, new_path)
                return path
            
            except Exception as e:
                print(f"Error: {e}")
                return "error"
    
        elif suffixBox.clickedButton() == overwrite_button:
            return "overwrite"
        else:
            return "cancel"
        
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

    def add_section(self):
        list_scene_path = "{}/{}/File/{}/Scenes".format(self.user_path, self.user_project, self.user_storage)
        
        app = QApplication([])
        user_input, ok = QInputDialog.getText(None, "Input", "Rename")
        app.quit()

        found = False

        if ok and user_input: #check text exist or not
            for file_name in os.listdir(list_scene_path):
                if user_input == file_name:
                    found = True
                    app = QApplication([])
                    QMessageBox.warning(None, "Warning", "The name exists, please create a new one")
                    app.quit()
                    break
            if not found:
                full_path = os.path.join(list_scene_path, user_input)
                os.makedirs(full_path, exist_ok=True)
                self.storage()
                #shutil.copytree(self.section_path, full_path, dirs_exist_ok=True)
        
        elif ok and user_input:
            app = QApplication([])
            QMessageBox.warning(None, "Warning", "Please write any name before clicking OK button")
            app.quit()
        else:
            pass

    def del_section(self):
        try:
            path = "{}/{}/File/{}/Scenes".format(self.user_path, self.user_project, self.user_storage)
            full_path = os.path.join(path, self.user_section)
            shutil.rmtree(full_path)

            self.storage()

            app = QApplication([])
            QMessageBox.warning(None, "Warning", "Section deleted successfully")
            app.quit()

        except:
            app = QApplication([])
            QMessageBox.critical(None, "Error", f"Could not delete section. Error: {e}")
            app.quit()

    def add_project(self):
        user_input, ok = QInputDialog.getText(None, "Input", "Rename")
        if not user_input: #check text exist or not
            QMessageBox.warning(self, "Warning", "Please write a name before clicking OK.")
            return
        
        project_exists = False
        for file_name in os.listdir(self.user_path):
            if user_input == file_name:
                project_exists = True
                break

            if project_exists:
                QMessageBox.warning(self, "Warning", "The name already exists, please create a new one.")
                return

            full_path = os.path.join(self.user_path, user_input)
            os.makedirs(full_path, exist_ok=True)
            shutil.copytree(self.project_path, full_path, dirs_exist_ok=True)

            self.ui.project_box.clear()
            self.setup_project_box()
            self.list_file_in_folder("{}".format(self.user_path), self.ui.project_box)

    def del_project(self):
        try:
            full_path = os.path.join(self.user_path, self.user_project)
            shutil.rmtree(full_path)
            self.ui.project_box.clear()
            self.setup_project_box()
            self.list_file_in_folder("{}".format(self.user_path), self.ui.project_box)
            QMessageBox.warning(self, "werning", "section deleted successfully")
        except:
            QMessageBox.warning(self, "Error", f"Error deleting section: {e}")

    def add_scene(self):
        user_input, ok = QInputDialog.getText(None, "Input", "Rename")

        if not user_input:
            QMessageBox.warning(self, "Warning", "Please write a name before clicking OK.")
            return

        list_scene_path = os.path.join(self.user_path, self.user_project, "File", self.user_storage, "Scenes", self.user_section)
        os.makedirs(list_scene_path, exist_ok=True) # สร้าง directory หลักของ Scenes ไว้ก่อน

        scene_exists = False
        for file_name in os.listdir(list_scene_path):
            if user_input == file_name:
                scene_exists = True
                break

        if scene_exists:
            QMessageBox.warning("Warning", "The name already exists, please create a new one.")
            return

        full_path = os.path.join(list_scene_path, user_input)
        try:
            shutil.copytree(self.file_path, full_path, dirs_exist_ok=True)
            self.department2() # เรียก method ที่เกี่ยวข้องกับการอัพเดท UI หรือส่วนอื่นๆ
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"Error: Source file path not found: {self.file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error creating scene: {e}")

    def del_scene(self):
        try:
            path = os.path.join(self.user_path, self.user_project, "File", self.user_storage, "Scenes", self.user_section)
            full_path = os.path.join(path, self.user_scene)
            shutil.rmtree(full_path)
            self.department2()
            QMessageBox.warning(self, "Warning", "Scene deleted successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error deleting scene: {e}")

    def add_asset(self):
        user_input, ok = QInputDialog.getText(None, "Input", "Rename")

        if not user_input:
            QMessageBox.warning(self, "Warning", "Please write a name before clicking OK.")
            return

        list_asset_path = os.path.join(self.user_path, self.user_project, "File", self.user_storage, "Assets", self.user_type)
        os.makedirs(list_asset_path, exist_ok=True) # สร้าง directory หลักของ Assets ไว้ก่อน

        asset_exists = False
        for file_name in os.listdir(list_asset_path):
            if user_input == file_name:
                asset_exists = True
                break

        if asset_exists:
            QMessageBox.warning(self, "Warning", "The name already exists, please create a new one.")
            return

        full_path = os.path.join(list_asset_path, user_input)
        try:
            shutil.copytree(self.file_path, full_path, dirs_exist_ok=True)
            self.department1() # เรียก method ที่เกี่ยวข้องกับการอัพเดท UI หรือส่วนอื่นๆ
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"Error: Source file path not found: {self.file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error creating asset: {e}")

    def del_asset(self):
        try:
            path = os.path.join(self.user_path, self.user_project, "File", self.user_storage, "Assets", self.user_type)
            full_path = os.path.join(path, self.user_scene)
            shutil.rmtree(full_path)
            self.department1()
            QMessageBox.warning(self, "Warning", "Asset deleted successfully.") # แก้คำผิดและเปลี่ยนเป็นแจ้งสำเร็จ
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error deleting asset: {e}")

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
        self.project_path = data.get("project_path", "{}".format([]))
        self.file_path = data.get("file_path", "{}".format([]))
        self.maya_path = data.get("Maya_path", "{}".format([]))
        self.spp_path = data.get("spp_path", "{}".format([]))

def show_app():
    app = QApplication(sys.argv)
    demo = App()
    demo.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    show_app()
