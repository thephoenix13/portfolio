import markdown2
from xhtml2pdf import pisa

md_path = "D:/Projects/Pratik/projects_summary.md"
pdf_path = "D:/Projects/Pratik/Pratik_Gade_Profile.pdf"

with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

body_html = markdown2.markdown(md_content, extras=["tables", "fenced-code-blocks", "strike"])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @page {{
    size: A4;
    margin: 18mm 20mm 18mm 20mm;
  }}

  body {{
    font-family: Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    color: #1a1a1a;
    line-height: 1.6;
  }}

  h1 {{
    font-size: 22pt;
    color: #111;
    margin-bottom: 2px;
    margin-top: 0;
  }}

  h1 + p {{
    font-size: 10pt;
    color: #555;
    margin-top: 0;
    margin-bottom: 14px;
  }}

  h2 {{
    font-size: 13pt;
    color: #1a1a1a;
    border-bottom: 2px solid #2d6cdf;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
  }}

  h3 {{
    font-size: 10.5pt;
    color: #2d6cdf;
    margin-top: 16px;
    margin-bottom: 4px;
  }}

  h4 {{
    font-size: 9.5pt;
    color: #444;
    margin-top: 10px;
    margin-bottom: 2px;
  }}

  p {{
    margin: 4px 0 8px 0;
  }}

  strong {{
    color: #111;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e0e0e0;
    margin: 14px 0;
  }}

  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 9pt;
  }}

  th {{
    background-color: #2d6cdf;
    color: #fff;
    text-align: left;
    padding: 6px 10px;
    font-size: 8.5pt;
    font-weight: bold;
  }}

  td {{
    padding: 5px 10px;
    border-bottom: 1px solid #e8e8e8;
    vertical-align: top;
  }}

  tr:nth-child(even) td {{
    background-color: #f6f8ff;
  }}

  ul, ol {{
    margin: 4px 0;
    padding-left: 18px;
  }}

  li {{
    margin-bottom: 3px;
  }}

  code {{
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 2px;
    font-size: 8.5pt;
  }}
</style>
</head>
<body>
{body_html}
</body>
</html>"""

with open(pdf_path, "wb") as out_f:
    result = pisa.CreatePDF(html, dest=out_f)

if result.err:
    print(f"PDF generation failed with {result.err} errors.")
else:
    print(f"PDF saved to: {pdf_path}")
