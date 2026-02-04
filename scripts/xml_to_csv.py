import os
import xml.etree.ElementTree as ET
import csv

# CHANGE THIS PATH to your local ACNE04 annotation folder
XML_DIR = "ACNE04/Annotations"
OUTPUT_CSV = "acne04_labels.csv"

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    image_name = root.find("filename").text

    severity = root.find("severity")
    lesion_count = root.find("lesion_count")

    if severity is None or lesion_count is None:
        return None

    return {
        "image": image_name,
        "severity": int(severity.text),
        "lesion_count": int(lesion_count.text)
    }

def main():
    data = []

    for file in os.listdir(XML_DIR):
        if file.endswith(".xml"):
            record = parse_xml(os.path.join(XML_DIR, file))
            if record:
                data.append(record)

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["image", "severity", "lesion_count"]
        )
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV file created: {OUTPUT_CSV}")
    print(f"Total samples: {len(data)}")

if __name__ == "__main__":
    main()
