"""
> storage for all ui style sheets to maintain
> consistent look across all UIs

>> need to make this more easily adaptable
"""


def labelHeadingStyleSheet() -> str:
    stylesheet: str = """
    QLabel { 
    color: rgb(235, 235, 235); 
    font-family: Microsoft YaHei UI;
    font-size: 12px;
    }
    """
    return stylesheet

def label_text_stylesheet() -> str:
    stylesheet:str = """
    QLabel { 
    color: rgb(115, 115, 122);
    font-family: Microsoft YaHei UI;
    font-size: 11px;
    }
    """
    return stylesheet

def group_box_stylesheet() -> str:
    stylesheet: str = """
    QGroupBox  {
    border: 1px solid rgb(69, 70, 75);
    border-color: rgb(69, 70, 75);
    border-radius: 6px; 
    padding-left: 6px;
    padding-top: 6px;
    padding-bottom: 6px;
    padding-right: 6px; } 
    QGroupBox::title  {
    padding: 5px 8000px 5px 8000px;
    background-color: transparent;
    color: transparent; }
    """
    return stylesheet

def line_edit_stylesheet() -> str:
    stylesheet:str = """
    QLineEdit {
    border: 1px solid rgb(64, 65, 70);
    border-radius: 2px;
    background-color: rgb(36, 37, 40);
    color: rgb(226, 233, 235);
    padding-left: 3px;
    padding-right: 5px; 
    font-family: Microsoft YaHei UI;
    font-size: 12px; }
    """
    return stylesheet

def slider_stylesheet() -> str:
    stylesheet: str = """
    QSlider::groove:horizontal {
    border: 1px solid rgb(43, 114, 184);
    background: rgb(43, 114, 184);
    height: 2px; }
    QSlider::handle:horizontal {
    background: rgb(36, 37, 40);
    width: 20px;
    margin: -5px -1px;
    border-radius: 5px;
    border: 1px solid rgb(36, 37, 40); }
    QSlider::add-page:horizontal {
    background: qlineargradient(x1:0, y1:0
    x2:0, y2:0, stop:0 #B1B1B1, stop:1 #c4c4c4); }
    QSlider::handle:horizontal:hover {
    background:rgb(43, 114, 184);
    border-color: rgb(43, 114, 184); }
    """
    return stylesheet

def main_button_stylesheet() -> str:
    stylesheet: str = """
    QPushButton {
    border: 1px solid rgb(50, 92, 134);
    border-radius: 2px;
    background-color: rgb(43, 114, 184);
    color: rgb(235, 235, 235); 
    font-family: Microsoft YaHei UI;
    font-size: 13px;
    }
    QPushButton:hover {
    border: 1px solid rgb(235, 235, 235);
    background-color: rgb(235, 235, 235);   
    color: rgb(115, 115, 122);
    }
    QPushButton:pressed {
    border: 1px solid rgb(64, 65, 70);
    background-color: rgb(36, 37, 40);  
    } """
    return stylesheet

def combobox_stylesheet(color:str, image_path: str) -> str:
    stylesheet: str = f"""
    QComboBox {{
    border: 2px solid transparent;
    border-radius: 5px;
    background-color: {color};
    font-family: Microsoft YaHei UI;
    font-weight: bold;
    font-size: 13px;
    padding: 1px 0px 1px 3px; /* This (useless) line resolves a bug with the font color */
    }}
    QComboBox:focus {{ color: black; }}
    QComboBox::drop-down {{ 
    background-color: {color};
    border: 0px; }}
    QComboBox::down-arrow {{
    image: url({image_path});
    width: 20px;
    height: 20px;
    padding-right: 20px;
    }}
    QComboBox QAbstractItemView {{
    border: 2px solid transparent;
    border-radius: 2px;
    background-color: {color};
    }}
    """
    return stylesheet

def sanitycheck_stylesheet(state: bool) -> str:
    color: str = "rgb(180, 255, 180)" if state else "rgb(255, 100, 100)"
    stylesheet: str = f"""
    QLabel {{ 
    color: {color};
    font-family: Microsoft YaHei UI;
    font-size: 11px;
    }}
    """
    return stylesheet