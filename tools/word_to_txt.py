import os
import logging
import docx2txt

def word_to_txt(word_file, source_folder, output_folder):
    try:
        input_path = os.path.join(source_folder, word_file)
        output_path = os.path.join(output_folder, f"{os.path.splitext(word_file)[0]}.txt")
        
        text = docx2txt.process(input_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        logging.info(f"Converted {word_file} to TXT")
        return f"Converted {word_file} to TXT"
    except Exception as e:
        logging.error(f"Error converting {word_file} to TXT: {str(e)}")
        raise