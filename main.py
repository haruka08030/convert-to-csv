import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(
        pdf_path,
        pages='all',
        multiple_tables=True,
        guess=True,
        stream=True,
        lattice=False
    )
    return tables

def save_tables_to_csv(tables, base_output_name):
    if tables:
        for i, df in enumerate(tables):
            if not df.empty:
                output_file = f"{base_output_name}_{i+1}.csv"
                df.to_csv(output_file, index=False, encoding='utf-8')
                print(f"✅ テーブル {i+1} を {output_file} に保存しました。")
    else:
        print("⚠️ PDF内に表が見つかりませんでした。")

pdf_file = 'list.pdf'
output_name = 'extracted_table'

all_tables = extract_tables_from_pdf(pdf_file)

save_tables_to_csv(all_tables, output_name)