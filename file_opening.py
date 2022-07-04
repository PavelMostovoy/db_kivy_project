from docxtpl import DocxTemplate
from pathlib import Path
from docx import Document
cur_dir = Path(__file__).parent

template_file = cur_dir.joinpath('test_form.docx')

document = Document(template_file)
# document.save('new-file-name.docx')
def get_template(variable):
    destination_file = cur_dir.joinpath(f"generated_doc{variable}.docx")
    doc = DocxTemplate(template_file)
    context = { 'initial' : "First_added text",
            'new_text': "Noviy text",
            'not_existing' : "not filled"}
    doc.render(context)
    doc.save(destination_file)

