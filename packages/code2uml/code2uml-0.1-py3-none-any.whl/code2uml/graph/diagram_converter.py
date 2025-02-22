import json

class DiagramConverter:
    def __init__(self, json_data):
        self.data = json.loads(json_data) if isinstance(json_data, str) else json_data

    def to_plantuml(self):
        """Convert JSON data to PlantUML class diagram format"""
        result = ["@startuml"]
        # result.append("skinparam dpi 300")

        # Add classes
        for class_name, class_data in self.data['classes'].items():
            result.append(f"class {class_name} {{")
            for method in class_data['methods']:
                result.append(f"  {method}")
            for field in class_data['fields']:
                result.append(f"  {field['type']} {field['name']};")
            result.append("}")

        # Add inheritance relationships
        for class_name, class_data in self.data['classes'].items():
            for base_class in class_data['bases']:
                if base_class in self.data['classes']:
                    result.append(f"{base_class} <|-- {class_name}")

        # Add relationships based on method parameters
        # for class_name, class_data in self.data['classes'].items():
        #     for field in self.data['classes'][class_name]['fields']:
        #         for class_internal_name, class_intenal_data in self.data['classes'].items():
        #             if field == class_internal_name:
        #                 result.append(f"{class_name} --> {class_internal_name}")

        result.append("@enduml")
        return "\n".join(result)

    def to_mermaid(self):
        """Convert JSON data to Mermaid class diagram format"""
        result = ["classDiagram"]

        # Add classes
        for class_name, class_data in self.data['classes'].items():
            result.append(f"class {class_name} {{")
            for method in class_data['methods']:
                result.append(f"  {method}")
            for field in class_data['fields']:
                result.append(f"  {field['type']} {field['name']};")
            result.append("}")

        # Add inheritance relationships
        for class_name, class_data in self.data['classes'].items():
            for base_class in class_data['bases']:
                if base_class in self.data['classes']:
                    result.append(f"{class_name} --|> {base_class}")

        # Add relationships based on method parameters
        # for class_name, class_data in self.data['classes'].items():
        #     for field in self.data['classes'][class_name]['fields']:
        #         for class_internal_name, class_intenal_data in self.data['classes'].items():
        #             if field == class_internal_name:
        #                 result.append(f"{class_name} --> {class_internal_name}")

        return "\n".join(result)

def save_diagrams(json_data, base_filename):
    print("jsonData:", json.dumps(json_data, indent=4))
    converter = DiagramConverter(json_data)

    # Save PlantUML
    with open(f"{base_filename}.puml", "w") as f:
        f.write(converter.to_plantuml())

    # Save Mermaid
    with open(f"{base_filename}.mmd", "w") as f:
        f.write(converter.to_mermaid())

if __name__ == "__main__":
    # Example JSON data
    example_data = {
        "classes": {
            "A": {
                "methods": ["int testAdd(int x, int y)"],
                "fields": [],
                "bases": []
            },
            "B": {
                "methods": ["void useA(A a)"],
                "fields": [],
                "bases": []
            },
            "E": {
                "methods": ["int testAdd(int x, int y)"],
                "fields": [],
                "bases": ["A"]
            }
        }
    }

    save_diagrams(example_data, "example_diagram")