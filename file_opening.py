from docxtpl import DocxTemplate

# document = Document('template/test_form.docx')
# document.save('new-file-name.docx')

doc = DocxTemplate('template/test_form.docx')
context = { 'initial' : "First_added text",
            'new_text': "Noviy text",
            'not_existing' : "not filled"}
doc.render(context)
doc.save("generated_doc.docx")