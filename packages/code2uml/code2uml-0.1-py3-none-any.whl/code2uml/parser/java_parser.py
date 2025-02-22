from antlr4 import *

if "__main__" == __name__:
    from antlr.java import JavaLexer, JavaParser, JavaParserListener
else:
    from .antlr.java import JavaLexer, JavaParser, JavaParserListener
import json

def get_before_equal(s):
    if '=' in s:
        index = s.index('=')
        return s[:index]
    return s


class JavaClassListener(JavaParserListener.JavaParserListener):
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.current_class = None
        self.current_method = None
        self.classes = []

    def enterClassDeclaration(self, ctx: JavaParser.JavaParser.ClassDeclarationContext):
        class_name = ctx.identifier().getText()
        class_type = "class" if ctx.CLASS() is not None else "interface"
        # # print(f"{class_type} {class_name}")

        bases = []
        if ctx.typeType() is not None:
            bases.append(ctx.typeType().getText())
            # # print("extend", ctx.typeType().getText())

        if ctx.typeList() is not None:
            for type_list in ctx.typeList():
                for interface_type in type_list.typeType():
                    # # print("interface_type", interface_type)
                    interface_name = interface_type.getText()
                    bases.append(interface_name)
                    # # print(f"Implements: {interface_name}")

        if class_name not in self.parsed_data['classes']:
            self.parsed_data['classes'][class_name] = {
                'methods': [],
                'fields': [],
                'bases': bases
            }
        else:
            self.parsed_data['classes'][class_name]['bases'] = bases
        self.current_class = class_name
        self.classes.append(class_name)

    def exitClassDeclaration(self, ctx: JavaParser.JavaParser.ClassDeclarationContext):
        self.current_class = None
        self.classes.pop()
        if len(self.classes) != 0:
            self.current_class = self.classes[-1]

    def enterMethodDeclaration(self, ctx: JavaParser.JavaParser.MethodDeclarationContext):
        if not self.current_class:
            return

        method_name = ctx.identifier().getText()
        # return_type = ctx.typeType().getText() if ctx.typeType() else "void"
        return_type = self.get_return_type(ctx)
        # print("return_type:", return_type)
        
        parameters = self.getMethodParamters(ctx)
        
  
        # print("parameters:", parameters)
        # formalParameter
        
        # parameters = self._get_parameters(ctx.formalParameters().formalParameterList())
        
        # # print(f"Method: {method_name} ({return_type})")
        # # print(f"Parameters: {parameters}")

        self.current_method = method_name
        # print("method:", method_name)
        # print("methodBody:", ctx.methodBody().getText())
        self.parsed_data['classes'][self.current_class]['methods'].append(f'{return_type} {self.current_method}({parameters});')

    def enterInterfaceDeclaration(self, ctx: JavaParser.JavaParser.InterfaceDeclarationContext):
        class_name = ctx.identifier().getText()
        bases = []
        if ctx.typeList() is not None:
            for type_list in ctx.typeList():
                for interface_type in type_list.typeType():
                    # # print("interface_type", interface_type)
                    interface_name = interface_type.getText()
                    bases.append(interface_name)
                    # # print(f"Implements: {interface_name}")

        if class_name not in self.parsed_data['classes']:
            self.parsed_data['classes'][class_name] = {
                'methods': [],
                'fields': [],
                'bases': bases
            }
        else:
            self.parsed_data['classes'][class_name]['bases'] = bases
        # print("interface body:", ctx.interfaceBody().getText())
        self.current_class = class_name
        self.classes.append(class_name)
        
    def enterInterfaceMethodDeclaration(self, ctx: JavaParser.JavaParser.InterfaceMethodDeclarationContext):
        # function declaration
        method_name = ctx.interfaceCommonBodyDeclaration().identifier().getText()
        return_type = self.get_return_type(ctx.interfaceCommonBodyDeclaration())
        parameters = self.getMethodParamters(ctx.interfaceCommonBodyDeclaration())
        self.parsed_data['classes'][self.current_class]['methods'].append(f'{return_type} {method_name}({parameters});')
        
    def exitInterfaceMemberDeclaration(self, ctx: JavaParser.JavaParser.InterfaceMethodDeclarationContext):
        self.current_method = None
        
    def exitInterfaceDeclaration(self, ctx: JavaParser.JavaParser.InterfaceDeclarationContext):
        self.current_class = None
        self.classes.pop()
        if len(self.classes) != 0:
            self.current_class = self.classes[-1]

    def getMethodParamters(self, ctx):
        parameters = ""
        if ctx.formalParameters().formalParameterList() is not None:
            for formalParameter in ctx.formalParameters().formalParameterList().formalParameter():
                if formalParameter.typeType().classOrInterfaceType() is not None:
                    parameter_type = formalParameter.typeType().classOrInterfaceType().getText()
                else:
                    parameter_type = formalParameter.typeType().primitiveType().getText()
                if formalParameter.variableDeclaratorId() is not None:
                    parameter_name = formalParameter.variableDeclaratorId().identifier().getText()
                parameters += f"{parameter_type} {parameter_name}, "
            parameters = parameters[:-2]
        return parameters

    def get_return_type(self, ctx):
        return_type = ""
        if ctx.typeTypeOrVoid().VOID() is not None:
            return_type = "void"
        else:
            if ctx.typeTypeOrVoid().typeType().classOrInterfaceType() is not None:
                return_type = ctx.typeTypeOrVoid().typeType().classOrInterfaceType().typeIdentifier().IDENTIFIER().getText()
            elif ctx.typeTypeOrVoid().typeType().primitiveType() is not None:
                return_type = ctx.typeTypeOrVoid().typeType().primitiveType().getText()
            else:
                return_type = "constructor"
        return return_type
        

    def exitMethodDeclaration(self, ctx: JavaParser.JavaParser.MethodDeclarationContext):
        self.current_method = None

    def enterFieldDeclaration(self, ctx: JavaParser.JavaParser.FieldDeclarationContext):
        if not self.current_class:
            return

        field_type = ctx.typeType().getText()
        field_names = [id.getText() for id in ctx.variableDeclarators().variableDeclarator()]
        
        # 避免出现 int a = 1;
        # HashMap<String, Integer> map = new HashMap<>();的情况
        for name in field_names:
            name = get_before_equal(name)
            field = {
                'name': name,
                'type': field_type
            }
            self.parsed_data['classes'][self.current_class]['fields'].append(field)

    def _get_parameters(self, parameter_list):
        if not parameter_list:
            return []
        return [
            {
                'name': param.variableDeclarator().getText(),
                'type': param.typeType().getText()
            }
            for param in parameter_list.formalParameter()
        ]

    def _get_access_modifier(self, ctx):
        # print("_get_access_modifier typeType:", ctx.typeType().classOrInterfaceType())
        return 'default'

    def _is_static(self, ctx):
        return ctx.KW_STATIC() is not None

    def _is_abstract(self, ctx):
        return ctx.KW_ABSTRACT() is not None

    def _is_final(self, ctx):
        return ctx.KW_FINAL() is not None

def parse_java(code, line_numbers = 0):
    input_stream = InputStream(code)
    lexer = JavaLexer.JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParser.JavaParser(stream)
    tree = parser.compilationUnit()
    parsed_data = {'classes': {}, 'lines': line_numbers}
    listener = JavaClassListener(parsed_data)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return parsed_data

def parse_java_files(files):
    code = ""
    line = 0
    for fileName in files:
        with open(fileName, 'r') as file:
            code += file.read()
            line += len(file.readlines())
    if code == "":
        # print("No code found in the files.")
        exit()
    else :
        return parse_java(code, line)


if __name__ == '__main__':
    # Example Java code to parse
    java_code = """
    public class Example extends BaseClass implements Interface1, Interface2 {
        private int field1;
        protected static final String field2 = "value";

        public Example() {
        }

        public int method1(int param1, String param2) {
            return 0;
        }

        protected T method2(T param1, T param2) {
        }

        static void method3() {
        }
    }
    public class Example1 extends Example {
        public Example1() {
        }
        public void method4() {
        }
        int x;
    }
    """
    parsed_data = parse_java(java_code)
    str = json.dumps(parsed_data, indent=4)
    # print(str)
