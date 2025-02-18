import os
import chardet

def convert_to_utf8(file_path):
    try:
        # Read the file in binary mode
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            
        # Detect the encoding
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        
        print(f"File: {file_path}")
        print(f"Detected encoding: {encoding} (confidence: {confidence})")
        
        if encoding and encoding.lower() != 'utf-8':
            print(f"Converting {file_path} from {encoding} to utf-8")
            try:
                # Try to decode using detected encoding
                content = raw_data.decode(encoding)
                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    f.write(content)
                print("Conversion successful")
            except UnicodeDecodeError as e:
                print(f"Failed to decode with {encoding}: {str(e)}")
                # Try some common encodings
                for enc in ['cp1252', 'latin1', 'iso-8859-1', 'cp850', 'cp437', 'cp437', 'windows-1252']:
                    try:
                        content = raw_data.decode(enc)
                        with open(file_path, 'w', encoding='utf-8', newline='') as f:
                            f.write(content)
                        print(f"Successfully converted using {enc}")
                        break
                    except UnicodeDecodeError:
                        continue
        else:
            print("Already in UTF-8 format")
        print("-" * 80)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.robot', '.resource', '.py', '.bat', '.txt', '.md', '.ini', '.cfg', '.json', '.yaml', '.yml', '.html')):
                file_path = os.path.join(root, file)
                if '.venv' not in file_path:  # Skip virtual environment files
                    convert_to_utf8(file_path)

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    adpa_dir = os.path.join(os.path.dirname(os.path.dirname(script_dir)), 'adpa')  # Get the adpa directory
    process_directory(adpa_dir)
