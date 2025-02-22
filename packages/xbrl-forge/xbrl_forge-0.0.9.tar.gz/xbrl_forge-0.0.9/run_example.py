import json

from src.xbrl_forge import create_xbrl, validate_input_data, load_input_data, convert_document

with open("examples/input_documents/stylesheet.css", "r") as f:
    style_data = f.read()
with open("examples/input_documents/ESEF-ixbrl.json", "r") as f:
    data_json = json.loads(f.read())
    validate_input_data(data_json)
    data = load_input_data(data_json)
with open("examples/input_documents/ESEF-ixbrl-2.json", "r") as f:
    data2_json = json.loads(f.read())
    validate_input_data(data2_json)
    data2 = load_input_data(data2_json)
with open("examples/input_documents/xbrl.json", "r") as f:
    data_xbrl_json = json.loads(f.read())
    validate_input_data(data_xbrl_json)
    data_xbrl = load_input_data(data_xbrl_json)
    
loaded_docx = convert_document("examples/file_conversions/Testing Docx document.docx")

results = create_xbrl([data, data2, data_xbrl, loaded_docx], styles=style_data)
results.save_files("examples/result", True)
results.create_package("examples/result", True)