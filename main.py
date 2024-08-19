from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
import pytesseract
from pdf2image import convert_from_path

# convert to image using resolution 600 dpi 
pages = convert_from_path("scanned.pdf", 600)

# extract text
text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'
print(text_data)
yaml_file = "recognizer.yaml"
registry = RecognizerRegistry()
registry.add_recognizers_from_yaml(yaml_file)

analyzer = AnalyzerEngine(registry=registry)
results = analyzer.analyze(text_data, language="en")

print(results)