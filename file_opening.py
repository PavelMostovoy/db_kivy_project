import os

from docxtpl import DocxTemplate
from pathlib import Path
from docx import Document
import datetime
cur_dir = Path(__file__).parent
cur_date = datetime.date.today()
results_folder = cur_dir.joinpath(str(cur_date))
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

template_file = cur_dir.joinpath('template').joinpath('test_form.docx')
document = Document(template_file)
# document.save('new-file-name.docx')
def get_template(variable):
    destination_file = results_folder.joinpath(f"generated_doc{variable}.docx")
    doc = DocxTemplate(template_file)
    context = { 'initial' : "First_added text",
            'new_text': "Noviy text",
            'not_existing' : "not filled"}
    doc.render(context)
    doc.save(destination_file)

