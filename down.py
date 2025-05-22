from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=10)

# Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "50 Playwright JS Locator Examples with Descriptions", ln=True, align='C')
pdf.ln(5)
pdf.set_font("Arial", size=10)

# Data
locators = [
    ('page.locator(\'text=Submit\')', 'Finds element with exact text Submit.'),
    ('page.locator(\'button:has-text("Login")\')', 'Finds a button element that contains Login.'),
    ('page.locator(\'input[placeholder="Email"]\')', 'Finds input with placeholder Email.'),
    ('page.locator(\'input:has-text("Username")\')', 'Locates input that has inner text Username.'),
    ('page.locator(\'a\', { hasText: \'Home\' })', 'Finds anchor (<a>) that contains text Home.'),
    ('page.locator(\'div:has(span)\')', 'Finds a <div> that contains a <span>.'),
    ('page.locator(\'form:has(button:has-text("Submit"))\')', 'Locates form with a submit button inside.'),
    ('page.locator(\'li:has-text("Item 3")\')', 'Finds list item with text Item 3.'),
    ('page.locator(\'button\', { hasText: /Sign in/i })', 'Finds button with text Sign in (case-insensitive).'),
    ('page.locator(\'input[type="checkbox"]\')', 'Finds all checkboxes.'),
    ('page.locator(\'[data-testid="submit-btn"]\')', 'Locates using a custom test ID.'),
    ('page.locator(\'div:has-text("Welcome")\')', 'Locates <div> with inner text Welcome.'),
    ('page.locator(\'nav >> text=Dashboard\')', 'Finds text Dashboard within a <nav> tag.'),
    ('page.locator(\'table >> tr:has(td:has-text("User"))\')', 'Row in table with User in a cell.'),
    ('page.locator(\'section:has(h2:has-text("Features"))\')', 'Section with heading Features.'),
    ('page.locator(\'.card:has(.price-tag)\')', 'Card that has a .price-tag element.'),
    ('page.locator(\'ul >> li:has-text("Settings")\')', 'List item in <ul> with text Settings.'),
    ('page.locator(\'div[class*="container"]\')', 'Class name contains container.'),
    ('page.locator(\'h1:has-text("Welcome")\')', 'Heading 1 that says Welcome.'),
    ('page.locator(\'input:visible\')', 'Locates visible input fields only.'),
    ('page.locator(\'input:disabled\')', 'Locates disabled input fields.'),
    ('page.locator(\'input:checked\')', 'Locates checked checkbox or radio input.'),
    ('page.locator(\'a[href*="docs"]\')', 'Anchor tag with href containing docs.'),
    ('page.locator(\'[name="q"]\')', 'Finds element with attribute name="q".'),
    ('page.locator(\'.alert:has-text("Error")\')', 'Finds alert box with text Error.'),
    ('page.locator(\'#main:has(article)\')', 'Main div that has an article tag inside.'),
    ('page.locator(\'span:has-text("Online")\')', 'Span with status text Online.'),
    ('page.locator(\'input[type="password"]\')', 'Password input field.'),
    ('page.locator(\'button:is(:hover)\')', 'Button when hovered (pseudo-class).'),
    ('page.locator(\'div[role="dialog"]\')', 'ARIA role dialog.'),
    ('page.locator(\'[aria-label="Close"]\')', 'Element with accessibility label Close.'),
    ('page.locator(\'label:has-text("Username") + input\')', 'Input next to label Username.'),
    ('page.locator(\'tr >> td:nth-child(2)\')', 'Second column cell in a table row.'),
    ('page.locator(\'div:has-text("Sale") >> nth=0\')', 'First div with Sale.'),
    ('page.locator(\'li.selected\')', 'List item with class selected.'),
    ('page.locator(\'.tab:has-text("Overview")\')', 'Tab with label Overview.'),
    ('page.locator(\'div >> nth=2\')', 'Third div on the page.'),
    ('page.locator(\'section:has(.highlight)\')', 'Section containing a highlighted element.'),
    ('page.locator(\'div:has-text("Success"):visible\')', 'Visible div with Success.'),
    ('page.locator(\'form[action="/login"]\')', 'Login form via action attribute.'),
    ('page.locator(\'input:enabled\')', 'Only enabled input fields.'),
    ('page.locator(\'img[alt="Profile"]\')', 'Image with alt text Profile.'),
    ('page.locator(\'.list-group-item:has-text("Item 2")\')', 'List group item with text Item 2.'),
    ('page.locator(\'button:has-text("Remove"):visible\')', 'Visible remove button.'),
    ('page.locator(\'div.notification:has-text("Updated")\')', 'Notification with update message.'),
    ('page.locator(\'h3:has-text("Latest News")\')', 'Header with Latest News.'),
    ('page.locator(\'.modal-footer >> button:has-text("OK")\')', 'OK button inside modal footer.'),
    ('page.locator(\'select >> option:has-text("Philippines")\')', 'Option with value Philippines.'),
    ('page.locator(\'a:has-text("Learn more")\')', 'Anchor with Learn more text.'),
    ('page.locator(\'footer:has(a:has-text("Contact"))\')', 'Footer containing contact link.'),
]

# Add each locator
for i, (code, desc) in enumerate(locators, 1):
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 8, f'{i}. {code}', ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, f'Description: {desc}')
    pdf.ln(1)

# Save the PDF
pdf_path = "Playwright_JS_Locators_Tutorial.pdf"
pdf.output(pdf_path)

pdf_path
