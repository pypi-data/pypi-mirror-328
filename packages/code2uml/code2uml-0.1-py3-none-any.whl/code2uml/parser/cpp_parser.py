from antlr4 import *

# print("__name__:", __name__)
if "." == __name__:
    from antlr.cpp import CPP14Lexer, CPP14Parser
else:
    from .antlr.cpp import CPP14Lexer, CPP14Parser

import json

# ANTLR解析器,用于解析C++代码
class CPPListener(ParseTreeListener):
    def __init__(self, parsed_data):
        self.parsed_data = parsed_data
        self.current_class = None  # 跟踪当前解析的类名

    def enterIncludeDirective(self, ctx):
        include = ctx.children[1].getText()
        self.parsed_data['includes'].append(include)

    def enterNamespaceDefinition(self, ctx):
        namespace = ctx.namespaceName().getText()
        self.parsed_data['namespaces'].append(namespace)

    # 处理类定义
    def enterClassSpecifier(self, ctx):
        # 提取类名并初始化数据结构
        class_head = ctx.classHead()
        if class_head.classHeadName() and class_head.classHeadName().className():
            class_name = class_head.classHeadName().className().getText()
            self.parsed_data['classes'][class_name] = {
                'methods': [],
                'fields': [],
                'bases': []
            }
            self.current_class = class_name  # 设置当前类名
            # 解析继承关系
            base_clause = class_head.baseClause()
            # print("base_clause:", base_clause)
            if base_clause:
                base_spec_list = base_clause.baseSpecifierList()
                # print("base_spec_list:", base_spec_list)
                if base_spec_list:
                    for base_spec in base_spec_list.baseSpecifier():
                        base_info = self.parse_base_specifier(base_spec, class_head)
                        self.parsed_data['classes'][class_name]['bases'].append(base_info)

    def parse_base_specifier(self, base_spec_ctx, class_head):
        access_spec = None
        is_virtual = False
        base_type = ""
        class_key = class_head.classKey().getText().lower()
        # print("class_key:", class_key)

        # 遍历子节点提取信息
        for child in base_spec_ctx.getChildren():
            text = child.getText()
            if text == 'virtual' or text == 'override' or text == 'final' or text == 'public' or text == 'protected' or text == 'private':
                continue
            # print("child:", child.getText())
            base_type = child.getText()

        return base_type

    # 离开类定义
    def exitClassSpecifier(self, ctx):
        self.current_class = None  # 离开类作用域时重置

    def enterFunctionDefinition(self, ctx):
        # 提取返回类型
        return_type = ctx.declSpecifierSeq().getText() if ctx.declSpecifierSeq() else "void"
        # print("return_type:", return_type)
        # 处理函数定义（包括类方法）
        decl_spec = ctx.declSpecifierSeq()
        try:
            # 处理没有返回类型的构造函数/析构函数
            func_decl = decl_spec.getText() + " " if decl_spec else ""
            func_decl += ctx.declarator().getText()
        except AttributeError:
            func_decl = ctx.declarator().getText()

        # print("func_decl:", func_decl)

        declarator_text = ctx.declarator().getText()
        if '::' in declarator_text:
            parts = declarator_text.split('::')
            if len(parts) >= 2:
                class_part = parts[-2]
                # print("parts:", parts)
                # 获取类名，和初始化结构体
                class_name = class_part.split('<')[0].strip()
                if class_name not in self.parsed_data['classes']:
                    self.parsed_data['classes'][class_name] = {
                        'methods': [],
                        'fields': [],
                        'bases': []
                    }

                replace_class = parts[-2]
                # print("replace_class:", replace_class, "func_decl:", func_decl)
                func_decl = func_decl.replace(f"{replace_class}::", "")
                # print("func_decl:", func_decl)

                self.parsed_data['classes'][class_name]['methods'].append(func_decl)
                return

        # 如果当前在类的作用域中，添加到当前类的方法
        if self.current_class:
            self.parsed_data['classes'][self.current_class]['methods'].append(func_decl)
        else:
            self.parsed_data['functions'].append(func_decl)

    def enterMemberDeclaration(self, ctx):
        # 处理类成员声明（字段）
        # print("enterMemberDeclaration:")
        if ctx.memberDeclaratorList():
            for declarator in ctx.memberDeclaratorList().memberDeclarator():
                field_decl = declarator.getText()
                # print("field_decl:", field_decl)
                if self.current_class:
                    self.parsed_data['classes'][self.current_class]['fields'].append(field_decl)

def parse_cpp(code, line_numbers = 0):
    input_stream = InputStream(code)
    lexer = CPP14Lexer.CPP14Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPP14Parser.CPP14Parser(stream)
    tree = parser.translationUnit()

    parsed_data = {
        'classes': {},
        'lines': line_numbers
    }

    listener = CPPListener(parsed_data)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return parsed_data

def parse_cpp_files(files):
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
        return parse_cpp(code, line)

if __name__ == '__main__':
    # file_name = sys.argv[1]
    codeFile = ["../tests/cpp/a.h", "../tests/cpp/a.cpp"]
    parsed_data = parse_cpp_files(codeFile)
    str = json.dumps(parsed_data, indent=4)
    # print(str)
